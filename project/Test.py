import numpy as np
from motion_planning import motion_plan
import math as m

# Inputs

# Link Lengths:
l_1 = 270.35
l_2 = 69
l_3 = 364.35
l_4 = 69
l_5 = 374.29
l_6 = 10
l_7 = 374.42
l_8 = 229.525

# Thetas:
theta_1 = 0
theta_2 = 0
theta_3 = 0
theta_4 = 0
theta_5 = 0
theta_6 = 0
theta_7 = 0
theta_list = [theta_1, theta_2, theta_3, theta_4, theta_5, theta_6, theta_7]

# Tau:
t = .01

# Gst(0)
g_0 = np.array([[1/np.sqrt(2), -1/np.sqrt(2), 0, (l_2+l_3+l_5+l_8)*np.cos(np.pi/4)], [1/np.sqrt(2), 1/np.sqrt(2), 0,
                                                                                      (l_2+l_3+l_5+l_8)*np.sin(np.pi/4)], [0, 0, 1, (l_1-l_4-l_6)], [0, 0, 0, 1]])

c = 1/m.sqrt(2)
g_1 = np.array([
    [c, -c, 0, -500],
    [c, c, 0, 500],
    [0, 0, .999, 0],
    [0, 0, 0, 1]
])
g_2 = np.array([
    [c, -c, 0, -500],
    [c, c, 0, 500],
    [0, 0, .999, 500],
    [0, 0, 0, 1]
])
g_3 = np.array([
    [c, c, 0, 500],
    [-c, c, 0, 500],
    [0, 0, 1, 500],
    [0, 0, 0, 1]
])
g_4 = np.array([
    [0, 0, 1, 500],
    [0, 1, 0, 500],
    [-1, 0, 0, 500],
    [0, 0, 0, 1]
])

print("Desired Config-1")
print(g_1)
print("---------------------------------------------------------------------")
x = motion_plan(g_0, g_0, theta_list, g_1, t, 0, 750)
print("Final Config-1")
print(x)
print("Desired Config-2")
print(g_2)
print("---------------------------------------------------------------------")
x = motion_plan(g_0, g_1, theta_list, g_2, t, 0, 750)
print("Final Config-2")
print(x)
print("Desired Config-3")
print(g_3)
print("---------------------------------------------------------------------")
x = motion_plan(g_0, g_2, theta_list, g_3, t, 0, 750)
print("Final Config-3")
print(x)
print("Desired Config-4")
print(g_4)
print("---------------------------------------------------------------------")
x = motion_plan(g_0, g_3, theta_list, g_4, t, 0, 750)
print("Final Config-4")
print(x)
