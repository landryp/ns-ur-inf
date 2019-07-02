#!/usr/bin/python
#__author__ = 'philippe.landry@ligo.org'
#__date__ = '07-2019'

import numpy as np
from nsstruc.constants import *

# DEFINE FIT TYPES

def logfit(consts,n,Lambda):

	terms = [consts[i]*np.log(Lambda)**i for i in range(n+1)]

	return np.sum(terms)
	
def log10bifit(consts,m,Lambda):

	terms = [np.sum([consts[i,j]*m**i*np.log10(Lambda)**j for j in range(2)]) for i in range(5)]

	return np.sum(terms)
	
def F(n,q):
	
	return (1.-q**(10./(3.-n)))/(1.+q**(10./(3.-n)))
	
def bifit(a,b,consts,n,q,Lambda):

	numterms = [np.sum([b[i-1,j-1]*q**j*Lambda**(-i/5.) for j in range(1,3)]) for i in range(1,4)]
	denomterms = [np.sum([consts[i-1,j-1]*q**j*Lambda**(-i/5.) for j in range(1,3)]) for i in range(1,4)]

	return F(n,q)*Lambda*(a + np.sum(numterms))/(a + np.sum(denomterms))

# GIVE UNIVERSAL RELATION FITS

def IbarLove(m,Lambda): # Ibar-Love fit from Yagi+Yunes PhysRep '16

	consts = [1.496,0.05951,0.02238,-6.953e-4,8.345e-6]
	n = 4

	return np.exp(logfit(consts,n,Lambda))
	
def CLove(m,Lambda): # C-Love fit from Yagi+Yunes PhysRep '16

	consts = [0.360,-0.0355,0.000705]
	n = 2

	return logfit(consts,n,Lambda)
	
def BinaryLove(q,LambdaS): # Binary Love fit from Yagi+Yunes CQG '16

	a = 0.07550
	b = np.array([[-2.235,0.8474],[10.45,-3.251],[-15.70,13.61]])
	consts = np.array([[-2.048,0.5976],[7.941,0.5658],[-7.360,-1.320]])
	n = 0.743

	return bifit(a,b,consts,n,q,LambdaS)
	
def CanonBiLove(m,Lambda): # Canonical binary Love fit from Kumar+Landry PRD '19

	consts = np.array([[-9.4469,4.6152],[3.9702e1,-1.2226e1],[-4.9173e1,1.4214e1],[2.4937e1,-7.1134],[-4.7288,1.3416]])

	return 10.**log10bifit(consts,m,Lambda)

# DEFINE DERIVED QUANTITIES

def IIbar(m,Ibar): # I in terms of Ibar

	return 1e-45*G**2*Ibar*m**3*Msun**3/c**4

def RC(m,C): # R in terms of C

	R = 1e-5*G*m*Msun/(c**2*C)

	return R
	
# GIVE EFFECTIVE FITS FOR DERIVED QUANTITIES

def ILove(m,Lambda): # I in terms of Ibar-Love fit

	return IIbar(m,IbarLove(m,Lambda))
	
def RLove(m,Lambda): # R in terms of C-Love fit

	return RC(m,CLove(m,Lambda))

