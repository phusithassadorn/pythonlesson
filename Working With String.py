phrase = "Phusit Hassadorn"

print(phrase + "is cool") # string is plain text container

print(phrase.lower()) # make small form of text ex. abcdefghijklmnopqrstuvwxyz
print(phrase.upper()) # make big form of text ex. ABCDEFGHIJKLMNOPQRSTUVWXYZ

print(phrase.isupper()) # check a text and show in bool form ex. true,false in this case is show false 
print(phrase.upper().isupper()) # upper convert small text to big text and check a text 

print(phrase[0]) # show character position in this case 0 position is P
print(len(phrase)) # count the charecter

print(phrase.index("P")) # search the text position to show in this case P is 0 because P is the first charecter

print(phrase.replace("Phusit","Cat")) # repalce a text
