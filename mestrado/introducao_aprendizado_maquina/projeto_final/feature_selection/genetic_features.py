from random import randint, random, sample
from operator import itemgetter


class GeneticFeatures():
    def __init__(self, 
                 qtd_features, 
                 pop_size, 
                 iterations,
                 max_repeated_best_ind=5,
                 crossover='one-point',
                 selection='elitism',
                 metric_ascending=True, 
                 total_bests=None):
        self.pop_size = pop_size
        self.crom = qtd_features
        self.crom_max = self.crom - 1
        self.iter = iterations
        self.max_repeated_best_ind = max_repeated_best_ind
        self.crossover_method = crossover
        self.selection_method = selection
        self.pop = self._gen_pop()
        self.metric_asc = metric_ascending
        if total_bests:
            self.total_selection = total_bests
        else:
            self.total_selection = self.pop_size // 2

    def _gen_pop(self):
        pop = [
            [randint(0, 1) for i in range(self.crom)] 
            for j in range(self.pop_size)]
        pop = self._check_pop_croms(pop)
        pop = [i + [None] for i in pop]
        return pop

    def _get_rand_crom(self):
        return randint(0, self.crom_max)

    def _check_pop_croms(self, pop):
        for i in pop:
            if (i[0:self.crom].count(0) == 0) or (i[0:self.crom].count(1) == 0):
                temp = self._get_rand_crom()
                i[temp] = int(not i[temp])
        return pop
    
    def selection(self):
        selection = {
            'elitism': self._elitism,
            'roulette': self._roulette,
            'tournament': self._tournament}
        selection[self.selection_method]()

    def _elitism(self):
        self.pop.sort(key=itemgetter(-1), reverse=self.metric_asc)
        self.pop = self.pop[0:self.total_selection]

    def _roulette(self):
        new_pop = []
        total = sum(i[-1] for i in self.pop)
        proportions = [i[-1] / total for i in self.pop]
        for i in range(self.total_selection):
            rnd = random() * random()
            diff = [abs(rnd - i) for i in proportions]
            new_pop.append(self.pop[diff.index(min(diff))].copy())
        self.pop = new_pop.copy()

    def _tournament(self):
        new_pop = []
        for i in range(self.total_selection):
            indexes = sample(range(self.pop_size), 3)
            temp = list(map(self.pop.__getitem__, indexes))
            temp.sort(key=itemgetter(-1), reverse=self.metric_asc)
            new_pop.append(temp[0])
        self.pop = new_pop.copy()
    
    def mutation(self):
        for i in self.pop:
            if random() <= 0.05:
                temp = self._get_rand_crom()
                i[temp] = int(not i[temp])
        self.pop = self._check_pop_croms(self.pop)
    
    def _one_point_cross(self):
        borns = []
        while len(borns) < self.pop_size - self.total_selection:
            parents = sample(self.pop, 2)
            point = randint(1, self.crom_max)
            kid = parents[0][0:point] + parents[1][point:]
            kid[-1] = None
            kid = self._check_pop_croms([kid])
            borns.append(kid[0])
        return borns
    
    def _two_point_cross(self):
        borns = []
        while len(borns) < self.pop_size - self.total_selection:
            parents = sample(self.pop, 2)
            points = sorted(sample(range(1, self.crom), 2))
            kid = (
                parents[0][0:points[0]] + 
                parents[1][points[0]:points[1]] + 
                parents[0][points[1]:])
            kid[-1] = None
            kid = self._check_pop_croms([kid])
            borns.append(kid[0])
        return borns
    
    def _uniform_cross(self):
        borns = []
        perc = 0.25
        while len(borns) < self.pop_size - self.total_selection:
            indexes = sample(range(self.crom), int(self.crom * perc))
            parents = sample(self.pop, 2)
            par_a, par_b = parents[0].copy(), parents[1].copy()
            for ind in indexes:
                par_b[ind] = par_a[ind]
            par_b[-1] = None
            kid = self._check_pop_croms([par_b])
            borns.append(kid[0])
        return borns

    def crossover(self):
        cross = {
            'one-point': self._one_point_cross,
            'two-points': self._two_point_cross,
            'uniform': self._uniform_cross}
        new_pop = cross[self.crossover_method]()
        self.pop += new_pop
    
    def _get_best_score(self):
        temp_pop = self.pop.copy()
        temp_pop.sort(key=itemgetter(-1), reverse=self.metric_asc)
        return temp_pop[0][-1]

    def _get_best_ind(self):
        temp_pop = self.pop[0:self.total_selection].copy()
        temp_pop.sort(key=itemgetter(-1), reverse=self.metric_asc)
        return temp_pop[0]

    def fit(self):
        pass

    def run(self):
        print('Running')
        max_values = []
        for it in range(self.iter):
            print(f'Generation: {it + 1}')
            self.fit()
            max_values.append(self._get_best_score())
            if max_values.count(max(max_values)) == self.max_repeated_best_ind:
                break
            self.selection()
            self.mutation()
            self.crossover()
        return max_values, self._get_best_ind(), it