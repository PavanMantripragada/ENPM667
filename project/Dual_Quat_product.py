import numpy as np
from Dual_Number_Products import Product
from Dual_Vector_Dot import Dot
from DualNum_Vector_Prod import Num_Vec_Prod as NVP
from Dual_Vector_Cross import Cross


def Dual_Quat_Prod(A, B):
    # A and B are both dual unit quaternions, therefore 4 quaternions present
    # Scalar Part:
    AsBs = Product(A[0, 0], A[0, 1], B[0, 0], B[0, 1])
    AvBv = Dot(A, B)
    Scalar = AsBs-AvBv
    # Vector Component:
    AsBv = NVP(A, B)
    BsAv = NVP(B, A)
    AB = AsBv+BsAv
    ABv = Cross(A, B)
    Vector = AB+ABv
    Result = np.vstack((Scalar, Vector))
    return Result
