#!/usr/bin/python
#__author__ = 'philippe.landry@ligo.org'
#__date__ = '07-2019'

import numpy as np
from nsstruc.constants import *
from nsurinf.universalrelationfits import *
from numpy.random import normal

# IMPLEMENT GAUSSIAN SCATTER IN UNIVERSAL RELATIONS

def deltaIbarLove(m,Lambda):

	errstd = IbarLove_noerr(m,Lambda)*0.0059/1.645	# max error from Carson+ PRD '19 "previous"

	return normal(0.,errstd)
	
def deltaCLove(m,Lambda):

	errstd = CLove_noerr(m,Lambda)*0.065/1.645	# max error from Carson+ PRD '19 "previous"
	
	return normal(0.,errstd)
	
def deltaCanonBiLove(m,Lambda):

	errfit = 3.7152 - 5.2874*m + 1.8876*m**2
	errstd = CanonBiLove_noerr(m,Lambda)*errfit/1.645	# max error from Landry+Kumar PRD '19
	
	return normal(0.,errstd)
	
# GIVE EFFECTIVE UNIVERSAL RELATIONS, MARGINALIZING OVER UNCERTAINTY IN FITS

def ILove(m,Lambda,*args): # I in terms of Ibar-Love fit

	return IIbar(m,IbarLove_noerr(m,Lambda)+deltaIbarLove(m,Lambda))
	
def CLove(m,Lambda,*args): # C-Love fit

	return CLove_noerr(m,Lambda)+deltaCLove(m,Lambda)
	
def RLove(m,Lambda,*args): # R in terms of C-Love fit

	return RC(m,CLove(m,Lambda))
	
def chiLove(m,Lambda,Omega,*args): # chi in terms of Ibar-Love fit

	return chiI(m,ILove(m,Lambda),Omega)
	
def CanonBiLove(m,Lambda,*args): # Canonical binary Love fit

	return CanonBiLove_noerr(m,Lambda)+deltaCanonBiLove(m,Lambda)
	
def OmegaLove(m,Lambda,chi,*args): # Omega in terms of Ibar-Love fit

	return OmegaI(m,ILove(m,Lambda),chi)

def ILove14(m,Lambda14,*args): # I in terms of Ibar-Love fit

	return IIbar(m,IbarLove_noerr(m,CanonBiLove(m,Lambda14))+deltaIbarLove(m,CanonBiLove(m,Lambda14)))
	
def CLove14(m,Lambda14,*args): # C-Love fit

	return CLove_noerr(m,CanonBiLove(m,Lambda14))+deltaCLove(m,CanonBiLove(m,Lambda14))
	
def RLove14(m,Lambda14,*args): # R in terms of C-Love fit

	return RC(m,CLove(m,CanonBiLove(m,Lambda14)))
	
def chiLove14(m,Lambda14,Omega,*args): # chi in terms of Ibar-Love fit

	return chiI(m,ILove(m,CanonBiLove(m,Lambda14)),Omega)
	
def OmegaLove14(m,Lambda14,chi,*args): # Omega in terms of Ibar-Love fit

	return OmegaI(m,ILove(m,CanonBiLove(m,Lambda14)),chi)
	
def Omega12Love14(Lambda14,m1,m2,chi1,chi2,*args): # Omega1,2 in terms of Ibar-Love fit

	return [OmegaI(m1,ILove(m1,CanonBiLove(m1,Lambda14)),chi1), OmegaI(m2,ILove(m2,CanonBiLove(m2,Lambda14)),chi2)]
	
def I12Love14(Lambda14,m1,m2,*args): # I1,2 in terms of Ibar-Love fit

	return [IIbar(m1,IbarLove_noerr(m1,CanonBiLove(m1,Lambda14))+deltaIbarLove(m1,CanonBiLove(m1,Lambda14))), IIbar(m2,IbarLove_noerr(m2,CanonBiLove(m2,Lambda14))+deltaIbarLove(m2,CanonBiLove(m2,Lambda14)))]
