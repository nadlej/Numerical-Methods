import numpy as np
def eigenvalue(A, v):
    Av = A.dot(v)
    return v.dot(Av)

def power_iteration (A, num_simulations ):

    b_k = np.ones(A.shape[0])
    for _ in range(num_simulations ):

        b_k1 = np.dot(A, b_k)
        b_k1_norm = np.linalg.norm(b_k1)
        b_k = b_k1 / b_k1_norm
        ev = eigenvalue(A,b_k)


    return b_k, ev

def power_iteration_second (A, num_simulations,v ):
    b_k = np.ones(A.shape[0])
    i = 0
    for _ in range(num_simulations ):

        b_k1 = np.dot(A, b_k)
        if i != 0:
            b_k1 = b_k1 - np.dot(v,np.dot(np.transpose(v),b_k1))
        else:
            b_k1 = np.dot(A, b_k)

        b_k1_norm = np.linalg.norm(b_k1)
        b_k = b_k1 / b_k1_norm
        ev = eigenvalue(A,b_k)
        i = i+1

    return b_k, ev



def main():
    A = np.array([[19. / 12., 13. / 12., 5. / 6., 5. / 6., 13. / 12., -17. / 12.],
                  [13. / 12., 13. / 12., 5. / 6., 5. / 6., -11. / 12., 13. / 12.],
                  [5. / 6., 5. / 6., 5. / 6., -1. / 6., 5. / 6., 5. / 6.],
                  [5. / 6., 5. / 6., -1. / 6., 5. / 6., 5. / 6., 5. / 6.],
                  [13. / 12., -11. / 12., 5. / 6., 5. / 6., 13. / 12., 13. / 12.],
                  [-17. / 12., 13. / 12., 5. / 6., 5. / 6., 13. / 12., 19. / 12.]])
    v = 0
    ev = 0

    v, ev = power_iteration(A,100)
    print("Wartosc własna I:", ev)
    print("Wektor własny I: ", v)
    v, ev = power_iteration_second(A,100,v)
    print("Wartosc własna I:", ev)
    print("Wektor własny I: ", v)

main()
