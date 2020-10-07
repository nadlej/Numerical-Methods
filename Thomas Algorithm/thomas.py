
k = 7

Upper = [1, 1, 1, 1, 1, 1, 1]
Middle = [4,  4,  4, 4, 4, 4, 4]
Downer = [1, 1, 1, 1, 1, 1, 1]
Y = [1, 2, 3, 4, 5, 6, 7]

def Thomas():
     n = 6

     Downer[0] /= Middle[0]
     Y[0] /= Middle[0]

     for i in range(1,n):
         Downer[i] /= Middle[i] - Upper[i] * Downer[i-1]
         Y[i] = (Y[i] - Upper[i] * Y[i-1]) / (Middle[i] - Upper[i] * Downer[i-1])


     Y[n] = (Y[n] - Upper[n] * Y[n-1]) / (Middle[n] - Upper[n] * Downer[n-1])

     i = n-1
     while i >= 0:
         Y[i] -= Downer[i] * Y[i+1]
         i -= 1

def Answear():
    for i in range(k):
        print("X", i+1,"= ",'%.10f' % Y[i])

Thomas()
Answear()


