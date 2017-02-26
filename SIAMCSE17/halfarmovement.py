#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

import argparse
parser = argparse.ArgumentParser(description='compute margin movement from Halfar (1983) solution')
parser.add_argument('t', metavar='DURATION', type=float, default=10.0,
                    help='time (a) during which Halfar solution advances the margin')
args = parser.parse_args()

R0 = 750.0e3 # t=t0 radius of exact ice sheet (m)
H0 = 3600.0  # t=t0 center thickness of exact ice sheet (m)
n = 3.0
alpha = 1.0/9.0
beta = 1.0/18.0
q = 1.0 + 1.0 / n
m = n / (2.0*n + 1.0)

secpera = 31556926.0
g = 9.81        # m/s^2
rho = 910.0     # kg/m^3
A = 3.1689e-24  # 1/(Pa^3 s); EISMINT I value
Gamma = 2.0 * (rho * g)**n * A / (n + 2.0)

# see equation (9) in Bueler et al (2005); normally 422.45 a
t0 = (beta / Gamma) * (7.0/4.0)**3.0 * (R0**4.0 / H0**7.0)

tf = args.t * secpera
Rf = R0 * ((t0+tf) / t0)**beta

print 'in time interval [t0,t0+tf]=[%.3f,%.3f],' % (t0/secpera, (t0+tf)/secpera)
print 'the margin advances from %.3f km to %.3f km' % (R0/1000.0, Rf/1000.0)

