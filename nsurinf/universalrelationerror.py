#!/usr/bin/python
#__author__ = 'philippe.landry@ligo.org'
#__date__ = '07-2019'

import numpy as np
from nsstruc.constants import *
from nsurinf.universalrelationfits import *
from numpy.random import normal

# IMPLEMENT GAUSSIAN SCATTER IN UNIVERSAL RELATIONS

def deltaILove(m,Lambda):

	errstd = ILove(m,Lambda)*0.0059/1.645	# max error from Carson+ PRD '19 "previous"

	return normal(0.,errstd)
	
def deltaRLove(m,Lambda):

	errstd = RLove(m,Lambda)*0.056/1.645	# max error from Carson+ PRD '19 "unconstrained"
	
	return normal(0.,errstd)
	
def deltaCLove(m,Lambda):

	errstd = CLove(m,Lambda)*0.065/1.645	# max error from Carson+ PRD '19 "previous"
	
	return normal(0.,errstd)
	
def deltaCanonBiLove(m,Lambda):

	errfit = 3.7152 - 5.2874*m + 1.8876*m**2
	errstd = CanonBiLove(m,Lambda)*errfit/1.645	# max error from Landry+Kumar PRD '19
	
	return normal(0.,errstd)
