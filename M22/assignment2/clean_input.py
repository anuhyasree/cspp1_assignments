'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    """ revoming of special characters"""
    regex = re.compile('[^a-z0-9]')
    return regex.sub('', string)

def main():
    """main"""
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
