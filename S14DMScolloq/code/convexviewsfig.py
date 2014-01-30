import numpy as np
from matplotlib import pyplot as plt
from matplotlib import mlab

def convexview(linearcombination):
    # draw K
    plt.plot([1.0, 2.0, 20.0, 3.0, 1.0],[2.0, 4.0, 0.0, 1.0, 2.0],'b',lw=2.0)
    plt.fill([1.0, 2.0, 20.0, 3.0, 1.0],[2.0, 4.0, 0.0, 1.0, 2.0],
             facecolor='b', alpha=0.2, edgecolor='none')
    plt.text(3.5,1.2,r'$K$',fontsize=28,color='b')
    # draw axes
    plt.plot([0.5, 0.5],[-0.5, 4.5],'k',lw=1.0)
    plt.plot([0.0, 4.0],[0.5, 0.5],'k',lw=1.0)
    # plot u, v
    u = np.array([1.6,1.7])
    v = np.array([3.0,3.0])
    plt.plot(u[0],u[1],'.',markersize=14,color='k')
    plt.text(u[0]-0.3,u[1]-0.3,r'$u$',fontsize=24,color='k')
    plt.plot(v[0],v[1],'.',markersize=14,color='k')
    plt.text(v[0]+0.1,v[1]+0.1,r'$v$',fontsize=24,color='k')
    # show either interpretation
    eps = 0.6
    z = (1.0 - eps) * u + eps * v
    plt.plot(z[0],z[1],'.',markersize=14,color='k')
    if linearcombination:
        # lin-comb : (1 - eps) u + eps v
        plt.plot([u[0],v[0]], [u[1],v[1]],'k',lw=2.0)
        plt.text(z[0],z[1]-0.3,r'$(1-\varepsilon) u + \varepsilon v$',fontsize=24,color='k')
    else:
        # intoK : u + eps (v - u)
        ax = plt.axes()
        w = eps * (v - u)
        ax.arrow(u[0],u[1],w[0],w[1],
                 head_width=0.1, head_length=0.2, length_includes_head=True, fc='k', ec='k')
        plt.text(z[0],z[1]-0.3,r'$u + \varepsilon (v - u)$',fontsize=24,color='k')
    plt.axis([-1.0,4.0,0.0,5.0],'k',lw=2.0)
    plt.axis('off')

if __name__ == '__main__':
    #plt.xkcd()
    plt.figure(1)
    convexview(True)
    plt.savefig('convexview-lincomb.png')
    plt.figure(2)
    convexview(False)
    plt.savefig('convexview-intoK.png')
    #plt.show()

