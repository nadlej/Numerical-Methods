import numpy as np
from math import sqrt


def householder(A):
    n = len(A)

    for k in range(n - 2):
        i = k + 1
        P = A[i:n, i:n]
        u = A[i:n, k]
        s = sqrt(np.dot(u, u))
        if u[0] < 0: s = -s
        u[0] += s
        h = np.dot(u, u)
        v = 2 * np.dot(P, u) / h
        v -= (np.dot(u, v) / h) * u
        A[i:n, i:n] = P - np.outer(v, u) - np.outer(u, v)
        A[k, i] = -s

    return list(np.diagonal(A)), list(np.diagonal(A, 1))


maxIter = 500
tol = 1e-7

A = [[19 / 12, 13 / 12, 5 / 6, 5 / 6, 13 / 12, -17 / 12],
    [13 / 12, 13 / 12, 5 / 6, 5 / 6, -11 / 12, 13 / 12],
    [5 / 6, 5 / 6, 5 / 6, -1 / 6, 5 / 6, 5 / 6],
    [5 / 6, 5 / 6, -1 / 6, 5 / 6, 5 / 6, 5 / 6],
    [13 / 12, -11 / 12, 5 / 6, 5 / 6, 13 / 12, 13 / 12],
    [-17 / 12, 13 / 12, 5 / 6, 5 / 6, 13 / 12, 19 / 12]]

d, b = householder(np.array(A))

n = len(d)
x = [0.] * n
y = [0.] * (n - 1)
z = [0.] * n
c = [0.] * n
s = [0.] * n
q = [0.] * n

for k in range(maxIter):
    x[0] = d[0]
    y[0] = b[0]

    for j in range(1, n):
        i = j - 1
        z[i] = sqrt(x[i] ** 2 + b[i] ** 2)
        c[i] = x[i] / z[i]
        s[i] = b[i] / z[i]
        q[i] = c[i] * y[i] + s[i] * d[j]
        x[j] = -s[i] * y[i] + c[i] * d[j]

        if j != n - 1:
            y[j] = c[i] * b[j]

    z[n - 1] = x[n - 1]
    d[0] = s[0] * q[0] + c[0] * z[0]
    b[0] = s[0] * z[1]

    for j in range(1, n - 1):
        d[j] = s[j] * q[j] + c[j - 1] * c[j] * z[j]
        b[j] = s[j] * z[j + 1]

    d[n - 1] = c[n - 2] * z[n - 1]

    if sum([abs(bi) for bi in b]) < tol: break

print('Wartości własne')
for lambd in d:
    print('{:18.14f}'.format(lambd))
