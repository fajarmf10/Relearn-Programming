'''
Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.
'''
import re


def regex(string):
    if len(string) > 0:
        string = string.lower()
        pattern = re.compile('[a,e,i,o,u]')
        vowels = pattern.findall(string)
        return(len(vowels))
    else:
        return("Please enter the string!!")


def check_vowel(string):
    string.replace(" ", "")
    if len(string) > 0:
        string.lower()
        count = 0
        for i in string:
            if i in 'aiueo':
                count += 1
                print('Vowels found : ' + i)
            else: pass
    return('Total vowels found : %d' % count)

if __name__ == '__main__':
    string = input("Enter your string : ")
    # print(check_vowel(string))
    print(regex(string))
