import numpy as np
from matplotlib import pyplot as plt
from matplotlib import mlab

def convexproj(x,y,xstr,ystr,num,**kwargs):
    fig = plt.figure(num)
    plt.plot([1.0, 2.0, 20.0, 3.0, 1.0],[2.0, 4.0, 0.0, 1.0, 2.0],'b',lw=2.0)
    plt.fill([1.0, 2.0, 20.0, 3.0, 1.0],[2.0, 4.0, 0.0, 1.0, 2.0],
             facecolor='b', alpha=0.2, edgecolor='none')
    plt.text(3.2,2.5,r'$K$',fontsize=28,color='b')
    plt.plot([x[0],x[1]], [y[0],y[1]], 'k.', markersize=18)
    plt.text(x[0]-0.1,y[0]+0.2,xstr,fontsize=22,color='k')
    plt.text(x[1]-0.1,y[1]+0.3,ystr,fontsize=22,color='k')
    eta = kwargs.get('eta',None)
    if eta != None:
        ax = plt.axes()
        ax.arrow(x[0], y[0], x[1]-x[0], y[1]-y[0],
                 head_width=0.1, head_length=0.2, length_includes_head=True, fc='k', ec='k')
        plt.plot([eta[0],], [eta[1],], 'k.', markersize=18)
        plt.text(eta[0]+0.1,eta[1]+0.1,r"$\eta$",fontsize=22,color='k')
        # FIXME: add arrow to eta
    plt.axis([-1.5,4.0,0.0,5.0],'k',lw=2.0)
    plt.axis('off')
    return fig

if __name__ == '__main__':
    #plt.xkcd()
    convexproj([-1.0,1.0],[2.4,2.0],r"$x$",r"$y$",1)
    plt.savefig('proj_xy.png')
    convexproj([0.4,1.5],[3.7,3.0],r"$x'$",r"$y'$",2)
    plt.savefig('proj_xyprime.png')
    convexproj([-1.0,1.0],[2.4,2.0],r"$x$",r"$y$",3,eta=[2.0,3.5])
    plt.savefig('proj_xy_vect.png')
    #plt.show()

