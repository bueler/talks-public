import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
    x = np.linspace(-0.2,1.2,141)
    y = x.copy()
    plt.plot(x,getzero(x),'k')
    plt.plot(getzero(y),y,'k')
    plt.text(1.22,0.0,r'$u_1$',fontsize=20)
    plt.text(-0.02,1.24,r'$u_2$',fontsize=20)
    # constraints in color
    plt.plot(x[x>=psi[0]],level(x[x>=psi[0]],psi[1]),'g',lw=4.0)
    plt.plot(level(y[y>=psi[1]],psi[0]),y[y>=psi[1]],'r',lw=4.0)
    plt.text(psi[0]-0.02,-0.1,r'$\psi_1$',fontsize=20,color='r')
    plt.plot([psi[0],psi[0]],[-0.02,0.02],'k')
    plt.text(-0.1,psi[1],r'$\psi_2$',fontsize=20,color='g')
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
    plt.plot(x[1:4],u[1:4],'ko',markersize=9)
    plt.text(0.1,0.15,r'$u$',fontsize=20)
    plt.axis('off')
    if name != None:
        plt.savefig(name)

def constraints3D(u,psi,myfig):
    assert len(u)==5
    assert len(psi)==5
    ax = myfig.gca(projection='3d')
    def linetoplane(j,x,y,z,c):
        if u[j]-psi[j]>0.05:
             ax.plot(np.array(x),np.array(y),np.array(z),'%c-' % c,lw=2.0,alpha=0.8)
    linetoplane(1, [psi[1],u[1]-0.03], [u[2],u[2]],        [u[3],u[3]],        'r')
    linetoplane(2, [u[1],u[1]],        [psi[2],u[2]-0.03], [u[3],u[3]],        'g')
    linetoplane(2, [u[1],u[1]],        [u[2],u[2]],        [psi[3],u[3]-0.03], 'b')
    ax.plot(u[1:2],u[2:3],u[3:4],'ko',markersize=12)
    A = np.array([[1.0, 1.0], [1.0, 1.0]])
    B = np.array([[0.0, 1.0], [0.0, 1.0]])
    C = np.array([[0.0, 0.0], [1.0, 1.0]])
    def scsh(P,t):  # scale and shift
        return (1.0-t)*P+t
    alf = 0.6
    ax.plot_surface(psi[1]*A,scsh(B,psi[2]),scsh(C,psi[3]),color='r',alpha=alf)
    ax.set_xticks((psi[1],))
    ax.set_xticklabels((r'$\psi_1$',), color='r', fontsize=16)
    ax.plot_surface(scsh(C,psi[1]),psi[2]*A,scsh(B,psi[3]),color='g',alpha=alf)
    ax.set_yticks((psi[2],))
    ax.set_yticklabels((r'$\psi_2$',), color='g', fontsize=16)
    ax.plot_surface(scsh(B,psi[1]),scsh(C,psi[2]),psi[3]*A,color='b',alpha=alf)
    ax.set_zticks((psi[3],))
    ax.set_zticklabels((r'$\psi_3$',), color='b', fontsize=16)
    ax.view_init(azim=50.0, elev=27.0)
    ax.set_xlim3d(0.0,1.0)
    ax.set_ylim3d(0.0,1.0)
    ax.set_zlim3d(0.0,1.0)
    #ax.set_xlabel(r'$u_1$', fontsize=16)
    #ax.set_ylabel(r'$u_2$', fontsize=16)
    #ax.set_zlabel(r'$u_3$', fontsize=16)

if __name__ == '__main__':
    x = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
    psi = np.array([-0.2,0.1,0.2,0.3,-0.12])
    u = np.array([0.0, 0.2, 0.35, 0.4, 0.0])   # FIXME: this could come from FEM calculation
    fig1 = plt.figure()
    with plt.xkcd():
        convex2var(psi[1:3],u[1:3], [0.5,-0.1], None)
    fig2 = plt.figure()
    oneD(x,psi,u,None)
    fig3 = plt.figure()
    constraints3D(u,psi,fig3)
    plt.show()

