'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    """main"""
    string_len = ''
    num_lines = int(input())
    for i in range(num_lines):
        i += 1
        string_len += input()
        string_len += '\n'
    print(string_len)

if __name__ == '__main__':
    main()
