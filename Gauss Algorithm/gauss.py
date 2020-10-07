
Matrix = [ [4,1,0,0,0,0,1],
           [1,4,1,0,0,0,0],
           [0,1,4,1,0,0,0],
           [0,0,1,4,1,0,0],
           [0,0,0,1,4,1,0],
           [0,0,0,0,1,4,1],
           [1,0,0,0,0,1,4]]

Y = [1,2,3,4,5,6,7]

Answear = [0,0,0,0,0,0,0]

def TranformToUpper():
    for i in range(7):
        for j in range(i+1,7):
            c = Matrix[j][i] / Matrix[i][i]
            Y[j] = Y[j] - c * Y[i]

            for k in range(i,7):
                if i == k:
                    Matrix[j][k] = 0
                else:
                    Matrix[j][k] = Matrix[j][k] - c * Matrix[i][k]

def Backubstitution():
    i = 6
    while i >= 0:

        sum = 0.0

        for j in range(i+1,7):
            if i != j:
                sum += Matrix[i][j] * Answear[j]

        Answear[i] = (Y[i] - sum) / Matrix[i][i]
        i -= 1

def ShowAnswear():
    for i in range(7):
        print("X ", i + 1, "= ",'%.10f' % Answear[i])

TranformToUpper()
Backubstitution()
ShowAnswear()