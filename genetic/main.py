import numpy as np
import math
import random
from scipy import sparse
import matplotlib
from matplotlib import rc
from matplotlib import pyplot as plt
import seaborn as sns
import os
import subprocess

from population import population
from select_o import select_o
from fitness import fitness
from bin2dec import bin2dec
from f_obj import f_obj
from roulette import roulette
from crossover import crossover
from mutation import mutation
from new_gen import new_gen
random.seed(0)
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


# i generation
i_ger = 0

phi_fitness_sort=[]

#generate initial population (random)
pop_s=population(N_ind,N_prop,N_bit)
pop_s=pop_s[::-1]
print(len(pop_s))
root='C:/Users/Tomás/Desktop/PRODEM/optimizacao/Trabalho_tomas/genetic/'
pop_s= open(root+ 'text_file.txt', 'r').read()

#evaluate population
#phi - property (xy)
#phi_fitness - FObj value for each property
phi, phi_fitness = fitness(N_ind, N_prop, N_bit, bounds, pop_s)
print(len(phi_fitness))
print(len(phi))
print(len(phi[0]))

#FIGURE INITIAL

I=np.zeros(len(phi_fitness))

for i in range(len(phi_fitness)):
    I[i]=Boolean_M*phi_fitness[i]

i_ind= list(I).index(max(I))

x_init=np.zeros(1)
x_fin=60*np.ones(1)
x_init= np.append(x_init,phi[0:N,i_ind])
x_init= np.append(x_init,x_fin)
y_init=np.zeros(1)
y_fin=np.zeros(1)
y_init= np.append(y_init,phi[N:,i_ind])
y_init= np.append(y_init,y_fin)
fig2, ax2 = plt.subplots(figsize = (10, 8))
plt.axis([0, 60, -20, 20])


ax2.plot([0, 10.3, 21.1, 31.7, 42.1,51.8, 60],[0,-4.28,-7.9,-9.86,-9.4,-6.01, 0],'o-', color='k')
ax2.plot(x_init,y_init,marker='+',color='b')
plt.show()
##END FIGURE INITIAL

fit_min=[]
fit_q1=[]
fit_q2=[]
n_iter=[]

count = 0
for i_ger in range(N_ger_max-1):

    phi_P = select_o(phi_fitness, Boolean_M)

    I=np.zeros(len(phi_fitness))

    for i in range(len(phi_fitness)):
        I[i]=Boolean_M*phi_fitness[i]

    i_ind= list(I).index(max(I))

    s_par=pop_s[(i_ind)*N_prop*N_bit:(i_ind+1)*N_prop*N_bit]

    pop_sons = new_gen(N_ind, N_prop, N_bit, pop_s, phi_P, ProbMut, N_elit, Boolean_M, phi_fitness, ProbCross)
    pop_s = pop_sons

    phi, phi_fitness = fitness(N_ind, N_prop, N_bit, bounds, pop_s)

    I=np.zeros(len(phi_fitness))

    for i in range(len(phi_fitness)):
        I[i]=Boolean_M*phi_fitness[i]

    i_ind= list(I).index(max(I))

    s_son = pop_s[(i_ind)*N_prop*N_bit:(i_ind+1)*N_prop*N_bit-1]

    phi = np.asarray(phi)
    testing=np.ravel(phi,'F')
    testing_2=testing[(i_ind)*2*N : (i_ind+1)*2*N]
    print(f_obj(testing_2))

#FIGURES


    I=np.zeros(len(phi_fitness))

    for i in range(len(phi_fitness)):
        I[i]=Boolean_M*phi_fitness[i]
    
    index_I=I.argsort(axis=0)

    i_ind_min= list(I).index(max(I))
    i_ind_q1=index_I[math.floor(len(I)*(1/4))]
    i_ind_q2=index_I[len(I)//2]

    x_init_min=np.zeros(1)
    x_fin_min=60*np.ones(1)
    x_init_min= np.append(x_init_min,phi[0:N,i_ind_min])
    x_init_min= np.append(x_init_min,x_fin_min)
    y_init_min=np.zeros(1)
    y_fin_min=np.zeros(1)
    y_init_min= np.append(y_init_min,phi[N:,i_ind_min])
    y_init_min= np.append(y_init_min,y_fin_min)

    x_init_q1=np.zeros(1)
    x_fin_q1=60*np.ones(1)
    x_init_q1= np.append(x_init_q1,phi[0:N,i_ind_q1])
    x_init_q1= np.append(x_init_q1,x_fin_q1)
    y_init_q1=np.zeros(1)
    y_fin_q1=np.zeros(1)
    y_init_q1= np.append(y_init_q1,phi[N:,i_ind_q1])
    y_init_q1= np.append(y_init_q1,y_fin_q1)

    x_init_q2=np.zeros(1)
    x_fin_q2=60*np.ones(1)
    x_init_q2= np.append(x_init_q2,phi[0:N,i_ind_q2])
    x_init_q2= np.append(x_init_q2,x_fin_q2)
    y_init_q2=np.zeros(1)
    y_fin_q2=np.zeros(1)
    y_init_q2= np.append(y_init_q2,phi[N:,i_ind_q2])
    y_init_q2= np.append(y_init_q2,y_fin_q2)


    if i_ger % 200 ==0:
        fig3, ax3 = plt.subplots(figsize = (10, 8))
        plt.axis([0, 60, -20, 20])

        ax3.plot([0, 10.3, 21.1, 31.7, 42.1,51.8, 60],[0,-4.28,-7.9,-9.86,-9.4,-6.01, 0],'o-', color='k')
        ax3.plot(x_init_min,y_init_min,marker='+',color='b')
        ax3.plot(x_init_q1,y_init_q1,marker='+',color='g')
        ax3.plot(x_init_q2,y_init_q2,marker='+',color='r')

        plt.show()

    phi_fitness_sort=np.sort(phi_fitness)
    fit_min=np.append(fit_min,min(phi_fitness))
    fit_q1=np.append(fit_q1,phi_fitness_sort[math.floor(len(I)*(3/4))])
    fit_q2=np.append(fit_q2,phi_fitness_sort[(len(I)//2)])
    n_iter=np.append(n_iter,i_ger)


    

    if i_ger % 200 ==0:
        fig4, ax4 = plt.subplots(figsize = (10, 8))
        ax4.scatter(n_iter,fit_min,marker='+',color='b')
        ax4.scatter(n_iter,fit_q1,marker='+',color='g')
        ax4.scatter(n_iter,fit_q2,marker='+',color='r')
        plt.show()



#END FIGURES

#STOPPING CRITERIA

    if s_par==s_son:
        count=count+1
    else:
        count=1
    
    if count == N_ger_eq:
        break

    print(count)


I=np.zeros(len(phi_fitness))

for i in range(len(phi_fitness)):
    I[i]=Boolean_M*phi_fitness[i]


index_I=I.argsort(axis=0)

i_ind=index_I[-1]

phi = np.asarray(phi)

print(f_obj(np.transpose(np.ravel(phi[ (i_ind-1)*2*N : i_ind*2*N],'F') )))