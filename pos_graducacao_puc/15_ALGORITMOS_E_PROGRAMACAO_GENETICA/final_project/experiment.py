from operator import itemgetter

from population import Population
from calc_fitness import CalcFitness

# Generate population
pop = Population(5, 3)
population = pop.generate_population(False, 7)

# Calculate fitness
fit = CalcFitness()
for el in population:
    el.append(fit.calc_fitness(el))

# Order population by fitness
key = itemgetter(-1)
population.sort(key=key)