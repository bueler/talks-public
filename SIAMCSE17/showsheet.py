#!/usr/bin/env python

import sys
def importfail(name):
    print "'import %s' failed" % name
    print "need link to petsc/bin/petsc-pythonscripts/%s.py?" % name
    sys.exit(99)

try:
    import PetscBinaryIO as pbio
except:
    importfail('PetscBinaryIO')
try:
    import petsc_conf
except:
    importfail('petsc_conf')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d

# FIXME argparse to get these values
L = 1800.0e3
mx = 96
fname = 'ice_96_100.dat'

mapshape = (mx,mx)
dx = L / mx
dy = dx
x = np.linspace(0.0,L-dx,mx)
y = x

try:
    fh = open(fname)
except:
    print "unable to open '%s' ... ending ..." % fname
    sys.exit(1)

io = pbio.PetscBinaryIO()
vecnames = ['b','H']
for name in vecnames:
    try:
        objecttype = io.readObjectType(fh)
    except pbio.DoneWithFile:
        print "no next Vec in '%s' ... ending ..." % fname
        sys.exit(2)
    if objecttype == 'Vec':
        if name == 'b':
            b = np.reshape(io.readVec(fh),mapshape)
        elif name == 'H':
            H = np.reshape(io.readVec(fh),mapshape)
        else:
            print "how did I get here?"
            sys.exit(3)
        print "  read Vec %s" % name
    else:
        print "unexpected objecttype '%s' ... ending ..." % objecttype
        sys.exit(4)
fh.close()

colors = np.empty(b.shape, dtype=str)
for yk in range(mx):
    for xk in range(mx):
        if H[xk,yk] > 1.0:        # rounding error gives 10^-15 size values
            colors[xk,yk] = 'w'   # FIXME 
        else:
            colors[xk,yk] = 'g'   # FIXME 

fig = plt.figure(figsize=(12,6))
ax = fig.gca(projection='3d')
xx, yy = np.meshgrid(x,y)
hand = ax.plot_surface(xx/1000.0,yy/1000.0,H+b,rstride=1,cstride=1,facecolors=colors)

#ax.set_zlim3d(0.0, max(b.flatten()))
#fig.colorbar(h,shrink=0.8,aspect=8)

ax.set_xlabel('x  (km)')
ax.set_ylabel('y  (km)')
plt.show()

