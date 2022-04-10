import numpy as np
from numpy.linalg import inv
from Unit_Quat_to_gamma import Unit_Quat_to_gamma as UQ_G
from Dual_Unit_Quaternion import DUQ
from Conjuate_of_Dual_Quat import Conguate_DQ as C_DQ
from Dual_Quat_product import Dual_Quat_Prod as DQP
from Dual_Quat_Power import Dual_Quat_Power as Power
from Dual_Quat_Gamma import Dual_Quat_to_Gamma as DQG
from SpatialManipJac import SpatialManipJac as SpatJac
from skew_matrix import skew
from Manipdkin import manipdkin as mani
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Givens for Spatial/Manip Jacobian

# Link Lengths:
l_1 = 270.35
l_2 = 69
l_3 = 364.35
l_4 = 69
l_5 = 374.29
l_6 = 10
l_7 = 229.525

type_joints = ["Rev", "Rev", "Rev",
               "Rev", "Rev", "Rev", "Rev"]
# Axis
w_list = [[0, 0, 1], [-1/np.sqrt(2), 1/np.sqrt(2), 0], [1/np.sqrt(2), 1/np.sqrt(2), 0], [-1/np.sqrt(2), 1/np.sqrt(
    2), 0], [1/np.sqrt(2), 1/np.sqrt(2), 0], [-1/np.sqrt(2), 1/np.sqrt(2), 0], [1/np.sqrt(2), 1/np.sqrt(2), 0]]


# Points on Axes
q_list = [[0, 0, 0], [l_2*np.cos(np.pi/4), l_2*np.sin(np.pi/4), l_1], [0, 0, l_1], [(l_2+l_3)*np.cos(np.pi/4), (l_2+l_3)*np.sin(np.pi/4), l_1-l_4], [(l_2+l_3)*np.cos(np.pi/4), (l_2+l_3)*np.sin(
    np.pi/4), l_1-l_4], [(l_2+l_3+l_5)*np.cos(np.pi/4), (l_2+l_3+l_5)*np.sin(np.pi/4), l_1-l_4-l_6], [(l_2+l_3+l_5)*np.cos(np.pi/4), (l_2+l_3+l_5)*np.sin(np.pi/4), l_1-l_4-l_6]]


def motion_plan(g_0, g, theta_list, g_f, tau, start, stop):
    # Setting up path of end effector:
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Motion Algorithm:
    for i in range(start, stop):
        # Step 1: Convert g(0) to unit quat (7,1) and dual unit quat
        gam_t = UQ_G(g)
        A_t = DUQ(g)
        A_f = DUQ(g_f)
        # Step 2: Compute A(t+1)
        A_star = C_DQ(A_t)
        x = DQP(A_star, A_f)
        y = Power(x, tau)
        A_t1 = DQP(A_t, y)
        # Step 3: Convert A(t+1) to gamma(t+1):
        gam_t1 = DQG(A_t1)
        # Setp 4: Computing Joint config(t+1), Jr_1:
        p = gam_t1[0: 3]
        p_hat = skew(p)
        Q = gam_t1[3: 7]
        beta = 1
        J_1 = np.array([[-Q[1, 0], Q[0, 0], Q[3, 0], -Q[2, 0]], [-Q[2, 0], -
                                                                 Q[3, 0], Q[0, 0], Q[1, 0]], [-Q[3, 0], Q[2, 0], -Q[1, 0], Q[0, 0]]])
        J = 2*np.matmul(p_hat, J_1)
        J_1 = 2*J_1
        J_2 = np.array([[1, 0, 0, J[0, 0], J[0, 1], J[0, 2], J[0, 3]], [0, 1, 0, J[1, 0], J[1, 1], J[1, 2], J[1, 3]], [0, 0, 1, J[2, 0], J[2, 1], J[2, 2], J[2, 3]], [
            0, 0, 0, J_1[0, 0], J_1[0, 1], J_1[0, 2], J_1[0, 3]], [0, 0, 0, J_1[1, 0], J_1[1, 1], J_1[1, 2], J_1[1, 3]], [0, 0, 0, J_1[2, 0], J_1[2, 1], J_1[2, 2], J_1[2, 3]]])
        Js = SpatJac(w_list, q_list, type_joints, theta_list)
        B = np.matmul(np.matmul(np.transpose(
            Js), (inv(np.matmul(Js, np.transpose(Js))))), J_2)
        if i == 0:
            theta_rate = np.transpose(np.array([theta_list]))
        else:
            theta_rate = theta_list
        Jr_1 = theta_rate+np.matmul((beta*B), (gam_t1-gam_t))
        # Step 5: computing g_bar using Manipdkin:
        g_bar_t1 = mani(g_0, w_list, q_list, type_joints, Jr_1)
        # Updating:
        g = g_bar_t1
        theta_list = Jr_1
        # Inputting coordinates into graph
        ax.scatter(g_bar_t1[0, 3], g_bar_t1[1, 3], g_bar_t1[2, 3], c='r')

    plt.show()
    return g_bar_t1
