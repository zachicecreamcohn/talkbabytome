import random

def replace_word(english_string, target_word, replacement_word):
    # replace all instances of target_word  with replacement_word in english_string
    
    # target_word without capitalization
    target_word = target_word.lower()


    # english_string as a list of words
    english_string_list = english_string.split()
    for word in english_string_list:
        current_replacement_word = replacement_word
        # selected_word = word without punctuation or capitalization
        selected_word = word.strip(".,:;?!").lower()

        if selected_word == target_word:
            # if first letter of word is capitalized, capitalize replacement_word
            if word[0].isupper():
                current_replacement_word = current_replacement_word.capitalize()

            # if word has punctuation, add punctuation to replacement_word
            if word[-1] in ".,:;?!":
                current_replacement_word += word[-1]



            # print(f"REPLACEMENT WORD: {current_replacement_word}")
            english_string_list[english_string_list.index(word)] = current_replacement_word
        else:
            # print("not the word\n")
            pass
    # join the list of words back into a string
    return " ".join(english_string_list)


def replace_letter(english_string, target_letter, replacement_letter):
    # replace all instances of target_letter  with replacement_letter in english_string

    # for each letter in english_string, if it is target_letter, replace it with replacement_letter
    for letter in english_string:
        if letter == target_letter:
            #if letter is capitalized, capitalize replacement_letter
            if letter.isupper():
                english_string = english_string.replace(letter, replacement_letter.upper())
            else:
                english_string = english_string.replace(letter, replacement_letter)
    

    return english_string



baby_dict = {
    "mother": "mama",
    "father": "dada",
    "dad": "dada",
    "mom": "mama",	
    "cat" : "kitty",
    "dog" : "doggy",
    "puppy" : "doggy",
    "kitten" : "kitty",
    "I'm": "I",
    "I've": "I",
    "fucking": "poopy",
    "Fucking": "Poopy",
    "fuck": "poop",
    "Fuck": "Poop",
    "motherfucker": "poopy",
    "Motherfucker": "Poopy",
    "motherfucking": "poopy",
    "Motherfucking": "Poopy",
    "motherfuck": "poop",
    "Motherfuck": "Poop",
    "shit": "poop",
    "Shit": "Poop",
    "shithead": "poopy",
    "Shithead": "Poopy",
    "today": "tooday",
    "Today": "Tooday",
    "because": "becuz",
    "Because": "Becuz",	
    "and":'an',
    "And":'An',
    "all": "aw",
    "All": "Aw",
    "banana": "ba-ana",
    "Banana": "Ba-ana",
    "bear":"bar",
    "Bear":"Bar",
    "pacifier":"binkie",
    "Pacifier":"Binkie",
    "bird":"birdie",
    "Bird":"Birdie",
    "teddy":"bo-bo",
    "Teddy":"Bo-bo",
    "rabbit":"bunee",
    "Rabbit":"Bunee",
    "goodbye":"bye-bye",
    "Goodbye":"Bye-bye",
    "feces": "ca-ca",
    "Feces": "Ca-ca",
    "car": "car",
    "Car": "Car",
    "chips":"chip-chips",
    "Chips":"Chip-chips",
    "train":"choo-choo",
    "Train":"Choo-choo",
    "that": "dah",
    "That": "Dah",
    "doll":"dowy",
    "Doll":"Dowy",
    "duck": "ducky",
    "Duck": "Ducky",
    "even": "eben",
    "Even": "Eben",
    "fish":"fishee",
    "Fish":"Fishee",
    "butterflies":"fwuttabyes",
    "Butterflies":"Fwuttabyes",
    "goat":"gawt",
    "Goat":"Gawt",
    "horse":"horsie",
    "Horse":"Horsie",
    "goodnight":"nite-nite",
    "Goodnight":"Nite-nite",
    "tasty": "nummy",
    "Tasty": "Nummy",
    "don't": "nuh-nuh",
    "Don't": "Nuh-nuh",
    "dinner": "din-din",
    "Dinner": "Din-din",
    "speak": "tawk",
    "Speak": "Tawk",
    "spoke" : "tawked",
    "Spoke" : "Tawked",
    "didn't": "nuh-nuh",
    "Didn't": "Nuh-nuh",
    







    
    
    }
def english_to_babytalk(english_string):
    # for each key in baby_dict, replace all instances of key with value in english_string
    for key in baby_dict:
        english_string = replace_word(english_string, key, baby_dict[key])

    for word in english_string.split():
        # if word does not end with "er", do something
        if word[-2:] != "er":
            new_word = replace_letter(word, "r", "w")
            english_string = english_string.replace(word, new_word)
        
        
        # if word is "the" or "The", replace with "da" or "Da"
        if word == "the":
            english_string = english_string.replace(word, "da")
        elif word == "The":
            english_string = english_string.replace(word, "Da")

    
    
    # if word ends with "th", replace with "f"
    for word in english_string.split():
        if word[-2:] == "th":
            english_string = english_string.replace(word, word[:-2] + "f")

    # if word ends with "a", replace "a" with "uh"
    for word in english_string.split():
        not_yet_replaced = True
        for key in baby_dict:

            if (word.lower().strip() == baby_dict[key].lower().strip()) == True:
                not_yet_replaced = False
                break


        if not_yet_replaced == True:
            # print('hi')
            if word[-1] == "a":
                replace_letter(english_string, "a", "uh")


    
    # if word ends with "'s', replace with 'z'
    for word in english_string.split():
        if word[-2:] == "'s":
            english_string = english_string.replace(word, word[:-2] + "z")
    # convert all l's to w's
    english_string = replace_letter(english_string, "l", "w")
    
    # for each word in english_string, if it ends in s, replace it with z
    english_string_list = english_string.split()
    for word in english_string_list:
        # if word has punctuation, remove punctuation and add it to the end of the new word
        if word[-1] in ".,:;?!":
            punctuation = word[-1]
            word = word[:-1]
        else:
            punctuation = ""
        if word[-1] == "s":
            english_string_list[english_string_list.index(word+punctuation)] = word[:-1] + "z" + punctuation
    english_string = " ".join(english_string_list)

    # for each word in english_string, if it ends in "ing", replace it with "in"
    english_string_list = english_string.split()
    for word in english_string_list:
        if word[-3:] == "ing":
            english_string_list[english_string_list.index(word)] = word[:-3] + "in"
    english_string = " ".join(english_string_list)

    # for each word in english_string, if it contains "ough", replace wiht "o"
    english_string_list = english_string.split()
    for word in english_string_list:
        if "ough" in word:
            english_string_list[english_string_list.index(word)] = word.replace("ough", "o")
    english_string = " ".join(english_string_list)

    # for each word in english_string, if it ends with "er", replace it with "-wa"
    english_string_list = english_string.split()
    for word in english_string_list:
        if word[-1] in ".,:;?!":
            # if word ends in "er", replace it with "-wa"
            if word[-4:-1] == "ter":
                english_string_list[english_string_list.index(word)] = word[:-4] + "-wa" + word[-1]
        else:
            # if word ends in "er", replace it with "-wa"
            if word[-3:] == "ter":
                english_string_list[english_string_list.index(word)] = word[:-3] + "-wa"
        
    english_string = " ".join(english_string_list)

    # for each word in english_string, if double consonant, replace it with only one of those consonants
    english_string_list = english_string.split()
    for word in english_string_list:
        for i in range(len(word)-1):
            if word[i] in "bcdfghjklmnpqrstvwxz":
                try:
                    
                    if word[i] == word[i+1]:
                        word_as_list = list(word)
                        word_as_list.pop(i)
                        new_word = "".join(word_as_list)
                        english_string_list[english_string_list.index(word)] = new_word
                except Exception as e:
                    pass
    english_string = " ".join(english_string_list)

    return english_string

    


string_for_conversion = "I'm going to the store to buy some milk. Dad is gonna go with me."
# print(english_to_babytalk(string_for_conversion))


# return first string between quotes in string
def get_quoted_string(string):
    quotation_mark_type = '""'
    try:
        # replace all instances of "“" or "”" with "\""

        if "“" in string:
            quotation_mark_type = '“”'
        string = replace_letter(string,"“", "\"")
        string = replace_letter(string,"”", "\"")


        # escape all double quotes in string
        string = string.replace('"', '\\"')
    except Exception as e:
        print(e)
    # if string does not contain quotes, return None
    if string.count('"') == 0:
        return None
    else:
        # print(string.count('"'))

        
        # find first quote
        first_quote_index = string.find('"')

        # set second_half_of_string to all parts of string after first quote
        second_half_of_string = string[first_quote_index+1:]

        # find second quote
        second_quote_index = second_half_of_string.find('"')

        # return string between quotes
        return [second_half_of_string[:second_quote_index-1], quotation_mark_type]
        

            

def get_all_quoted_strings(string):
    # while string contains quotes, get quoted string and add it to list
    quoted_strings = []

    # redefine string
    selected_string = string
    #define boolean to keep track of whether or not get_quoted_string() has returned None
    no_quotes = False

    while no_quotes == False:
   
        found_quote = get_quoted_string(selected_string)
        
        


        # print(found_quote)
        if found_quote == None:
            no_quotes = True
        else:
            quotation_mark_type = found_quote[1]
            found_quote = found_quote[0]
            quoted_strings.append(found_quote)
            if quotation_mark_type == '“”':
                selected_string = selected_string.replace('“'+found_quote+'”', "")
            else:
                selected_string = selected_string.replace('"'+found_quote+'"', "")



    return quoted_strings
quote_test = "“When a member uses his or her national platform to encourage violence, tragically, people listen,” Speaker Nancy Pelosi of California said, adding that “depictions of violence can foment actual violence, as witnessed by this chamber on Jan. 6, 2021.”"





### USE:
# get_all_quoted_strings(quote_test) # returns a list of quotes found in original String.


