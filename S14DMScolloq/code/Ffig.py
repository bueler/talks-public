import numpy as np
from matplotlib import pyplot as plt
from matplotlib import mlab

def Ffig(x,Fx,z,Piz,**kwargs):
    fig = plt.figure(1)
    # draw and label K
    plt.plot([1.0, 2.0, 4.0, 3.0, 1.0],[2.0, 4.0, 4.0, 1.0, 2.0],'b',lw=2.0)
    plt.fill([1.0, 2.0, 4.0, 3.0, 1.0],[2.0, 4.0, 4.0, 1.0, 2.0],
             facecolor='b', alpha=0.2, edgecolor='none')
    plt.text(3.2,3.5,r'$K$',fontsize=28,color='b')
    plt.axis([-2.0,5.0,-1.0,5.0],'k',lw=2.0)
    # draw axes
    plt.plot([0.0, 0.0],[-0.5, 4.5],'k',lw=2.0)
    plt.plot([-1.5, 4.0],[0.0, 0.0],'k',lw=2.0)
    # plot and label points
    plt.plot(x[0],x[1],'.',markersize=12,color='k')
    plt.text(x[0]+0.1,x[1]+0.1,r'$x$',fontsize=24,color='k')
    plt.plot(Fx[0],Fx[1],'.',markersize=12,color='k')
    plt.text(Fx[0]+0.1,Fx[1]+0.1,r'$F(x)$',fontsize=24,color='k')
    plt.plot(z[0],z[1],'.',markersize=12,color='k')
    plt.text(z[0]-0.2,z[1]+0.1,r'$z$',fontsize=24,color='k')
    plt.plot(Piz[0],Piz[1],'.',markersize=12,color='k')
    plt.text(Piz[0]+0.1,Piz[1]-0.05,r'$\Pi z$',fontsize=24,color='k')
    # arrows
    ax = plt.axes()
    ax.arrow(0.0,0.0,z[0],z[1],
             head_width=0.1, head_length=0.2, length_includes_head=True, fc='k', ec='k')
    ax.arrow(Fx[0],Fx[1],x[0]-Fx[0],x[1]-Fx[1],
             head_width=0.1, head_length=0.2, length_includes_head=True, fc='k', ec='k')

    plt.axis('off')
    return fig

if __name__ == '__main__':
    #plt.xkcd()
    x = np.array([2.0,3.0])
    Fx = np.array([1.5,0.5])
    Ffig(x,Fx,x-Fx,[1.06,2.10])
    plt.savefig('Fx-map-on-K.png')
    #plt.show()

