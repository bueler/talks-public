import numpy as np
from numpy import linalg as LA
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from fem1d import minJ, contourgen

def convex2var(u,psi,center,name,**kwargs):
    '''Figure showing convex set K and solution in a 2-variable slice.'''
    assert len(u)==5
    assert len(psi)==5
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
    plt.plot(x[x>=psi[1]],level(x[x>=psi[1]],psi[2]),'g',lw=4.0)
    plt.plot(level(y[y>=psi[2]],psi[1]),y[y>=psi[2]],'r',lw=4.0)
    plt.text(psi[1]-0.02,-0.1,r'$\psi_1$',fontsize=20,color='r')
    plt.plot([psi[1],psi[1]],[-0.02,0.02],'k')
    plt.text(-0.1,psi[2],r'$\psi_2$',fontsize=20,color='g')
    plt.plot([-0.02,0.02],[psi[2],psi[2]],'k')
    ## contour lines dashed black on circles around (0.5,-0.1)
    theta = np.linspace(0.0,2.0*np.pi,1501)
    dx = kwargs.get('dx',0.25)
    f0 = kwargs.get('f0',0.0)
    CC = minJ(dx,f0,u[3]) + [0.0, 0.05, 0.1, 0.2, 0.5, 1.0, 1.5, 2.0, 3.0]
    for j in range(len(CC)):
         x,y = contourgen(dx,f0,CC[j],u[3],theta)
         ins = (x > psi[1]) & (y > psi[2]) & (x < 1.2) & (y < 1.2)
         plt.plot(x[ins],y[ins],'k.',markersize=2)
    # label big ideas: convex set K, solution location, unconstrained minimizer
    plt.text(1.0,1.0,r'$\mathcal{K}$',fontsize=28)
    plt.plot(u[1],u[2],'ko',markersize=14)
    plt.text(u[1]-0.1,u[2]+0.1,'solution',fontsize=24)
    if LA.norm([u[1]-center[0],u[2]-center[1]]) > 0.01:
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
    yy = np.linspace(-0.2,1.2,101)
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
    plt.text(0.1,max(u),r'$u$',fontsize=20)
    plt.axis([min(x)-0.2,max(x)+0.2,-0.2,0.9])
    plt.axis('off')
    if name != None:
        plt.savefig(name)

def constraints3D(u,psi,myfig,name):
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
    if name != None:
        plt.savefig(name)

