import sys
import random
import copy
import json
import numpy as np

# CONFIG
POPULATION_SIZE = 100
NUMBER_OF_ITERATIONS = 500
TOURNAMENT = 4
PROB_CROSSOVER = 0.9
PROB_MUTATION = 0.05
SEED = 42
TARGET_STRING = "METHINKS IT IS LIKE A WEASEL"
GENOTYPE_SIZE = len(TARGET_STRING)

OPTIONS = list(range(65, 91)) + [32]


def fitness(individual):
    """ Computes the number of positions between the phenotype and the target string
    This function should return the number of different positions between the phenotype of an individual and the TARGET_STRING
    """
    different_pos = 0
    return different_pos


def generate_random_individual():
    """ You should generate a random individual the elements that are available in the OPTIONS variable
    """
    genotype = []
    ### Your code here
    return {'genotype': genotype, 'fitness': None }


def generate_initial_population():
    for i in range(POPULATION_SIZE):
        yield generate_random_individual()


def mapping(genotype):
    sentence = ""
    for value in genotype:
        sentence += chr(value)
    return sentence

    


def evaluate(ind):
    pheno = mapping(ind['genotype'])
    ind['fitness'] = fitness(pheno)



def choose_indiv(population):
    pool = random.sample(population, TOURNAMENT)
    pool.sort(key=lambda i: i['fitness'])
    return copy.deepcopy(pool[0])


def crossover(p1, p2):
    """You should implement the combination operator with a single cut point
    """
    genotype = []
    
    #Your code here
    
    return {'genotype': genotype, 'fitness': None}


def mutate(p):
    p = copy.deepcopy(p)
    p['fitness'] = None
    ### Your code here
    return p


def main():
    bests = []
    # Create a initial population randomly
    population = list(generate_initial_population())
    it = 0
    #Evaluate how good the individuals are (problem dependent)
    for it in range(it, NUMBER_OF_ITERATIONS):
        for i in population:
            if i['fitness'] == None:
                evaluate(i)
        population.sort(key = lambda x: x['fitness'])
        best = (mapping(population[0]['genotype']), population[0]['fitness'])
        bests.append(best)
        print("Best at", it, best[0])
        new_population = []
        while len(new_population) < POPULATION_SIZE:
            if random.random() < PROB_CROSSOVER:
                #Parent Selection
                p1 = choose_indiv(population)
                p2 = choose_indiv(population)
                #Recombination
                ni = crossover(p1, p2)
            else:
                ni = choose_indiv(population)
            #Mutation 
            if random.random() < PROB_MUTATION:
                ni = mutate(ni)
            new_population.append(ni)
        population = new_population
    print(bests[-1])
if __name__ == '__main__':
    random.seed(SEED)
    main()