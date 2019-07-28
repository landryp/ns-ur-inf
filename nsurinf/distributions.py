#!/usr/bin/python
#__author__ = 'philippe.landry@ligo.org'
#__date__ = '07-2019'

import numpy as np
from numpy.random import uniform
from numpy.random import normal
from numpy.random import choice
from scipy.special import gamma
from scipy.stats import gaussian_kde

# DEFINE UNIFORM DISTRIBUTIONS

def unif(lb,ub,num=1): # uniform between lb and ub

	vals = []
	for i in range(num):
		val = uniform(lb,ub)
		vals.append(val)

	return vals
	
def unifm1m2(lb1,ub1,lb2,ub2,star,num=1): # uniform between lb and ub, but with m1 always greater than m2

	vals1 = []
	vals2 = []
	for i in range(num):
		val1 = -1
		val2 = 0
		while val1 < val2:
			val1 = uniform(lb1,ub1)
			val2 = uniform(lb2,ub2)
		
		vals1.append(val1)
		vals2.append(val2)

	if star == 1: return vals1
	elif star == 2: return vals2

def unifmcq(lbm,ubm,lbq,ubq,star,num=1): # uniform in mc and q between their lb and ub, but with m1 always greater than m2

	vals1 = []
	vals2 = []
	for i in range(num):
		val1 = -1
		val2 = 0
		while val1 < val2:
			mc = uniform(lbm,ubm)
			q = uniform(lbq,lbm)
			val1 = mc*(1.+q)**0.2/(q**0.6)
			val2 = q*val1
		
		vals1.append(val1)
		vals2.append(val2)

	if star == 1: return vals1
	elif star == 2: return vals2

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
