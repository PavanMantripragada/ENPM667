from Dual_Number_Products import Product
import numpy as np


def Cross(E, F):
    R1 = Product(E[2, 0], E[2, 1], F[3, 0], F[3, 1]) - \
        Product(E[3, 0], E[3, 1], F[2, 0], F[2, 1])
    R2 = Product(E[3, 0], E[3, 1], F[1, 0], F[1, 1]) - \
        Product(E[1, 0], E[1, 1], F[3, 0], F[3, 1])
    R3 = Product(E[1, 0], E[1, 1], F[2, 0], F[2, 1]) - \
        Product(E[2, 0], E[2, 1], F[1, 0], F[1, 1])
    R = np.array([R1, R2, R3])
    return R
