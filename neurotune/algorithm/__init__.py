"""
Algorithm objects are thin wrappers around built-in optimisation library
algorithms. At this stage they come only from the inspyred library but other
optimisation libraries could be added as well.
"""
from __future__ import absolute_import
from abc import ABCMeta  # Metaclass for abstract base classes


class Algorithm(object):
    """
    Base optimization algorithm class
    """
    # Declare this class abstract to avoid accidental construction
    __metaclass__ = ABCMeta

    # A value assigned to simulations that fail due to numerical instability
    # caused by unrealistic parameters. Can be overridden by algorithms that
    # can handle such values more gracefully (such as GridAlgorithm).
    BAD_FITNESS_VALUE = 1e20

    def __init__(self, evaluator, mutation_rate, maximize, seeds,
                 population_size):
        self.evaluator = evaluator
        self.population_size = population_size
        self.maximize = maximize
        self.mutation_rate = mutation_rate
        self.seeds = seeds
        self.tuner = None

    def optimize(self, evaluator):
        """
        The optimisation algorithm, which takes the tries to minimise the
        supplied evaluator function

        `evaluator` -- a function that takes a candidate (iterable of floats)
                       and evaluates its fitness. This function is supplied by
                       the relevant Tuner class and is transparent to the
                       algorithm.
        """
        raise NotImplementedError("'optimize' is not implemented by derived "
                                  "class of 'Algorithm' ,'{}'"
                                  .format(self.__class__.__name__))

    def set_tune_parameters(self, tune_parameters):
        self.genome_size = len(tune_parameters)
        self.constraints = [(p.lbound, p.ubound) for p in tune_parameters]

    def uniform_random_chromosome(self, random, args):  # @UnusedVariable
        return [random.uniform(lo, hi) for lo, hi in self.constraints]
