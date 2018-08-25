'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
	"""main"""
    stri = ""
    num_lines = int(input())
    for i in range(num_lines):
        i += 1
        stri += input()
        stri += '\n'
    print(stri)

if __name__ == '__main__':
    main()
