import sympy as sp
import numpy as np

m1,m2,M,l1,l2,g = sp.symbols("m1 m2 M l1 l2 g")

A = sp.Matrix([[0,1,0,0,0,0],[0,0,-m1*g/M,0,-m2*g/M,0],
            [0,0,0,1,0,0],[0,0,-(M+m1)*g/(M*l1),0,-m2*g/(M*l1),0],
            [0,0,0,0,0,1],[0,0,-m1*g/(M*l1),0,-(M+m2)*g/(M*l2),0]])

B = sp.Matrix([[0],[1/M],[0],[1/(M*l1)],[0],[1/(M*l2)]])

I = sp.Matrix([[1,0,0,0,0,0],[0,0,0,1,0,0],[0,1,0,0,0,0],
             [0,0,0,0,1,0],[0,0,1,0,0,0],[0,0,0,0,0,1]])

A_new = I.inv() * A * I

B_new = I.inv() * B

print(B_new)
