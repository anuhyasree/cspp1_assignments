"""Exercise: Assignment-2
 Write a Python function, sumofdigits, that takes in
 one number and returns the sum of digits of given number.
 This function takes in one number and returns one number.
"""
def sumofdigits(n_number):
    '''
    n is positive Integer
    returns: a positive integer, the sum of digits of n.
    '''
    if n_number == 0:
        return 0
    return (n_number % 10) + sumofdigits(n_number // 10)
def main():
    """def"""
    a_num = input()
    print(sumofdigits(int(a_num)))
if __name__ == "__main__":
    main()
