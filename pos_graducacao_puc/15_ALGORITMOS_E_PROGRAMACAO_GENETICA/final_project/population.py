from random import randint as rdi

class Population():

    def __init__(self, qtd_people, num_chromosome):
        self.qtd_people = qtd_people
        self.num_chromosome = num_chromosome
    
    def generate_population(self, bin_exp=True, max_int=None):
        if bin_exp:
            return [[rdi(0, 1) for i in range(self.num_chromosome)] for j in range(self.qtd_people)]
        else:
            if not max_int:
                raise AttributeError('parameter max_int not be NoneType')
            else:
                return [
                    [rdi(1, max_int) for i in range(self.num_chromosome)] 
                    for j in range(self.qtd_people)]