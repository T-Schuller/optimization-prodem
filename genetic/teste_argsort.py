import numpy as np
import math
import random
from scipy import sparse

from population import population
from select_o import select_o
from fitness import fitness
from bin2dec import bin2dec
from f_obj import f_obj
from roulette import roulette
from crossover import crossover
from mutation import mutation
from new_gen import new_gen
random.seed()
N = 5
x_min = 0
x_max = 60
y_min = -20
y_max = 20

#Initial bounds
bounds = np.zeros((2*N,2))
bounds[0:N,0] = x_min
bounds[0:N,1] = x_max
bounds[N:2*N,0] = y_min
bounds[N:2*N,1] = y_max

N_ind = 500
N_prop = 10 
N_bit = 16
Boolean_M = -1
ProbMut = 1E-2
ProbCross = 1
N_ger_max = 2000
N_elit = 4
N_ger_eq = 100

bounds[0,0]=5
bounds[0,1]=15
bounds[1,0]=15
bounds[1,1]=25
bounds[2,0]=25
bounds[2,1]=35
bounds[3,0]=35
bounds[3,1]=45
bounds[4,0]=45
bounds[4,1]=55

x = np.arange(10,60,10)
y = np.zeros(len(x))
xy = np.append(x,y)

# i generation
i_ger = 0


#generate initial population (random)
pop_s=population(N_ind,N_prop,N_bit)
print(len(pop_s))
#evaluate population
#phi - property (xy)
#phi_fitness - FObj value for each property
phi, phi_fitness = fitness(N_ind, N_prop, N_bit, bounds, pop_s)

I=np.zeros(len(phi_fitness))

for i in range(len(phi_fitness)):
    I[i]=Boolean_M*phi_fitness[i]

i_ind= list(I).index(min(I))






print(i_ind)