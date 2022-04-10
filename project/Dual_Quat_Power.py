import numpy as np
from Conjuate_of_Dual_Quat import Conguate_DQ as CDQ
from Quat_product import Quat_Product as QP
from DualNum_Vector_Prod import Num_Vec_Prod as NVP


def Dual_Quat_Power(A, tau):
    # A is a 4x2 matrix
    # Set Up
    print(A.shape)
    Ar = A[0:4, 0]
    Ar = Ar.reshape(4, 1)
    Ad = A[0:4, 1]
    Ad = Ad.reshape(4, 1)
    A_Star = CDQ(A)
    Ar_Star = A_Star[0:4, 0]
    Ar_Star = Ar_Star.reshape(4, 1)
    # Finding components
    theta = 2*np.arccos(Ar[0])
    u1 = Ar[1]/np.sin(theta/2)
    u2 = Ar[2]/np.sin(theta/2)
    u3 = Ar[3]/np.sin(theta/2)
    u = np.array([u1, u2, u3])
    p_quat = QP(2*Ad, Ar_Star)
    p = p_quat[1:4]
    d = np.matmul(np.transpose(p), u)
    m = .5*(np.transpose(np.cross(np.transpose(p), np.transpose(u))) +
            ((p-(d*u))*(1/np.tan(theta/2))))
    u_bar = np.column_stack((u, m))
    cos_1 = np.cos((tau*theta)/2)
    cos_2 = -(((tau*d)/2)*np.sin((tau*theta)/2))
    Scalar = np.vstack((cos_1, cos_2)).transpose()
    sin_1 = np.sin((tau*theta)/2)
    sin_2 = ((tau*d)/2)*np.cos((tau*theta)/2)
    sin = np.vstack((sin_1, sin_2)).transpose()
    # In order to use Dual Num/Vector need to convert vector into a 4x2. 1st row isnt used, so can be dummy
    u_bar = np.vstack(([0, 0], u_bar))
    Vector = NVP(sin, u_bar)
    D_tau = np.vstack((Scalar, Vector))
    return D_tau
