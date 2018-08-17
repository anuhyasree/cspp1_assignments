#Assume s is a string of lower case characters.
"""Write a program that counts up the number of vowels"""
#contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and
#'u'. For example, if s = 'azcbobobegghakl', your program should print
#Number of vowels: 5
def main():
    """defination of bla"""
    s_tr = input("enter the string:")
    c_co = 0
    for char in s_tr:
        if char in 'AEIOUaeiou':
            c_co += 1
    print("number of vowels:" + str(c_co))
if __name__ == "__main__":
    main()
