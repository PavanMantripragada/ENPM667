import sympy as sp

# problem 6
p11,p12,p21,p22 = sp.symbols("p11 p12 p21 p22")

P = sp.Matrix([[p11,p12],[p21,p22]])
A = sp.Matrix([[-3,2],[-1,-1]])
Q = sp.eye(2)

L = A.T * P + P * A
print(L)

eq1 = sp.Eq(L[0,0] + 1,0)
eq2 = sp.Eq(L[0,1],0)
eq3 = sp.Eq(L[1,0],0)
eq4 = sp.Eq(L[1,1] + 1,0)

sol = sp.solve((eq1,eq2,eq3,eq4),(p11,p12,p21,p22))
print(sol)

det = sol[p11]*sol[p22] - sol[p12]*sol[p21]
print("determinant : ",det)




# problem 5
S = sp.eye(3)
#S = sp.Matrix([[0,1,1],[1,0,0],[0,1,-1]])
A = sp.Matrix([[1,1,0],[0,1,0],[0,1,1]])
B = sp.Matrix([[0,1],[1,0],[0,1]])
A_hat = S.inv() * A * S
B_hat = S.inv() * B
print(A_hat)
print(B_hat)

# problem 4
B = sp.Matrix([[0],[1]])
print(B*B.T)

