import sympy as sp
import simupy as sm

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

key_list = []
for key in sol.keys():
    key_list.append(key)

Xdot = sp.Matrix([[dx],[dq1],[dq2],[sol[key_list[0]]],[sol[key_list[1]]],[sol[key_list[2]]]])
X = sp.Matrix([[x],[q1],[q2],[dx],[dq1],[dq2]])
F_mat = sp.Matrix([[F]])




JF = Xdot.jacobian(F_mat)
JX = Xdot.jacobian(X)

JX_subs = sp.N(JX.subs([(x,0),(q1,0),(q2,0),(dx,0),(dq1,0),(dq2,0),(F,0)]))
sp.N(JX_subs)
JF_subs = sp.N(JF.subs([(x,0),(q1,0),(q2,0),(dx,0),(dq1,0),(dq2,0),(F,0)]))
sp.N(JF_subs)

# JX.subs(x,0)
# JX.subs(q1,0)
# JX.subs(q2,0)
# JX.subs(dx,0)
# JX.subs(dq1,0)
# JX.subs(dq2,0)
# JX.subs(F,0)
C = JF_subs
blah = JF_subs
for i in range(5):
    blah = JX_subs*blah
    C = C.row_join(blah) 
    

C = sp.N(C.subs([(M,10),(m1,10),(m2,1),(l1,2),(l2,1),(g,10)]))
