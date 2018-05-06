#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" An Simple Example for Tank MC

Adapted from an example from
Scott Rome, http://srome.github.io/Dont-Solve-Simulate-Markov-Chain-Monte-Carlo-Methods-with-PyMC3/

"""

import os
os.environ['MKL_THREADING_LAYER']='GNU'

import numpy as np
import pymc3 as pm
import matplotlib.pyplot as plt

size = 200
a = 1.
b = 2.
x = np.linspace(0,1,size)
y_sigma = 0.1
line = a + b*x

line_noise = line + np.random.normal(
    scale=y_sigma,
    size=size)

model = pm.Model()

#define prior_0_parameters
with model:
    y_hat_sigma = pm.HalfCauchy('sigma',beta=10,testval=1.)
    a_hat = pm.Normal('Intercept',0,sd=20)
    b_hat = pm.Normal('x',0,sd=20)

with model:
    # Define Likelihood
    likelihood = pm.Normal(
        'y',
        mu=a_hat+b_hat*x,
        sd=y_hat_sigma,
        observed=line_noise)

    # inference
    trace = pm.sample(
        progressbar=False,
        tune=1000,
        #njobs=4,
        cores=1)

#plt.figure(figsize=(7, 7))
pm.traceplot(trace)
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 7))
plt.plot(x, line_noise, 'x', label='data')
pm.plots.plot_posterior_predictive_glm(
    trace,
    samples=100,
    label='posterior predictive regression lines')
plt.plot(x, line, label='true regression line', lw=3., c='y')

plt.title('Posterior predictive regression lines')
plt.legend(loc=0)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
