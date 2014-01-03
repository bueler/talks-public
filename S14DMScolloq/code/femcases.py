import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from genfig import convex2var, oneD, constraints3D

def gsconstrained(u0,psi,tol,DL,UU,bb):
    '''Run constrained Gauss-Seidel:
        (D+L) u^{k+1} = - U u^{k} + b
        u^{k+1} >= psi
    where  A u = b  is an  n x n  unconstrained linear system and  A = D + L + U
    is decomposition of  A  into diagonal, lower-triangular, upper-triangular
    parts.  Inputs:
        u0  = initial values for u  (length n+2)
        psi = constraint  (length n+2)
        tol = stop when |u^{k+1} - u^{k}| < tol, using L^2 norm
        DL  = D+L  (shape n x n)
        UU  = U  (shape n x n)
        bb  = b  (shape n x 1)
    Note that if  A  is  n x n  and  b  is  n x 1  then  u0, psi  have length
    n+2  because the linear system is for the interior points in a 1D system
    Returns final  u^{k+1}.'''
    m = len(u0)
    n = m-2
    assert np.shape(u0) == (m,)
    assert np.shape(psi) == (m,)
    assert np.shape(DL) == (n,n)
    assert np.shape(UU) == (n,n)
    assert np.shape(bb) == (n,)
    v = u0[1:n+1].copy()
    vold = v.copy()
    DL = np.array(DL)
    UU = np.array(UU)
    for itr in range(200):
        for i in range(n):
            vtmp = - np.dot(UU[i,:],v) + bb[i]
            if i > 0:
                vtmp = vtmp - np.dot(DL[i,:i],v[:i])
            vtmp = vtmp / DL[i,i]
            v[i] = np.maximum(vtmp, psi[i+1])
        print '.',
        c = LA.norm(v - vold)
        if c < tol:
            break
        vold = v.copy()
    print ':  %d iterations' % itr
    ufinal = u0.copy()
    ufinal[1:n+1] = v
    return ufinal

def gstestcase():
    # Gauss-Seidel test case with inactive constraint
    u0  = np.array([0.0, 3.0, 2.0, 4.0, 0.0])
    psi = np.array([-1.0, -1.0, -1.0, -1.0, -1.0])
    DL = [[2.0, 0.0, 0.0], [-1.0, 3.0, 0.0], [0.0, -1.0, 2.0]]
    UU = [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [0.0, 0.0, 0.0]]
    bb = [1.0, 1.0, 1.0]
    ugs = gsconstrained(u0,psi,1.0e-5,DL,UU,bb)
    ucorrect = np.array([0.0, 1.0, 1.0, 1.0, 0.0])
    print ugs
    print LA.norm(ugs-ucorrect)/LA.norm(u0)

def solvefem(dx,f0,psi,tol,**kwargs):
    '''Set up linear system from three-interior-point, equally-spaced FEM method
    applied to
       J[v] = \int_0^L (1/2) (v')^2 - f v.
    The corresponding unconstrained critical point condition is
       (grad J)(u) = A u - b = 0
    Solve the constrained problem for that system, i.e. the variational
    inequality
       (grad J)(u) (v - u) >= 0   for all v >= psi.'''
    # here A = DL + UU
    DL = [[2.0, 0.0, 0.0], [-1.0, 2.0, 0.0], [0.0, -1.0, 2.0]]
    UU = [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [0.0, 0.0, 0.0]]
    bb = f0 * dx**2 * np.ones(3)
    u0 = np.maximum(np.zeros(5),psi)
    return gsconstrained(u0,psi,tol,DL,UU,bb)

if __name__ == '__main__':
    #gstestcase()
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
        with plt.xkcd():
            fig1 = plt.figure()
            name = 'case_f%d_psi%d_convex.png' % (f0,mpsi)
            print 'saving to file "%s" ...' % name
            convex2var(psi[1:3],u[1:3],uno[1:3],name)
        fig2 = plt.figure()
        name = 'case_f%d_psi%d_oneD.png' % (f0,mpsi)
        print 'saving to file "%s" ...' % name
        oneD(x,psi,u,name)
        fig3 = plt.figure()
        name = 'case_f%d_psi%d_3D.png' % (f0,mpsi)
        print 'saving to file "%s" ...' % name
        constraints3D(u,psi,fig3,name)

