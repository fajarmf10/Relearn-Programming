'''
Enter a string and the program will reverse it and print it out.
'''

def main():
    string = input("Enter your strings : ")
    string = (string)[::-1]
    print("Here is your reversed strings : " + string)

main()