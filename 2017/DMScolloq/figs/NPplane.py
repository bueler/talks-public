#!/usr/bin/env python

# consider N-P plane:
#     N = number of unknowns
#     P = number of processors
# various directions to infinity in this plane correspond to optimality,
# static scaling, weak scaling, and strong scaling

import numpy as np
import matplotlib.pyplot as plt
import sys

dash = 0.06
filenames = ['NPplane.pdf','NPplaneweakstrong.pdf']

SHOW = False
def writeout(outname):
    if SHOW:
        plt.show()
    else:
        print('writing file ' + outname)
        plt.savefig(outname,bbox_inches='tight')

for j in range(2):
    plt.figure(figsize=(7,6))
    ax = plt.gca()

    ax.arrow(-0.7, 0.0, 7.7, 0.0, head_width=0.07, head_length=0.15, fc='k', ec='k')
    plt.text(4.0,-1.0,'$P$ = number of processors',fontsize=12.0)

    ax.arrow(0.0, -1.0, 0.0, 7.0, head_width=0.07, head_length=0.15, fc='k', ec='k')
    plt.text(-0.9,6.0,'$N$ = degrees of freedom',fontsize=12.0,rotation=90.0)

    plt.plot([1.0, 1.0],[-dash,dash],'k')
    plt.text(0.7,-0.4,'$P$=1',fontsize=12.0)
    plt.text(0.6,-0.7,'(serial)',fontsize=12.0)

    ax.arrow(1.0, 0.5, 0.0, 5.0, head_width=0.15, head_length=0.2, fc='w', ec='k')
    plt.text(0.65,2.5,'optimality',fontsize=12.0,rotation=90.0)

    plt.plot([5.0, 5.0],[-dash,dash],'k')
    ax.arrow(5.0, 0.5, 0.0, 5.0, head_width=0.15, head_length=0.2, fc='w', ec='k')
    plt.text(4.7,2.8,'static scaling',fontsize=12.0,rotation=90.0)
    plt.text(4.9,-0.5,'$\hat P$',fontsize=12.0)

    if j == 1:
        ax.arrow(1.5, 1.5, 4.3, 4.3, head_width=0.15, head_length=0.2, fc='w', ec='k')
        plt.text(1.5,3.4,'weak scaling (slope=1)',fontsize=12.0,rotation=44.0)

        plt.plot([-dash,dash],[4.0,4.0],'k')
        ax.arrow(1.3, 4.0, 5.5, 0.0, head_width=0.15, head_length=0.2, fc='w', ec='k')
        plt.text(1.4,4.2,'strong scaling',fontsize=12.0)
        plt.text(-0.4,3.9,'$\hat N$',fontsize=12.0)

    plt.axis('off')
    plt.axis([-1.0, 8.0, -1.0, 7.0])
    writeout(filenames[j])

