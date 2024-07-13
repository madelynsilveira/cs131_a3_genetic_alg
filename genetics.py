#
# CS131 - Artificial Intelligence
# A3 - Genetic Algorithms
# Genetics Module
#

import sys
import random
from globals import BOXES

# GENERATIONAL OPERATORS -----------------------------------------------
def initial(size):

    elements = []

    for i in range(size):
        genome = ""

        # create a random genome
        for j in range(12):
            coin = bool((random.randint(1,999) % 2)== 0)

            if coin: genome += "0" 
            else: genome += "1"

        importance = fitness(genome)
        elements.append((importance, genome))
    
    return elements
    
def cull(generation, size):
    """
    Function to return tuples of fittest individuals in sorted order of specified size.
    """
    # sort the list in descending order based on importance 
    sorted_solutions = sorted(generation, key=lambda x: x[0])
    sorted_solutions.reverse()

    return sorted_solutions[:size]

def order(generation):
    """
    Function to return tuples of fittest individuals in sorted order.
    """
    # sort the list in descending order based on importance 
    sorted_solutions = sorted(generation, key=lambda x: x[0])
    sorted_solutions.reverse()

    return sorted_solutions

def reproduce(generation, size):
    """
    Implementation of the generation reproduction.
    """
    # up to 10% of size for each fringe operation
    mutators = random.randint(0, int(size * 0.1)) 

    # mutate chosen number of mutators
    for m in range(mutators):
        # get a random index within worse half of generation size (2nd half)
        index = random.randint(int(size/2), size - 1)

        # mutate the genome
        genome = mutate(str(generation[index][1]))
        generation[index] = (fitness(genome), genome)

    # recombine chosen number of mutators (all members available)
    for m in range(mutators):
        index = random.randint(0, size - 2)
        g1 = str(generation[index][1])
        g2 = str(generation[index + 1][1])

        (g1, g2) = crossover(g1, g2)
        generation[index] = (fitness(g1), g1)
        generation[index] = (fitness(g2), g2)
        
    return generation


# INDIVIDUAL OPERATORS
def fitness(genome):
    """
    Implementation of the fitness test for this algorithm.
    """
    weight = 0
    importance = 0

    length = len(genome)
    if length != 12: return 0

    for i in range(0, length):
        if genome[i] == "1":
            weight += BOXES[i][0]
            importance += BOXES[i][1]

    # exclude overweight boxes
    if weight <= 250:
        return importance
    return 0

# FRINGE OPERATIONS ----------------------------------------------------
def mutate(genome):
    """
    Implementation of the mutation fringe operation.
    """
    # Choose a random index
    index = random.randint(0, len(genome)-1)
    replacement = ""

    # get opposite binary
    if genome[index] == "1": replacement = "0"
    else: replacement = "1"

    # create new string
    genome = genome[:index] + replacement + genome[index+1:]

    return genome

def crossover(g1, g2):
    """
    Implementation of the crossover fringe operation.
    """
    # Choose a random index
    rand = random.randint(0, 12)

    # cross parts
    new1 = g1[:rand] + g2[rand:]
    new2 = g2[:rand] + g1[rand:]

    return (new1, new2)

def get_weight(genome):
    """
    Function to return the weight of a genome
    """
    weight = 0

    for i in range(0, len(genome)):
        if genome[i] == "1":
            weight += BOXES[i][0]

    return weight

# ADDITIONAL FUNCTIONS -------------------------------------------------
def print_pop(generation, gen_num):

    print("\nGeneration " + str(gen_num) + " members:")
    sys.stdout.write("Fittest = " )
    for x in range(len(generation)):
        sys.stdout.write("(" + str(generation[x][0]) + ",")
        sys.stdout.write(" " + str(generation[x][1]) + "),")
        if x % 5 == 0: sys.stdout.write("\n")
    sys.stdout.write(" Members = " + str(len(generation)) + "\n")
