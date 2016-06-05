class Matrix:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def create_matrix(self):
        z=[["value" for i in range(self.x)]for j in range(self.y)]
        for i in range(len(z)):
            for j in range(len(z)):
                z[i][j]= input("enter values for matrix items")

        print "matrix list is",z
        print "Matrix is"
        for p in z:
            print p
            
        return z
class MatrixAdd:
    def __init__(self,matrix1,matrix2):
        self.matrix1=matrix1
        self.matrix2=matrix2
    def matrix_add(self):
        matrix3= [x+y for x,y in zip(self.matrix1,self.matrix2)]
        print matrix3
        #for i,j in range(len(self.matrix1)):
         #   for p,q in range(len(self.matrix2)):
          #      matrix3= [x+y for x,y in zip(self.matrix1,self.matrix2)]
           # print matrix3
        return matrix3
            
        

a=input("enter matrix row size")
b=input("enter matrix column size")
m1=Matrix(a,b)
m2=Matrix(a,b)
matrix1=m1.create_matrix()
matrix2=m2.create_matrix()

m3=MatrixAdd(matrix1,matrix2)
m3.matrix_add()
