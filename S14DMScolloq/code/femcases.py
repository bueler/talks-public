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
        tol = stop when |u^{k+1} - u^{k}|/|u0[1:n+1]| < tol, using L^2 norm
        DL  = D+L  (shape n x n)
        UU  = U  (shape n x n)
        bb  = b  (shape n x 1)
    Note that if  A  is  n x n  and  b  is  n x 1  then  u0, psi  have length
    n+2  because the linear system is for the interior points in a 1D system
    Returns final  u^{k+1}.'''
    m = len(u0)
    n = m-2
    assert np.shape(u0) == (m,)
    assert LA.norm(u0) > 0.0
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
        c = LA.norm(v - vold) / LA.norm(u0[1:n+1])
        if c < tol:
            break
        vold = v.copy()
    print ' '
    print 'iterations = %d' % itr
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


if __name__ == '__main__':
    gstestcase()

