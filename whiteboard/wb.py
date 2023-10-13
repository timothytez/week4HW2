# 'stop gninnips my sdrow' challenge:

# Write a function that takes in a string of one or more words,
# and returns the same string,
# but with all five or more letter words reversed.
# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.


#input: string
#output: string - 5 + letter words reversed
#constraints: consists of only letters & spaces only if 1 +word
#steps: if 5 + letters - reverse it, 5 letters or less - pass

#input: "this is a coding challenge"

#output: "this is a gnidoc egnellahc"

def atring_edit(astring):
    empty_string = []
    for word in astring.split ():
        if len(word) >=5:
            empty_string.append(word[::-1])
        else:
            empty_string.append(word)
    return ' '.join(empty_string)
            
words = 'this is a coding challenge'
print('coding[::-1]')



alist