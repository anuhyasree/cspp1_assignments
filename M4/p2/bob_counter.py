'''Assume s is a string of lower case characters.
"""Write a program that prints the number of times the string 'bob' occurs"""
# in s. For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2'''
def main():
    """definition"""
    count_v = 0
    s_v = input()
    s_v2 = 'bob'
    for i in range(len(s_v)):
        if s_v2 == s_v[i:i+3]:
            count_v = count_v + 1
    print(count_v)
if __name__ == "__main__":
    main()
