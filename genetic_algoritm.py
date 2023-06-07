import random
from keys import Keys
import heapq
from copy import deepcopy


class Chromosome(object):
    def __init__(self, keys: Keys, code: list[int] = None):
        self.keys = keys
        self.code = keys.generation() if code is None else code

    @property
    def fitness(self):
        return self.keys.fitness(self.code)

    def mutate(self):
        self.code = self.keys.mutation(self.code)

    def cross(self, other):
        if self.code == other.code:
            return Chromosome(self.keys)

        code = self.keys.cross(self.code, other.code)
        return Chromosome(self.keys, code)

    def __eq__(self, other):
        return self.fitness == other.fitness and self.code == other.code

    def __gt__(self, other):
        return self.fitness > other.fitness

    def __lt__(self, other):
        return self.fitness < other.fitness


class Population(object):
    def __init__(self, size: int, k1: float, k2: float, keys: Keys, typeSelection):
        self.size = size
        self.k1 = k1
        self.k2 = k2
        self.keys = keys
        self.heapChromosomes = Population.create_first_population(size, keys)
        self.typeSelection = typeSelection

    @staticmethod
    def create_first_population(size: int, keys: Keys) -> list[Chromosome]:
        heapChromosomes = list()
        for i in range(size):
            chromosome = Chromosome(keys)
            heapq.heappush(heapChromosomes, chromosome)
        return heapChromosomes

    @property
    def bestChromosome(self):
        return heapq.nlargest(1, self.heapChromosomes)[0]

    def next(self):
        if self.typeSelection == 'e':
            self.select_elitism()

    def select_elitism(self):
        n = int(self.size * self.k1)
        bestChromosomes = heapq.nlargest(max(n, 2), self.heapChromosomes)

        for i in range(max(n, 2)):
            for j in range(i + 1, max(n, 2)):
                newChromosome = bestChromosomes[i].cross(bestChromosomes[j])
                _ = heapq.heappushpop(self.heapChromosomes, newChromosome)

    def mutate(self):
        indexec = range(self.size)
        indexecMutation = random.choices(indexec, k=max(1, int(self.size * self.k2)))

        for index in indexecMutation:
            self.heapChromosomes[index].mutate()

        heapq.heapify(self.heapChromosomes)

    def recreate(self):
        self.heapChromosomes = Population.create_first_population(self.size, self.keys)


class GeneticAlgoritm(object):
    def __init__(self, size: int, k1: float, k2: float, keys: Keys, typeSelection: str = 'e'):
        self.population = Population(size, k1, k2, keys, typeSelection)
        self.answerFitness = self.population.bestChromosome.fitness
        self.answerCode = deepcopy(self.population.bestChromosome.code)
        self.bestFitnesses = list()

    @property
    def answer(self):
        return self.answerFitness, self.answerCode

    def start(self, n: int = 1):
        self.population.recreate()
        self.answerFitness = self.population.bestChromosome.fitness
        self.answerCode = deepcopy(self.population.bestChromosome.code)
        self.bestFitnesses.clear()
        self.resume(n)

    def resume(self, n: int = 1):
        prevBestChromosome = self.population.bestChromosome
        cnt = 0

        self.bestFitnesses.append(prevBestChromosome.fitness)

        for i in range(n):
            self.population.next()

            curBestChromosome = self.population.bestChromosome
            self.bestFitnesses.append(curBestChromosome.fitness)

            if curBestChromosome.fitness > self.answerFitness:
                self.answerFitness = curBestChromosome.fitness
                self.answerCode = deepcopy(curBestChromosome.code)

            elif curBestChromosome == prevBestChromosome:
                cnt += 1
                if cnt > 5:
                    self.population.mutate()

            else:
                prevBestChromosome = curBestChromosome
                cnt = 0
