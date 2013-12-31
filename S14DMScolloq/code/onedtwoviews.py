import numpy as np
import matplotlib.pyplot as plt

#plt.xkcd()

psi1 = 0.1
psi2 = 0.3
psi3 = 0.2

x = [0.0, 0.25, 0.5, 0.75, 1.0] 
u = [0.0, 0.2, 0.35, 0.2, 0.0]   # FIXME: this could come from FEM calculation
def getzero(x):
    return np.zeros(np.shape(x))

# axes in black
xx = np.linspace(-0.2,1.2,141)
yy = np.linspace(-0.1,0.5,141)
plt.plot(xx,getzero(xx),'k')
plt.plot(getzero(yy),yy,'k')
plt.text(1.22,-0.01,r'$x$',fontsize=20)
plt.plot([1.0,1.0],[-0.02,0.02],'k')
plt.text(1.02,-0.05,r'$L$',fontsize=14)
plt.plot([0.0,0.0],[-0.02,0.02],'k')
plt.text(-0.05,-0.05,r'$0$',fontsize=16)
for j in [1,2,3]:
  plt.plot([x[j],x[j]],[-0.015,0.015],'k')
  plt.text(x[j]-0.02,-0.05,(r'$x_%d$' % j),fontsize=20)
# values of constraints as colored dots
plt.plot(x,[-0.2, psi1, psi2, psi3, -0.12],'k')
plt.plot(x[1],psi1,'ro',markersize=14)
plt.plot(x[2],psi2,'go',markersize=14)
plt.plot(x[3],psi3,'bo',markersize=14)
plt.text(0.9,-0.1,r'$\psi$',fontsize=20)
# solution as stronger black
plt.plot(x,u,'k',lw=4.0)
plt.text(0.1,0.15,r'$u$',fontsize=20)
plt.axis('off')
#plt.show()
plt.savefig('oned-basecase.png')
