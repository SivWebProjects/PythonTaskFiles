#Create parent class where you will have methods for matrix addition,
#multiplication, subtraction and transponse using numpy/math library.

#importing numpy library to manipulate large multi-dimensional arrays
import numpy as np

#all matrix operations done in methods
#methods and attributes are binded together
class ParentMatrix:
    def __init__(self, matrix_1, matrix_2):
        self.matrix_1 = matrix_1
        self.matrix_2 = matrix_2

    def addition(self):
        #add two matrices using numpy add() method and returns the result
        result = np.add(self.matrix_1, self.matrix_2)
        print("Addition of two matrices is: \n"+str(result))
    
    def subtraction(self):
        #subtracts two matrices using numpy subtract() method and returns the result
        result = np.subtract(self.matrix_1, self.matrix_2)
        print("Subtraction of two matrices is: \n"+str(result))
    
    def multiplication(self):
        #multiplies two matrices using numpy dot() method and returns the result
        result = np.dot(self.matrix_1, self.matrix_2)
        print("Multiplication of two matrices is: \n"+str(result))

    def transpose(self):
        #interchanging matrix rows into columns or columns into rows 
        #using numpy transpose() method and returns the result
        result_1 = np.transpose(self.matrix_1)
        print("Transpose of first matrix is: \n"+str(result_1))
        result_2 = np.transpose(self.matrix_2)
        print("Transpose of first matrix is: \n"+str(result_2))
        print()
        print()

class ChildMatrix(ParentMatrix):
    def __init__(self):
        super().__init__(matrix_1, matrix_2)
    
    def addition(self):
        result = [([(matrix_1[i][j] + matrix_2[i][j]) for j in range(len(matrix_1[0]))]) for i in range(len(matrix_1))]
        print("Addition of two matrices is: \n" + str(result))
    
    def subtraction(self):
        result = [([(matrix_1[i][j] - matrix_2[i][j]) for j in range(len(matrix_1[0]))]) for i in range(len(matrix_1))]
        print("Subtraction of two matrices is: \n" + str(result))

    def multiplication(self):
        result= [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix_2)] for row in matrix_1]
        print("Multplication of two matrices is: \n" + str(result))
    
    def transpose(self):
        result_1 = [([matrix_1[j][i] for j in range(len(matrix_1))]) for i in range(len(matrix_1[0]))]
        print("Transpose of first matrix is: \n" + str(result_1))

        result_2 = [([matrix_2[j][i] for j in range(len(matrix_2))]) for i in range(len(matrix_2[0]))]
        print("Transpose of second matrix is: \n" + str(result_2))


matrix_1 = np.array([[4, 5], [2,1]])
matrix_2 = np.array([[8, 4], [3,2]])

par_obj = ParentMatrix(matrix_1, matrix_2)
par_obj.addition()
par_obj.subtraction()
par_obj.multiplication()
par_obj.transpose()

child_obj = ChildMatrix()
child_obj.addition()
child_obj.subtraction()
child_obj.multiplication()
child_obj.transpose()