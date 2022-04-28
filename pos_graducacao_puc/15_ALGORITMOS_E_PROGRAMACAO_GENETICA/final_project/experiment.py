from operator import itemgetter

from population import Population
from calc_fitness import CalcFitness

ELITISM = True
ELIT_PERC = 0.3

# Generate population
pop = Population(qtd_people=10, num_chromosome=3)
population = pop.generate_population(bin_exp=False, max_int=7)

# Calculate fitness
fit = CalcFitness()
for el in population:
    el.append(fit.calc_fitness(el))

# Order population by fitness
key = itemgetter(-1)
population.sort(key=key)

if ELITISM:
    elite = population[0:int(len(population)*ELIT_PERC)]
    population = population[int(len(population)*ELIT_PERC):]
