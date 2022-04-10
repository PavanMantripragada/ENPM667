import numpy as np
import Function_Axis_Angle_to_Rot as AAR
import g_matrix_converter as g_m


def manipdkin(gst0, axis_joints, q_joints, type_joints, theta_list):
    n_j = len(type_joints)
    initial = np.identity(4)  # dummy variable
    Transform = []
    for i in range(n_j):
        if type_joints[i] == "Rev":
            axis = axis_joints[i]
            angle = theta_list[i, 0]
            e_w_hat = AAR.AA_to_R(axis, angle)
            y = (np.identity(3)-e_w_hat).dot(q_joints[i])
            y = y.reshape(3, 1)
            x = e_w_hat
            g = g_m.g_converter(x, y)
        if type_joints[i] == "Pris":
            x = np.identity(3)
            y = axis_joints[:, i].dot(theta_list[i])
            g = g_m.g_converter(x, y)
        # iterates g's for necessary amount of iterations
        # updates the new values into the current transformation list
        Transform.append(g)
    for g in range(len(Transform)):
        Transform[g] = np.matmul(initial, Transform[g])
        initial = Transform[g]
    gst_theta = np.matmul(initial, gst0)
    return(gst_theta)
