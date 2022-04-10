import numpy as np
from AdjointOfg import Adjoint
from e_xi_hat import trans_matrix


def SpatialManipJac(w_list, q_list, type_joints, theta):
    # Setup
    n_j = len(type_joints)
    initial = np.identity(4)
    g_list = []
    for i in range(n_j):
        g = trans_matrix(w_list[i], q_list[i], theta[i])
        g_list.append(g)
    # Finding zi_1
    if type_joints[0] == "Rev":
        w = np.array(w_list[0])
        w = w.reshape(3, 1)
        q = np.array(q_list[0])
        q = q.reshape(3, 1)
        x = np.transpose(np.cross(np.transpose(-w), np.transpose(q)))
        zi_1 = np.array([[x], [w]])
        zi_1 = zi_1.reshape(6, 1)
    if type_joints[0] == "Pris":
        v = np.array(w_list[0])
        v = v.reshape(3, 1)
        O = np.zeros([3, 1])  # u=O
        zi_1 = np.array([[v], [O]])
        zi_1 = zi_1.reshape(6, 1)
    Manip_Jac = zi_1
    # 2nd find zi_2-n/convert to zi_hat and append to Manip_Jac
    for i in range(1, n_j):
        g = np.matmul(initial, g_list[i-1])
        Adj = Adjoint(g)
        initial = g
        if type_joints[i] == "Rev":
            w = np.array(w_list[i])
            w = w.reshape(3, 1)
            q = np.array(q_list[i])
            q = q.reshape(3, 1)
            x = np.transpose(np.cross(np.transpose(-w), np.transpose(q)))
            zi = np.array([[x], [w]])
            zi = zi.reshape(6, 1)
        if type_joints[i] == "Pris":
            v = np.array(w_list[i])
            v = v.reshape(3, 1)
            O = np.zeros([3, 1])
            zi = np.array([[v], [O]])
            zi = zi.reshape(6, 1)
        zi_hat = np.matmul(Adj, zi)
        Manip_Jac = np.around(np.column_stack((Manip_Jac, zi_hat)), 4)
    return Manip_Jac
