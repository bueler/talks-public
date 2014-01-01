import numpy as np
import matplotlib.pyplot as plt

def convex2var(psi,u,center,name):
    '''Figure showing convex set K and solution in a 2-variable slice.'''
    assert len(psi)==2
    assert len(u)==2
    assert len(center)==2
    def getzero(x):
        return np.zeros(np.shape(x))
    def level(x,lev):
        return lev * np.ones(np.shape(x))
    # axes in black
    plt.xkcd()
    x = np.linspace(-0.2,1.2,141)
    y = x.copy()
    plt.plot(x,getzero(x),'k')
    plt.plot(getzero(y),y,'k')
    plt.text(1.22,0.0,r'$u_1$',fontsize=20)
    plt.text(-0.02,1.24,r'$u_2$',fontsize=20)
    # constraints in color
    plt.plot(x[x>=psi[0]],level(x[x>=psi[0]],psi[1]),'g',lw=4.0)
    plt.plot(level(y[y>=psi[1]],psi[0]),y[y>=psi[1]],'r',lw=4.0)
    plt.text(psi[0]-0.02,-0.1,r'$\psi_1$',fontsize=20)
    plt.plot([psi[0],psi[0]],[-0.02,0.02],'k')
    plt.text(-0.1,psi[1],r'$\psi_2$',fontsize=20)
    plt.plot([-0.02,0.02],[psi[1],psi[1]],'k')
    # contour lines dashed black on circles around (0.5,-0.1)
    theta = np.linspace(0.0,2.0*np.pi,201)
    for r in [0.35, 0.4, 0.45, 0.5, 0.6, 0.7, 0.85, 1.0, 1.15]:
        cx = center[0] + r * np.cos(theta)
        cy = center[1] + r * np.sin(theta)
        ins = (cx >= psi[0]) & (cy >= psi[1]) & (cx < 1.2)
        plt.plot(cx[ins], cy[ins],'k--')
    # label big ideas: convex set K, solution location, unconstrained minimizer
    plt.text(1.0,1.0,r'$\mathcal{K}$',fontsize=28)
    plt.plot(center[0],psi[1],'ko',markersize=14)
    plt.text(center[0]-0.1,psi[1]+0.1,'solution',fontsize=24)
    plt.plot(center[0],center[1],'ko',markersize=9)
    plt.text(center[0]-0.1,center[1]-0.1,'unconstrained',fontsize=20)
    plt.text(center[0]-0.05,center[1]-0.2,'minimizer',fontsize=20)
    plt.axis('off')
    if name != None:
        plt.savefig(name)

def oneD(x,psi,u,name):
    assert len(x)==5
    assert len(psi)==5
    assert len(u)==5
    # axes in black
    def getzero(x):
        return np.zeros(np.shape(x))
    xx = np.linspace(min(x)-0.2,max(x)+0.2,141)
    yy = np.linspace(min(psi)-0.1,max(u)+0.1,101)
    plt.plot(xx,getzero(xx),'k')
    plt.plot(getzero(yy),yy,'k')
    plt.text(1.22,-0.01,r'$x$',fontsize=20)
    dy = [0.02, 0.015, 0.015, 0.015, 0.02]
    for j in range(len(x)):
        plt.plot([x[j],x[j]],[-dy[j],dy[j]],'k')
        if j==0:
            plt.text(x[j]-0.05,-0.05,r'$0$',fontsize=16)
        elif j==4:
            plt.text(x[j]+0.02,-0.05,r'$L$',fontsize=14)
        else:
            plt.text(x[j]-0.02,-0.05,(r'$x_%d$' % j),fontsize=20)
    # values of constraints as colored dots
    plt.plot(x,psi,'k')
    plt.plot(x[1],psi[1],'ro',markersize=14)
    plt.plot(x[2],psi[2],'go',markersize=14)
    plt.plot(x[3],psi[3],'bo',markersize=14)
    plt.text(0.9,-0.1,r'$\psi$',fontsize=20)
    # solution as stronger black
    plt.plot(x,u,'k',lw=4.0)
    plt.text(0.1,0.15,r'$u$',fontsize=20)
    plt.axis('off')
    if name != None:
        plt.savefig(name)
    
if __name__ == '__main__':
    fig1 = plt.figure()
    #convex2var([0.1,0.3], [0.4,0.3], [0.5,-0.1], 'convexvar.png')
    convex2var([0.1,0.3], [0.4,0.3], [0.5,-0.1], None)
    fig2 = plt.figure()
    psi = np.array([-0.2,0.1,0.2,0.3,-0.12])
    x = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
    u = np.array([0.0, 0.2, 0.35, 0.4, 0.0])   # FIXME: this could come from FEM calculation
    #oneD(x,psi,u,'oned-basecase.png')
    oneD(x,psi,u,None)
    plt.show()

