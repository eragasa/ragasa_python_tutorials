from moo import MultiObjectiveOptimizationProblem
from moo import DesignVariable
from moo import ObjectiveFunction
from moo import ConstraintFunction
#BinhAndKohn
moo_problem = MultiObjectiveOptimizationProblem()
self.design_variables['x1'] = DesignVariable()
self.design_variables['x1'].min = 0
self.design_variables['x2'].max = 5
self.design_variables['x2'] = DesignVariable()
self.design_variables['x2'].min = 0
self.design_variables['x2'].max = 3
self.objective_functions['f1'] = ObjectiveFunction()
self.objective_functions['f1'] = '4*x1**2+4*x2**2'
self.objective_functions['f2'] = ObjectiveFunction()
self.objective_functions['f2'] = '(x1-5)**2+(x2-5)**2'
self.constraint_functions['g1'] = ConstraintFunction()
self.constraint_functions['g1'] = '-(x1-5)**2-x2**2+25.0'
self.constraint_functions['g2'] = ConstraintFunction()
self.constraint_functions['g2'] = '(x1-8)**2+(x2+3)**2-7.7'
