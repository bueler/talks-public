import numpy as np
import matplotlib.pyplot as plt

plt.xkcd()

def getzero(x):
    return np.zeros(np.shape(x))
def level(x,lev):
    return lev * np.ones(np.shape(x))

psi1 = 0.1
psi2 = 0.3

x = np.linspace(-0.2,1.2,141)
y = x.copy()
# axes in black
plt.plot(x,getzero(x),'k')
plt.plot(getzero(y),y,'k')
plt.text(1.22,0.0,r'$u_1$',fontsize=20)
plt.text(-0.02,1.24,r'$u_2$',fontsize=20)
# constraints in color
plt.plot(x[x>=psi1],level(x[x>=psi1],psi2),'g',lw=4.0)
plt.plot(level(y[y>=psi2],psi1),y[y>=psi2],'r',lw=4.0)
plt.text(psi1-0.02,-0.1,r'$\psi_1$',fontsize=20)
plt.plot([psi1,psi1],[-0.02,0.02],'k')
plt.text(-0.1,psi2,r'$\psi_2$',fontsize=20)
plt.plot([-0.02,0.02],[psi2,psi2],'k')
# contour lines dashed black on circles around (0.5,-0.1)
theta = np.linspace(0.0,2.0*np.pi,201)
for r in [0.35, 0.4, 0.45, 0.5, 0.6, 0.7, 0.85, 1.0, 1.15]:
    cx = 0.5 + r * np.cos(theta)
    cy = -0.1 + r * np.sin(theta)
    ins = (cx >= psi1) & (cy >= psi2) & (cx < 1.2)
    plt.plot(cx[ins], cy[ins],'k--')
# label big ideas: convex set K, solution location, unconstrained minimizer
plt.text(1.0,1.0,r'$\mathcal{K}$',fontsize=28)
plt.plot(0.5,psi2,'ko',markersize=14)
plt.text(0.4,psi2+0.1,'solution',fontsize=24)
plt.plot(0.5,-0.1,'ko',markersize=9)
plt.text(0.4,-0.20,'unconstrained',fontsize=20)
plt.text(0.45,-0.30,'minimizer',fontsize=20)
plt.axis('off')
#plt.show()
plt.savefig('convexvar.png')
