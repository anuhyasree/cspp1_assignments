"""perfect_square"""
def main():
    """your code here"""
    square = int(input())
    epsilon = 0.01
    guess = 0.0
    i = 0.0001
    num_of_guess = 0
    while abs(guess**2 - square) >= epsilon:
        guess += i
        num_of_guess += 1
    print('num_of_guess =', num_of_guess)
    if abs(guess**2 - square) >= epsilon:
        print('Failed')
    else:
        print(guess, 'is close to the square root of', square)
if __name__ == "__main__":
    main()
    