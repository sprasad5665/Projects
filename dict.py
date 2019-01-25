import json
import difflib
from difflib import get_close_matches

data = json.load(open("dd.json"))

#Function for retriving definition
def retrive_definition(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0:
        action = input("Did you mean %s instead? [y or n]: " % get_close_matches(word, data.keys())[0])
        if(action == 'y'):
            return data[get_close_matches(word, data.keys())[0]]
        elif(action=='n'):
            return ("The word doesn't exist, yet.")
        else:
            return ("We don't understand your entry. Apologies.")
             


word_user = input("Enter a word: ")


a=retrive_definition(word_user)

if type(a)==list:
    for item in a:
        print("-",item)
else:
    print("-",a)
    
