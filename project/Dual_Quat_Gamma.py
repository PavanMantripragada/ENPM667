import numpy as np
from Quat_product import Quat_Product as QP
from Conjuate_of_Dual_Quat import Conguate_DQ as CDQ


def Dual_Quat_to_Gamma(A):
    Ar = A[0:, 0]
    Ar = Ar.reshape(4, 1)
    Ad = A[0:, 1]
    Ad = Ad.reshape(4, 1)
    A_Star = CDQ(A)
    Ar_Star = A_Star[0:, 0]
    Ar_Star = Ar_Star.reshape(4, 1)
    p_quat = QP(2*Ad, Ar_Star)
    p = p_quat[1:4]
    gamma = np.vstack((p, Ar))
    return gamma
