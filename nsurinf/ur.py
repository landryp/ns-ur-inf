#!/usr/bin/python
#__author__ = 'philippe.landry@ligo.org'
#__date__ = '09-2019'

import numpy as np
from nsurinf.constants import *
from nsurinf.distributions import *

# DEFINE FIT TYPES

def logfit(consts,n,Lambda):

	terms = [consts[i]*np.log(Lambda)**i for i in range(n+1)]

	return np.sum(terms)
	
def log10bifit(consts,m,Lambda):

	terms = [np.sum([consts[i,j]*m**i*np.log10(Lambda)**j for j in range(2)]) for i in range(5)]

	return np.sum(terms)
	
def bifit(a,b,consts,n,q,Lambda):

	def F(n,q):
	
		return (1.-q**(10./(3.-n)))/(1.+q**(10./(3.-n)))

	numterms = [np.sum([b[i-1,j-1]*q**j*Lambda**(-i/5.) for j in range(1,3)]) for i in range(1,4)]
	denomterms = [np.sum([consts[i-1,j-1]*q**j*Lambda**(-i/5.) for j in range(1,3)]) for i in range(1,4)]

	return F(n,q)*Lambda*(a + np.sum(numterms))/(a + np.sum(denomterms))

# GIVE UNIVERSAL RELATION FITS AND ERRORS

def CLove_YY16(Lambda): # C-Love fit from Yagi+Yunes PhysRep '16 with max error from Carson+ PRD '19 "previous"

	consts = [0.360,-0.0355,0.000705]
	n = 2
	C = logfit(consts,n,Lambda)
	
	errstd = C*0.065/1.645
	deltaC = normal(0.,errstd)

	return C+deltaC

def IbarLove_YY16(Lambda): # Ibar-Love fit from Yagi+Yunes PhysRep '16 with max error from Carson+ PRD '19 "previous"

	consts = [1.496,0.05951,0.02238,-6.953e-4,8.345e-6]
	n = 4
	Ibar = np.exp(logfit(consts,n,Lambda))
	
	errstd = Ibar*0.0059/1.645
	deltaIbar = normal(0.,errstd)

	return Ibar+deltaIbar
	
def CanonBiLove_KL19(m,Lambda): # Canonical binary Love fit and max error from Kumar+Landry PRD '19

	consts = np.array([[-9.4469,4.6152],[3.9702e1,-1.2226e1],[-4.9173e1,1.4214e1],[2.4937e1,-7.1134],[-4.7288,1.3416]])
	newLambda = 10.**log10bifit(consts,m,Lambda)
	
	errfit = 3.7152 - 5.2874*m + 1.8876*m**2
	errstd = newLambda*errfit/1.645
	deltanewLambda = normal(0.,errstd)

	return newLambda+deltanewLambda

