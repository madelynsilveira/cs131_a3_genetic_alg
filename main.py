#
# CS131 - Artificial Intelligence
# A3 - Genetic Algorithms
#
# Implementation of the A* Algorithm.
# Uses a Priority Queue where the priority is h(n) + g(n)
# by Madelyn Silveira
# 

import sys
from genetics import initial, cull, reproduce, get_weight, print_pop, order


# create an initial population
size = 10000
generation = initial(size)
size = int(size / 2)
gen_num = 0


# lifetime of the population based on initial size
while size > 2:

    # split the generation by fittest and allow them to reproduce
    generation = cull(generation, size)
    generation = reproduce(generation, size) # applies fringe operations
    
    # see the evolution if you'd like by uncommenting the line below
    print_pop(generation, gen_num)

    # prepare for next population
    size = int(size / 2)
    gen_num += 1
    

# final conclusions
generation = order(generation)
importance = str(generation[1][0])
genome = str(generation[1][1])
weight = str(get_weight(genome))

print("\n---------------------------------------------------------------------")
print("After " + str(gen_num) + " generations...")
print("Your most valuable backpack is of importance " + importance + ".")
print("The genome for this sequence is " + genome + ".")
print("It has a weight of " + weight + ".")
print("---------------------------------------------------------------------\n")




