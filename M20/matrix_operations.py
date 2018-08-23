def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    result = []
    if len(m1) == len(m2[0]):
        for i in range(len(m1)):
            lst = []
            for j in range(len(m2[0])):
                sum = 0
                for k in range(len(m2)):
                    sum += int(m1[i][k])*int(m2[k][j])
                lst.append(sum)
            result.append(lst)
        return result
    else:
        print("Error: Matrix shapes invalid for mult")
        return None

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    result = []
    if len(m1) == len(m2):
        for i in range(len(m1)):
            lst = []
            for j in range(len(m1[0])):
                lst.append(int(m1[i][j])+int(m2[i][j]))
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
    r = int(line[0])
    c = int(line[1])
    matrix = []
    for i in range(r):
        line = input().split(" ")
        if len(line) == c:
            matrix.append([int(j) for j in line])
        else:
            print("Error: Invalid input for the matrix")
            return None
    return matrix

def main():
    # read matrix 1
    m1 = read_matrix()
    # print(m1)
    # read matrix 2
    m2 = read_matrix()    
    # print(m2)

    # add matrix 1 and matrix 2
    if m1 != None and m2 != None:
        print(add_matrix(m1, m2))

    # multiply matrix 1 and matrix 2
    if m1 != None or m2 != None:
        print(mult_matrix(m1, m2))
    

if __name__ == '__main__':
    main()
