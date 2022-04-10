import numpy as np
from skew_matrix import skew


def Quat_Product(Q, P):
    q_0 = Q[0]
    q = Q[1:4]
    q_hat = skew(q)
    I = np.identity(3)
    x = (q_0 * I)+q_hat
    Q_plus = [[q_0[0], -q[0, 0], -q[1, 0], -q[2, 0]], [q[0, 0], x[0, 0], x[0, 1], x[0, 2]],
              [q[1, 0], x[1, 0], x[1, 1], x[1, 2]], [q[2, 0], x[2, 0], x[2, 1], x[2, 2]]]
    Q_Prod = np.matmul(Q_plus, P)
    return Q_Prod
