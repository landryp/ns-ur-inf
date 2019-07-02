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

def ILove(m,Lambda): # I in terms of Ibar-Love fit

	return IIbar(m,IbarLove_noerr(m,Lambda)+deltaIbarLove(m,Lambda))
	
def CLove(m,Lambda): # C-Love fit

	return CLove_noerr(m,Lambda)+deltaCLove(m,Lambda)
	
def RLove(m,Lambda): # R in terms of C-Love fit

	return RC(m,CLove(m,Lambda))
	
def chiLove(m,Lambda,Omega): # chi in terms of Ibar-Love fit

	return chiI(m,ILove(m,Lambda),Omega)
	
def CanonBiLove(m,Lambda): # Canonical binary Love fit

	return CanonBiLove_noerr(m,Lambda)+deltaCanonBiLove(m,Lambda)
