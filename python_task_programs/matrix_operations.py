# Create parent class where you will have methods for matrix addition,
# multiplication, subtraction and transpose using numpy/math library.

# Importing numpy library to manipulate large multi-dimensional arrays
import numpy as np


class MatrixOperationsNumpy:
    """Performs matrix operations using numpy library."""
    def __init__(self, matrix_1, matrix_2):
        self.matrix_1 = matrix_1
        self.matrix_2 = matrix_2

    def addition(self):
        """Adds two matrices using numpy add() method"""
        result = np.add(self.matrix_1, self.matrix_2)
        print("Addition of two matrices is: \n"+str(result))
    
    def subtraction(self):
        """Subtracts two matrices using numpy subtract() method"""
        result = np.subtract(self.matrix_1, self.matrix_2)
        print("Subtraction of two matrices is: \n"+str(result))
    
    def multiplication(self):
        """Multiplies two matrices using numpy dot() method"""
        result = np.dot(self.matrix_1, self.matrix_2)
        print("Multiplication of two matrices is: \n"+str(result))

    def transpose(self):
        """Interchanging matrix rows into columns or columns into rows using numpy transpose() method"""
        result_1 = np.transpose(self.matrix_1)
        print("Transpose of first matrix is: \n"+str(result_1))
        result_2 = np.transpose(self.matrix_2)
        print("Transpose of first matrix is: \n"+str(result_2))
        print("----------*-----------")


class MatrixOperations(MatrixOperationsNumpy):
    """Performs matrix operations without using numpy library."""
    def __init__(self):
        super().__init__(matrix_1, matrix_2)
    
    def addition(self):
        """Adds two matrices"""
        result = [([(matrix_1[i][j] + matrix_2[i][j]) for j in range(len(matrix_1[0]))]) for i in range(len(matrix_1))]
        print("Addition of two matrices is: \n" + str(result))
    
    def subtraction(self):
        """Subtracts two matrices using numpy subtract() method"""
        result = [([(matrix_1[i][j] - matrix_2[i][j]) for j in range(len(matrix_1[0]))]) for i in range(len(matrix_1))]
        print("Subtraction of two matrices is: \n" + str(result))

    def multiplication(self):
        """Multiplies two matrices using numpy dot() method"""
        result= [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix_2)] for row in matrix_1]
        print("Multiplication of two matrices is: \n" + str(result))
    
    def transpose(self):
        """Interchanging matrices rows into columns"""
        result_1 = [([matrix_1[j][i] for j in range(len(matrix_1))]) for i in range(len(matrix_1[0]))]
        print("Transpose of first matrix is: \n" + str(result_1))

        result_2 = [([matrix_2[j][i] for j in range(len(matrix_2))]) for i in range(len(matrix_2[0]))]
        print("Transpose of second matrix is: \n" + str(result_2))


matrix_1 = np.array([[4, 5], [2,1]])
matrix_2 = np.array([[8, 4], [3,2]])

# Create instance of MatrixOperationsNumpy
par_obj = MatrixOperationsNumpy(matrix_1, matrix_2)

# Calling instance methods of MatrixOperationsNumpy
par_obj.addition()
par_obj.subtraction()
par_obj.multiplication()
par_obj.transpose()

# Create instance of MatrixOperations
child_obj = MatrixOperations()

# Calling instance methods of MatrixOperations
child_obj.addition()
child_obj.subtraction()
child_obj.multiplication()
child_obj.transpose()
