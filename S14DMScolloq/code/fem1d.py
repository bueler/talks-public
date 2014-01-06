import numpy as np
from numpy import linalg as LA

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

def solvefem(dx,f0,psi,tol):
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

def minJ(dx,f0,v3):
    '''For the same functional J[v] as referred-to in solvefem(), compute the
    unconstrained minimum in the case where v3 is fixed:
       min J[x,y,v3]
    '''
    ee = f0 * dx**2
    ff = ee + v3
    gg = (4.0/3.0) * (0.5 * ee + ff)
    C = (v3**2 - f0 * dx**2 * v3 - 0.25 * ee**2 - (3.0/16.0) * gg**2) / dx
    return C

def contourgen(dx,f0,C,v3,theta):
    '''For the same functional J[v] as referred-to in solvefem(), compute the
    x=v1, y=v2 coordinates along the contour
       J[v] = C,
    but with v3 fixed, i.e.
       J[x,y,v3] = C.
    This contour is an ellipse.  Input theta should be values in [0,2 pi].
    Returns x,y.'''
    ee = f0 * dx**2
    dd = dx * C - v3**2 + ee * v3
    ff = ee + v3
    gg = (4.0/3.0) * (0.5 * ee + ff)
    ss = dd + 0.25 * ee**2 + (3.0/16.0) * gg**2
    if ss >= 0.0:
        hh = np.sqrt(ss)
    else:
        hh = 0.0
    y = (2.0/np.sqrt(3.0)) * hh * np.sin(theta) + 0.5 * gg
    x = hh * np.cos(theta) + 0.5 * ee + 0.5 * y
    return x,y

if __name__ == '__main__':
    gstestcase()

