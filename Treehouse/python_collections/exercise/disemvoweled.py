def disemvowel(word):

    #list of vowels
    vowels = "aeiou"
    # list of letters to iterate through
    letters = list(word)
    # empty string
    disemvoweled = ""
    # iterate over the letters
    for letter in letters:
        # if this letter is a vowel
        if letter.lower() not in vowels:
            # remove it from the list
            disemvoweled += letter

    # overwrite the word variable with new string
    word = disemvoweled
    # return output

    return word

print(disemvowel('The quick brown fox jumped over 7 lazy dogs.'))
