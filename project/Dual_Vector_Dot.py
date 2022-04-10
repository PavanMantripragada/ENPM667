from Dual_Number_Products import Product
import numpy as np


def Dot(A, B):
    Av1 = Product(A[1, 0], A[1, 1], B[1, 0], B[1, 1])
    Av2 = Product(A[2, 0], A[2, 1], B[2, 0], B[2, 1])
    Av3 = Product(A[3, 0], A[3, 1], B[3, 0], B[3, 1])
    Dot = Av1+Av2+Av3
    return Dot
