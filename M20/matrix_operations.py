""" matrix multiplication and addition"""
def mult_matrix(math_1, math_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    result = []
    if len(math_1) == len(math_2[0]):
        for i in range(len(math_1)):
            lst = []
            for j in range(len(math_2[0])):
                total = 0
                for k in range(len(math_2)):
                    total += int(math_1[i][k])*int(math_2[k][j])
                lst.append(total)
            result.append(lst)
        return result
    else:
        print("Error: Matrix shapes invalid for mult")
        return None

def add_matrix(math_1, math_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    result = []
    if len(math_1) == len(math_2):
        for i in range(len(math_1)):
            lst = []
            for j in range(len(math_1[0])):
                lst.append(int(math_1[i][j])+int(math_2[i][j]))
            result.append(lst)
        return result
    else:
        print("Error: Matrix shapes invalid for addition")
        return None

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    line = input().split(",")
    row = int(line[0])
    col = int(line[1])
    matrix = []
    for i in range(row):
        line = input().split(" ")
        if len(line) == col:
            matrix.append([int(j) for j in line])
        else:
            print("Error: Invalid input for the matrix")
            return None
    return matrix

def main():
    # read matrix 1
    math_1 = read_matrix()
    # print(math_1)
    # read matrix 2
    math_2 = read_matrix()    
    # print(math_2)
    # add matrix 1 and matrix 2
    if math_1 != None and math_2 != None:
        print(add_matrix(math_1, math_2))
    # multiply matrix 1 and matrix 2
    if math_1 != None or math_2 != None:
        print(mult_matrix(math_1, math_2))
if __name__ == '__main__':
    main()
