from Dual_Number_Products import Product
import numpy as np


def Num_Vec_Prod(A, B):
    AsB1 = Product(A[0, 0], A[0, 1], B[1, 0], B[1, 1])
    AsB2 = Product(A[0, 0], A[0, 1], B[2, 0], B[2, 1])
    AsB3 = Product(A[0, 0], A[0, 1], B[3, 0], B[3, 1])
    AB = np.array([AsB1, AsB2, AsB3])
    return(AB)
