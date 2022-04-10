import math as mat
import numpy as np


def Rot_to_Quat(R):
    r_11 = R[0, 0]
    r_12 = R[0, 1]
    r_13 = R[0, 2]
    r_21 = R[1, 0]
    r_22 = R[1, 1]
    r_23 = R[1, 2]
    r_31 = R[2, 0]
    r_32 = R[2, 1]
    r_33 = R[2, 2]
    mx = np.array([[1, 1, 1, 1], [1, -1, -1, 1],
                   [-1, 1, -1, 1], [-1, -1, 1, 1]])
    vec = np.array([[r_11], [r_22], [r_33], [1]])
    q = (1/4)*(mx.dot(vec))
    Q = np.argmax(q)
    if Q == 0:
        q_0 = mat.sqrt(q[0])
        q_1 = (r_32-r_23)/(4*q_0)
        q_2 = (r_13-r_31)/(4*q_0)
        q_3 = (r_21-r_12)/(4*q_0)
    if Q == 1:
        q_1 = mat.sqrt(q[1])
        q_0 = (r_32-r_23)/(4*q_1)
        q_2 = (r_12+r_21)/(4*q_1)
        q_3 = (r_13+r_31)/(4*q_1)
    if Q == 2:
        q_2 = mat.sqrt(q[2])
        q_0 = (r_13-r_31)/(4*q_2)
        q_1 = (r_12+r_21)/(4*q_2)
        q_3 = (r_23+r_32)/(4*q_2)
    if Q == 3:
        q_3 = mat.sqrt(q[3])
        q_0 = (r_21-r_12)/(4*q_3)
        q_1 = (r_13+r_31)/(4*q_3)
        q_2 = (r_23+r_32)/(4*q_3)
    # Rounded in order to keep consistent decimal places
    q_0 = round(q_0, 15)
    q_1 = round(q_1, 15)
    q_2 = round(q_2, 15)
    q_3 = round(q_3, 15)
    Quat = np.array([[q_0], [q_1], [q_2], [q_3]])
    return(Quat)
