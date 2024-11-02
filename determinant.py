"""
This program finds the determinant of an NxN matrix inputted by the user, where N as well as
each value a in the matrix are integers.
"""

def inputMatrix():
    matrix = []  # Initialize an empty matrix list
    matrixSize = int(input("For the NxN matrix, what is N? : "))  # Convert to integer directly
    for i in range(matrixSize):
        row = input("Enter row " + str(i + 1) + ": ")
        values = list(map(int, row.split()))  # Convert input to integers
        matrix.append(values)  # Append the row to the matrix
    return matrix



def findDet(matrix):
    matrixSize = len(matrix)
    detParts = [] # A list that holds the parts that comprise the determinant
    # Break case for recursion
    if matrixSize == 1:
        return matrix[0][0]
    else:
        for columnIndex in range(matrixSize):
            a = matrix[0][columnIndex]
            p = pow(-1, columnIndex)
            newMatrix = []
            # Construction of newMatrix
            for newRowIndex in range(matrixSize - 1):
                row = []
                for newColumnIndex in range(matrixSize):
                    if newColumnIndex != columnIndex:
                        row.append(matrix[newRowIndex + 1][newColumnIndex])
                newMatrix.append(row)
            c = p * findDet(newMatrix)
                    
            detParts.append(a * c)
            
        det = sum(detParts)
        return det
    
    
    
def main():
    matrix = inputMatrix()   
    det = findDet(matrix)
    
    print("\nThe determinant for the matrix")
    print()
    for row in matrix:
        for element in row:
            print(str(element), end=" ")
        print()
        
    print("\nis: ", det)
    
if __name__ == "__main__":
    main()