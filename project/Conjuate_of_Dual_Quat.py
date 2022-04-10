import numpy as np


def Conguate_DQ(A):
    Q = A[0:4, 0]
    Q = Q.reshape(4, 1)
    P = A[0:4, 1]
    P = P.reshape(4, 1)
    Conj = np.array([[Q[0, 0], -Q[1, 0], -Q[2, 0], -Q[3, 0]], [
                     P[0, 0], -P[1, 0], -P[2, 0], -P[3, 0]]])
    Conj = np.transpose(Conj)
    return Conj
