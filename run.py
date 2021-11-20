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
    if english_string == '':
        return redirect(url_for('home'))
    else:
        # return the quotes
        return render_template('results.html', result=english_to_babytalk(english_string))


# route for babyipsum 
@app.route('/babyipsum')
def babyipsum():
    ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Dictumst vestibulum rhoncus est pellentesque. Tempor id eu nisl nunc mi ipsum faucibus vitae aliquet. Id porta nibh venenatis cras sed felis eget. Pulvinar sapien et ligula ullamcorper. Sit amet consectetur adipiscing elit duis tristique. Tortor aliquam nulla facilisi cras. Et netus et malesuada fames ac turpis egestas. Quis auctor elit sed vulputate mi. Tincidunt nunc pulvinar sapien et. Iaculis nunc sed augue lacus viverra vitae congue eu consequat."""
    ipsum2 = "Est ante in nibh mauris. Adipiscing elit pellentesque habitant morbi tristique senectus et netus et. Volutpat diam ut venenatis tellus in metus vulputate eu. A diam sollicitudin tempor id eu nisl nunc mi. Vitae sapien pellentesque habitant morbi tristique senectus et. Adipiscing diam donec adipiscing tristique risus nec feugiat. Vestibulum mattis ullamcorper velit sed ullamcorper morbi tincidunt. Tellus integer feugiat scelerisque varius morbi enim nunc faucibus. Sit amet nisl suscipit adipiscing. Aliquam etiam erat velit scelerisque. Semper risus in hendrerit gravida rutrum quisque non tellus. Amet est placerat in egestas erat imperdiet sed. Porta non pulvinar neque laoreet suspendisse interdum consectetur. At consectetur lorem donec massa sapien."
    
    return render_template('results.html', p1=english_to_babytalk(ipsum), p2=english_to_babytalk(ipsum2))

# route for form submission newtranslation
@app.route('/newtranslation', methods=['POST'])
def newtranslation():

    # redirect to home page
    return redirect(url_for('home'))



# route for about page
@app.route('/about')
def about():
    return render_template('about.html', title = ' - ABOUT US', about=True)


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


