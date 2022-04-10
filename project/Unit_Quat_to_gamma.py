import numpy as np
from Rot_to_Quat import Rot_to_Quat as RTQ


def Unit_Quat_to_gamma(g):
    R = g[0:3, 0:3]
    p = g[0:3, 3]
    p = p.reshape(3, 1)
    Quat = RTQ(R)
    gamma = np.vstack((p, Quat))
    return gamma
