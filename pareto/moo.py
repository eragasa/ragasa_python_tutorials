from collections import OrderedDict

class DesignVariable(object):
    def __init__(self):
        self.min = 0
        self.max = 1.0

class ObjectiveFunction(object):
    def __init__(self):
        self.design_variables = OrderedDict()
        self.function_string = ""
        self.value = None
    def evaluate(self,x):
        """
        x (dict): a dictionary of variable names and variable values
        """

        # copy values of x
        for k,v in self.design_variables:
            self.design_variables[k] = x[k]

        s = self.function_string

        for k,v in self.design_variables:
            s = s.replace(k,v)
        self.value = eval(s)
        return self.value

class ConstraintFunction(object):
    def __init__(self):
        self.design_variables = OrderedDict()
        self.function_string = ""

    def evaluation(self,x):
        """
        x (dict): a dictionary of variable name and variable values
        """

        for k,v in self.design_variables:
            self.design_variables[k] = x[k]

        s = self.function_string

class MultiObjectiveOptimizationProblem(object):
    def __init__(self):
        self.design_variables = OrderedDict()
        self.objective_functions = OrderedDict()
        self.constraint_functions = OrderedDict()

    def evaluate(self,x):

        for k,v in self.design_variables.items():
            self.design_variables[k] = x[k]

        for k,v in self.objective_functionse.items():
            v.evaluate(x = self.design_variables)

    def x(self):
        return OrderedDict([(k,v.value) for self.design_variables.items()])

    def y(self):
        return OrderedDict([(k,v.value) for self.objective_functions.items()])

class MultiObjectiveOptimizationProblemSolver(object):
    pass
