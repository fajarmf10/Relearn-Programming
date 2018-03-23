'''
Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary.
'''

def count(words):
    return(len(words.split()))

if __name__ == '__main__':
    words = input('Please enter your string here : ')
    print(count(words))