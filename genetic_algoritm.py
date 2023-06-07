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


class Generation(object):
    def __init__(self, size: int, k1: float, k2: float, keys: Keys, typeSelection):
        self.size = size  # Размер популяции
        self.k1 = k1  # Доля лучших особей, дающих потомство.
        self.k2 = k2  # Доля мутирующих особей.
        self.keys = keys  # Функции генерации, приспособленности, мутации, скрещивания.
        self.heapChromosomes = Generation.create_first_generation(size, keys)  # Бинкуча особей (очередь с приоритетом.)
        self.typeSelection = typeSelection  # Тип выборки лучших особей.

    @staticmethod
    def create_first_generation(size: int, keys: Keys) -> list[Chromosome]:
        heapChromosomes = list()
        for i in range(size):
            chromosome = Chromosome(keys)
            heapq.heappush(heapChromosomes, chromosome)
        return heapChromosomes

    @property
    def bestChromosome(self) -> Chromosome:
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
        self.heapChromosomes = Generation.create_first_generation(self.size, self.keys)


class GeneticAlgoritm(object):
    @staticmethod
    def check_parametrs(size, k1, k2, typeSelection):
        if size < 2:
            raise Exception('GeneticAlgoritm.size shoud be more one.')
        if not 0 < k1 <= 1:
            raise Exception('GeneticAlgoritm.k1 shoud be in (0; 1].')
        if not 0 < k2 <= 1:
            raise Exception('GeneticAlgoritm.k2 shoud be in (0; 1].')
        if typeSelection not in {'e'}:
            raise Exception('GeneticAlgoritm.typeSelection shoud be in {e}.')

    def __init__(self, size: int, k1: float, k2: float, keys: Keys, typeSelection: str = 'e'):
        GeneticAlgoritm.check_parametrs(size, k1, k2, typeSelection)
        self.population = Generation(size, k1, k2, keys, typeSelection)  # Текущая популяция.
        self.answerFitness = self.population.bestChromosome.fitness  # Лучшая приспособленность за всё время.
        self.answerCode = deepcopy(self.population.bestChromosome.code)  # Лучший генетический код за всё время.
        self.bestFitnesses = list()  # Список лучших приспособленностей каждого поколения.

    @property
    def answer(self) -> tuple[int, list[int]]:
        return self.answerFitness, self.answerCode

    def start(self, n: int = 1):
        self.population.recreate()
        self.answerFitness = self.population.bestChromosome.fitness
        self.answerCode = deepcopy(self.population.bestChromosome.code)
        self.bestFitnesses.clear()
        self.resume(n)

    def resume(self, n: int = 1):
        prevBestChromosome = self.population.bestChromosome
        cnt = 0  # Число поколений при не меняющимся лидере.

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
