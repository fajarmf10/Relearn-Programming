'''
From wikipedia :
Pig Latin is a language game or argot in which words in English are altered, usually by adding a fabricated suffix or by moving the onset or initial consonant or consonant cluster of a word to the end of the word and adding a vocalic syllable to create such a suffix. The objective is to conceal the words from others not familiar with the rules. The reference to Latin is a deliberate misnomer; Pig Latin is simply a form of argot or jargon unrelated to Latin, and the name is used for its English connotations as a strange and foreign-sounding language.

From description :
Pig Latin is a game of alterations played on the English language game. To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.
'''

import re


def pig_latin(string):
    if not string:
        return 'BLANK'

    # Lowercase the string
    string = string.lower()

    # Making the pattern of vowels
    pattern = re.compile('[a,e,i,o,u]')

    # for suffix
    y = 'y'
    tail = 'a' + y

    # Checking the string
    if string.startswith(y):
        # Return -yay
        return string + y + tail

    # Searching for vowel
    first_vowel = pattern.search(string)
    if not first_vowel:
        # Return -ay
        return string + tail

    # Getting the first vowel
    first_vowel = first_vowel.group()

    if string.find(first_vowel) == 0:
        # Return -yay
        return string + y + tail

    first, second = string.split(first_vowel, 1)
    return first_vowel + second + first + tail


if __name__ == '__main__':
    string = input("Enter your string : ")
    print(pig_latin(string))
