import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from femgenfig import convex2var, oneD, constraints3D
from fem1d import solvefem

if __name__ == '__main__':
    x = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
    dx = 0.25
    for (f0,mpsi) in (0,1), (2,0), (2,3), (-1,-1):
        if mpsi > -1:
            psi = mpsi * np.array([-0.2,0.1,0.2,0.15,-0.1])
        else:
            psi = np.array([-0.2,0.4,0.2,0.3,-0.12])
        tol = 1.0e-12
        u   = solvefem(dx,f0*1.0,psi,tol)
        print 'with    constraint: u_1=%f, u_2=%f' % (u[1],u[2])
        uno = solvefem(dx,f0*1.0,-1.0*np.ones(np.shape(psi)),tol)
        print 'without constraint: u_1=%f, u_2=%f' % (uno[1],uno[2])
        #with plt.xkcd():
        fig1 = plt.figure()
        name = 'case_f%d_psi%d_convex.png' % (f0,mpsi)
        print 'saving to file "%s" ...' % name
        convex2var(u,psi,uno[1:3],name,dx=dx,f0=f0)
        fig2 = plt.figure()
        name = 'case_f%d_psi%d_oneD.png' % (f0,mpsi)
        print 'saving to file "%s" ...' % name
        oneD(x,psi,u,name)
        fig3 = plt.figure()
        name = 'case_f%d_psi%d_3D.png' % (f0,mpsi)
        print 'saving to file "%s" ...' % name
        constraints3D(u,psi,fig3,name)

