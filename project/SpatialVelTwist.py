import numpy as np


def Spatial_Vel(Jacobian, Joint_Rate):
    J_r = np.array(Joint_Rate)
    J_r = J_r.reshape(6, 1)
    Spatial_vel = np.matmul(Jacobian, J_r)
    Spatial_vel = Spatial_vel.reshape(6, 1)
    return Spatial_vel
