#!/usr/bin/python
#__author__ = 'philippe.landry@ligo.org'
#__date__ = '09-2019'

import numpy as np
from nsurinf.constants import *

# LIKELIHOODS FOR INFERENCE OF I, CHI AND CHIEFF

def moi(m,Iofm):

	I = Iofm(m)*1e-45

	return I
	
def moicorr_B13(m,f,I):

	a = 0.19*(1e-3*f)**4 + 1.40
	b = -0.042*(1e-3*f)**4 + 0.19
	Cmin = 0.074*(1e-3*f)**2 + 0.005
	C = 0.2
	dI = 1e-45*(a*Cmin + b)*G**2*Msun**3*m**3/(c**4*C**2) - I

	return dI

def spin(f,m,I):

	chi = 2.*np.pi*f*c*I*1e45/(G*m**2*Msun**2)

	return chi
	
def effspin(chi1,m1,costheta1,chi2,m2,costheta2):

	chieff = (chi1*m1*Msun*costheta1 + chi2*m2*Msun*costheta2)/(m1*Msun+m2*Msun)
	
	return chieff
	
def radius(m,C):

	R = 1e-5*G*m*Msun/(C*c**2)

	return R

# LIKELIHOODS FOR CALCULATING I FROM UNIVERSAL RELATIONS

def dimmoi(m,Ibar):

	I = G**2*m**3*Msun**3*Ibar/c**4
	
	return I*1e-45
	
def moibar(Lambda,IbarofLambda):

	Ibar = IbarofLambda(Lambda)

	return Ibar
	
def tiddef(m,Lambda14,LambdaofmLambda14):

	Lambda = LambdaofmLambda14(m,Lambda14)

	return Lambda

