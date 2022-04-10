import numpy as np
from Rot_to_Quat import Rot_to_Quat as RTQ
from Quat_product import Quat_Product


def DUQ(g):
    R = g[0:3, 0:3]
    Ar = RTQ(R)  # Real Values
    p = g[0:3, 3]
    p = p.reshape(3, 1)
    P_quat = np.vstack((0, p))
    Ad = .5*Quat_Product(P_quat, Ar)  # Dual Part
    A = np.column_stack((Ar, Ad))
    return A
