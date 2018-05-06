import numpy as np
import os
os.environ['MKL_THREADING_LAYER']='GNU'
import pymc3 as pm

from moo import MultiObjectiveOptimizationProblem
from moo import DesignVariable
from moo import ObjectiveFunction
from moo import ConstraintFunction
#BinhAndKohn

def func_f1(x1,x2):
    print('x1:',type(x1))
    print(x1)
    print('x2',type(x2))
    print(x1)
    return 4*x1**2+4*x2**2

def func_f2(x1,x2):
    return (x1-8)**2+(x2+3)**2-7.7

moo_problem = MultiObjectiveOptimizationProblem()
moo_problem.design_variables['x1'] = DesignVariable()
moo_problem.design_variables['x1'].min = 0
moo_problem.design_variables['x1'].max = 5
moo_problem.design_variables['x2'] = DesignVariable()
moo_problem.design_variables['x2'].min = 0
moo_problem.design_variables['x2'].max = 3
moo_problem.objective_functions['f1'] = ObjectiveFunction()
moo_problem.objective_functions['f1'].variables = ['x1','x2']
moo_problem.objective_functions['f1'].function_string = '4*x1**2+4*x2**2'
moo_problem.objective_functions['f2'] = ObjectiveFunction()
moo_problem.objective_functions['f2'].variables = ['x1','x2']
moo_problem.objective_functions['f2'].function_string = '(x1-5)**2+(x2-5)**2'
moo_problem.constraint_functions['g1'] = ConstraintFunction()
moo_problem.constraint_functions['g1'] = '-(x1-5)**2-x2**2+25.0'
moo_problem.constraint_functions['g2'] = ConstraintFunction()
moo_problem.constraint_functions['g2'] = '(x1-8)**2+(x2+3)**2-7.7'

import networkx as nx
import theano
import theano.tensor as tt

class QoiFromTheta(tt.Op):
    itypes = [tt.dscalar]
    otypes = [tt.dscalar]

def get_parent_pymc3_obj(bn,node,num=0):
    return bn.node[BN.predecessors(node)[num]]['pymc3_obj']

def print_bayes_net(bn):
    for node in bayes_net.nodes.items():
        print(node)


bayes_net = nx.DiGraph()
for k,v in moo_problem.design_variables.items():
    bayes_net.add_node(k,
        dtype="Uniform",
        lower=v.min,
        upper=v.max
    )
for k,v in moo_problem.objective_functions.items():
    bayes_net.add_node(k,
        dtype="Deterministic",
        variables=v.variables,
        string=v.function_string
    )
print_bayes_net(bn=bayes_net)


bayes_model = pm.Model()
with bayes_model:
    for k,v in moo_problem.design_variables.items():
        if bayes_net.node[k]['dtype']=='Uniform':
            bayes_net.node[k]['pymc3_obj'] = pm.Uniform(
                k,
                lower=bayes_net.node[k]['lower'],
                upper=bayes_net.node[k]['upper']
            )
    f1 = 4*bayes_net.node['x1']['pymc3_obj']**2\
         + 4*bayes_net.node['x2']['pymc3_obj']**2
    f2 = (bayes_net.node['x1']['pymc3_obj']-8)**2\
         + (bayes_net.node['x1']['pymc3_obj']+3)**2-7.7
