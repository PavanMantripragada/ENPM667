import sympy as sp

t = sp.symbols("t")

M,m1,m2 = sp.symbols("M m1 m2")
l1,l2,g,F = sp.symbols("l1 l2 g F")
f_x = sp.Function("x")
f_q1 = sp.Function("theta_1")
f_q2 = sp.Function("theta_2")
x = f_x(t)
q1 = f_q1(t)
q2 = f_q2(t)

dx = sp.diff(x,t)
dq1 = sp.diff(q1,t)
dq2 = sp.diff(q2,t)

v12 = (dx+l1*sp.cos(q1)*dq1)**2 + (l1*sp.sin(q1)*dq1)**2
v22 = (dx+l2*sp.cos(q2)*dq2)**2 + (l2*sp.sin(q2)*dq2)**2

K = 0.5*(M*dx**2 + m1*v12 + m2*v22)
P = -m1*g*l1*sp.cos(q1) - m2*g*l2*sp.cos(q2)

L = K - P

dL_x = sp.diff(L,x)
dL_dx = sp.diff(L,dx)
Term_x = sp.diff(dL_dx,t) - dL_x - F

dL_q1 = sp.diff(L,q1)
dL_dq1 = sp.diff(L,dq1)
Term_q1 = sp.diff(dL_dq1,t) - dL_q1

dL_q2 = sp.diff(L,q2)
dL_dq2 = sp.diff(L,dq2)
Term_q2 = sp.diff(dL_dq2,t) - dL_q2


sol = sp.solve((Term_x,Term_q1,Term_q2),sp.Derivative(x, (t, 2)),
                sp.Derivative(q1, (t, 2)),sp.Derivative(q2, (t, 2)))

#print(sp.Derivative(q1, (t, 2)))
#print(sol)
#print(sp.latex(sp.simplify(Term_x)))