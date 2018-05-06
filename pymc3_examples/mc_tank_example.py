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

__author__ = "Eugene J. Ragasa"
__copyright__ = "Copyright 2018, Eugene J. Ragasa"
__credits__ = "Eugene J. Ragasa"
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Eugene J. Ragasa"
__email__ = "eugene.ragasa@gmail.com"

observed = np.array([7,275,182,86])
n_samples = 10000
m = max(observed)

model = pm.Model()
with model:
    # define the prior distribution
    N = pm.Uniform('N',m,10000)

    # calculation of the likelihood
    L = pm.Uniform('Likelihood', 0, N, observed=observed)

with model:
    step = pm.Metropolis()
    start ={'N' : m}
    samples = pm.sample(
        n_samples,
        step,
        start,
        cores=1)

pm.traceplot(samples[-2000::2])
plt.show()
print(np.median(samples[-2000::2]['N']))
print(sum(samples[-2000::2]['N'] <= 400)/len(samples[-2000::2]['N'])
)
