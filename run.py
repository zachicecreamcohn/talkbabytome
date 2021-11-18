# flask app for the web interface

# import get_all_quoted_strings() from file babytalk.py
from babytalk import get_all_quoted_strings, english_to_babytalk

# import flask
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

# start the flask app
app = Flask(__name__)

# routes
@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('main_form.html')

# route for form submission
@app.route('/quotes', methods=['POST'])
def quotes():
    # get the form data
    english_string = request.form['english_string']

    # return the quotes
    return render_template('results.html', result=english_to_babytalk(english_string))



# route for form submission newtranslation
@app.route('/newtranslation', methods=['POST'])
def newtranslation():
    # get the form data
    english_string = request.form['newtranslation']

    # redirect to home page
    return redirect(url_for('home'))

# route for about page
@app.route('/about')
def about():
    return render_template('about.html', title = ' - ABOUT US')


# route for api
@app.route('/api/quotes', methods=['POST'])
def api_quotes():
    # get the form data
    english_string = request.form['english_string']
    
    
    
    # get the quotes
    quotes = get_all_quoted_strings(english_string)

    # get english and convert to baby
    # return jsonify(english_to_babytalk(english_string))

    # return the quotes
    return jsonify(quotes)
    

# handle error 404
@app.errorhandler(404)
def page_not_found(e):
    errortitle = '404 Error'
    errormessage = 'Page not found'
    return render_template('error.html', errortitle=errortitle, errormessage=errormessage), 404



# run the app
if __name__ == '__main__':
    app.run(debug=True)


