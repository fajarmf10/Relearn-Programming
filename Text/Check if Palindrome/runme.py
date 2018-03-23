'''
Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar”
'''

def palindrome(string):
    # Removes all case distinctions present
    string = string.casefold()
    # Reverse the string
    reverstring = reversed(string)
    # Checking using list
    if list(string) == list(reverstring):
        return('Palindrome')
    else:
        return('Not Palindrome')


if __name__ == '__main__':
    string = input('Please enter your string here : ')
    print(palindrome(string))
