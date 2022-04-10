import numpy as np
import skew_matrix as S_M


def AA_to_R(axis, angle):
    w_1 = axis[0]
    w_2 = axis[1]
    w_3 = axis[2]
    theta = angle
    w_list = np.array([w_1, w_2, w_3])
    w_list = w_list.reshape(3, 1)
    w_hat = S_M.skew(w_list)
    R = np.identity(3)+(w_hat*np.sin(theta)) + \
        ((w_hat.dot(w_hat))*(1-(np.cos(theta))))
    return (R)
