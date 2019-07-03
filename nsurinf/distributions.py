#!/usr/bin/python
#__author__ = 'philippe.landry@ligo.org'
#__date__ = '07-2019'

import numpy as np
from numpy.random import normal
from scipy.stats import betaprime

# DEFINE ALL MANNER OF GAUSSIAN DISTRIBUTIONS

def posnormal(med,std,num=1): # truncated strictly positive Gaussian

	vals = []
	for i in range(num):
		val = -1
		while val <= 0:
			val = normal(med,std)
		vals.append(val)

	return vals

def nonnegnormal(med,std,num=1): # truncated non-negative Gaussian 

	vals = []
	for i in range(num):
		val = -1
		while val < 0:
			val = normal(med,std)
		vals.append(val)

	return vals
	
# DEFINE GENERALIZED BETA PRIME DISTRIBUTION

def posgenbetaprime(a,b,q,num=1):

	vals = []
	for i in range(num):
		val = -1
		while val <= 0:
			val = betaprime.rvs(a,b)/q # NEED TO FIX THIS
		vals.append(val)

	return vals
