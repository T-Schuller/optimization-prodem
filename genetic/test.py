import numpy as np
import math
import random
from bin2dec import bin2dec
from scipy import sparse
from f_obj import f_obj
from roulette import roulette
from crossover import crossover
from mutation import mutation
from new_gen import new_gen

N = 5
x_min = 0
x_max = 60
y_min = -20
y_max = 20

#Initial bounds
bounds = np.zeros((2*N,2))
bounds[0:N,0] = x_min
bounds[0:N,1] = x_max
bounds[N+1:2*N,0] = y_min
bounds[N+1:2*N,1] = y_max

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

##POPULATION

pop_array=np.zeros(N_ind*N_prop*N_bit)

for i in range(N_ind*N_prop*N_bit):
    pop_array[i] = random.randint(0, 1)
pop_s = ' '.join([str(elem) for elem in pop_array])
#pop_s = str(pop_array)
pop_s=pop_s.replace(".0", "")
pop_s=pop_s.replace(" ", "")

##END POPULATION

##FITNESS

phi_min = bounds[:,0]
phi_max = bounds[:,1]
#matrix whose columns are the properties of each individual
phi = np.zeros((N_prop, 1))
#FObj vector for each individual
phi_fitness = np.zeros((1, N_ind))
#column with the precision (increment) for each property
d_phi = np.divide((phi_max-phi_min),(2**N_bit-1))
#column with number of increments in each property
i_d_phi = np.zeros(N_prop)

#fitness of each individual (i_ind)
for i_ind in range(N_ind):
    for i_prop in range(N_prop):
        s = pop_s[(i_ind)*N_prop*N_bit + (i_prop)*N_bit  : (i_ind)*N_prop*N_bit + (i_prop)*N_bit + N_bit]
        i_d_phi[i_prop] = bin2dec(s)

    #property value
    phi = np.column_stack((phi,phi_min + i_d_phi*d_phi))
    #value of FObj for the property
    phi_fitness[:,i_ind] = f_obj(phi[:,i_ind])
phi_fitness=phi_fitness[0]

phi = np.delete(phi, 0, 1)

##END FITNESS

count = 0

##SELECT

phi_P = Boolean_M*phi_fitness
#lowest value of FObj function
phi_P_min = phi_P.min()
#highest value of the FObj function
phi_P_max = phi_P.max()
  
phi_P = phi_P-phi_P_min + 0.01*(phi_P_max-phi_P_min)
  
phi_P = np.cumsum(phi_P)
  
temp = phi_P[-1]
phi_P = phi_P/temp

#print(phi_P)

##END SELECT

I=np.zeros(len(phi_fitness))

for i in range(len(phi_fitness)):
    I[i]=Boolean_M*phi_fitness[i]

I=I.argsort(axis=0)

i_ind=I[-1]

s_par=pop_s[(i_ind-1)*N_prop*N_bit+1:i_ind*N_prop*N_bit]

#print(s_par)

pop_sons = new_gen(N_ind, N_prop, N_bit, pop_s, phi_P, ProbMut, N_elit, Boolean_M, phi_fitness, ProbCross)
pop_s = pop_sons


print(pop_s)