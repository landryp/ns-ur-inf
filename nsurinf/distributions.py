#!/usr/bin/python
#__author__ = 'philippe.landry@ligo.org'
#__date__ = '07-2019'

import numpy as np
from numpy.random import normal
from numpy.random import choice
from scipy.special import gamma
from scipy.stats import gaussian_kde

# DEFINE ALL MANNER OF GAUSSIAN DISTRIBUTIONS

def posnormal(med,std,num=1): # strictly positive Gaussian

	vals = []
	for i in range(num):
		val = -1
		while val <= 0:
			val = normal(med,std)
		vals.append(val)

	return vals

def nonnegnormal(med,std,num=1): # non-negative Gaussian 

	vals = []
	for i in range(num):
		val = -1
		while val < 0:
			val = normal(med,std)
		vals.append(val)

	return vals
	
def truncnormal(med,std,ub,num=1): # strictly positive Gaussian truncated at specified upper bound

	vals = []
	for i in range(num):
		val = -1
		while val <= 0 or val > ub:
			val = normal(med,std)
		vals.append(val)

	return vals
	
# DEFINE GENERALIZED BETA PRIME DISTRIBUTION

def genbetaprime_pdf(p,q,a,b,x):

	return (1.+(x/b)**a)**(-p-q)*(x/b)**(a*p-1.)*a*gamma(p+q)/(b*gamma(p)*gamma(q))

def genbetaprime(p,q,a,b,num=1):

	grid = np.arange(0.,1e5,1.)
	gridprobs = genbetaprime_pdf(p,q,a,b,grid)
	norm = sum(gridprobs)
	gridprobs = gridprobs/norm

	vals = []
	for i in range(num):
		val = choice(grid,size=1,p=gridprobs)
		vals.append(val[0])

	return vals

# GET DISTRIBUTION FROM SAMPLES

def samplesdistr(xdat,num=1):

	kde = gaussian_kde(xdat)
	grid = np.linspace(min(xdat),max(xdat),1e5)
	gridprobs = kde(grid)
	norm = sum(gridprobs)
	gridprobs = gridprobs/norm
	
	vals = []
	for i in range(num):
		val = choice(grid,size=1,p=gridprobs)
		vals.append(val[0])
		
	return vals
