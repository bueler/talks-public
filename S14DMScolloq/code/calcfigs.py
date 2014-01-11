import numpy as np
from matplotlib import pyplot as plt
from matplotlib import mlab

def prepaxes(num,**kwargs):
    def getzero(x):
        return np.zeros(np.shape(x))
    fig = plt.figure(num)
    xx = np.linspace(-1.0,5.0,7)
    yy = np.linspace(-1.0,5.0,7)
    plt.plot(xx,getzero(xx),'k')
    plt.plot(getzero(yy),yy,'k')
    plt.text(5.5,-0.1,r'$x$',fontsize=20)
    plt.text(-0.1,5.5,r'$y$',fontsize=20)
    plt.axis([-0.5,5.5,-1.5,5.5])
    plt.axis('off')
    a = kwargs.get('a',None)
    if a != None:
        plt.plot([a,a],[-0.1,0.1],'k')
        plt.text(a-0.1,-0.5,r'$a$',fontsize=20)
    b = kwargs.get('b',None)
    if b != None:
        plt.plot([b,b],[-0.1,0.1],'k')
        plt.text(b-0.1,-0.5,r'$b$',fontsize=20)
    return fig

def calcprob(root):
    # figure with no [a,b] and no soln
    prepaxes(1)
    x = np.linspace(-0.4,5.0,301)
    f = - 0.7*x + 4.0 + 1.3*np.cos(x)**3
    plt.plot(x,f)
    plt.text(2.0,3.0,r'$f$',fontsize=20)
    if root != None:
        plt.savefig(root + 'bare.png')
    # figure with closed interval and soln
    a = 1.5
    b = 4.5
    f = f[(x<=b)&(x>=a)]
    x = x[(x<=b)&(x>=a)]
    prepaxes(2,a=a,b=b)
    plt.plot(x,f)
    plt.text(2.0,3.0,r'$f$',fontsize=20)
    ic = mlab.find(f==min(f))[0]
    u = x[ic]
    fu = f[ic]
    plt.plot(u,fu,'k.',markersize=18)
    plt.plot([u,u],[-0.15,0.15],'k')
    plt.text(u-0.1,-0.7,r'$u$',fontsize=24)
    if root != None:
        plt.savefig(root + 'soln.png')
    # figure with closed interval and soln and tangent line
    prepaxes(3,a=a,b=b)
    plt.plot(x,f)
    plt.text(2.0,3.0,r'$f$',fontsize=20)
    plt.plot(u,fu,'k.',markersize=18)
    plt.plot([u,u],[-0.15,0.15],'k')
    plt.text(u-0.1,-0.7,r'$u$',fontsize=24)
    plt.plot([u-0.6,u+0.6],[fu,fu],'k--',linewidth=2.5)
    if root != None:
        plt.savefig(root + 'soln_interior.png')
    # figure with closed interval and soln and tangent line (at endpoint)
    prepaxes(4,a=a,b=b)
    x = np.linspace(a,b,301)
    f = - 0.7*x + 4.0 - 1.2*np.cos(x)
    plt.plot(x,f)
    plt.text(2.0,3.5,r'$f$',fontsize=20)
    plt.plot(b,f[-1],'k.',markersize=18)
    plt.plot([b,b],[-0.15,0.15],'k')
    plt.text(b-0.2,-1.0,r'$=u$',fontsize=24)
    t = np.linspace(b-0.8,b,2)
    fb = f[-1]
    dfb = -0.7 + 1.2 * np.sin(b)
    plt.plot(t,fb+dfb*(t-b),'k--',linewidth=3.5)
    if root != None:
        plt.savefig(root + 'soln_endpoint.png')
    # show if not saved
    if root == None:
        plt.show()


if __name__ == '__main__':
    with plt.xkcd():
        calcprob('calcprob_')
