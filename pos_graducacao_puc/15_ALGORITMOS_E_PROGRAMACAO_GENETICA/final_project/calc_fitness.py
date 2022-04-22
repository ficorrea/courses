class CalcFitness():

    def calc_fitness(self, element):
        return sum([1 + abs(i - j) for i, j in zip(element[0:-1], element[1:])])