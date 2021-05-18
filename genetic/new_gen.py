import numpy as np
import math
from roulette import roulette
from crossover import crossover
from mutation import mutation

def new_gen (N_ind, N_prop, N_bit, pop_s, phi_P, ProbMut, N_elit, Boolean_M, phi_fitness, ProbCross):

    pop_sons=pop_s

    I=np.zeros(len(phi_fitness))

    for i in range(len(phi_fitness)):
       I[i]=Boolean_M*phi_fitness[i]

    I=I.argsort(axis=0)

    for i_ind in range(N_elit):

        pop_sons=pop_sons[0:(i_ind)*N_prop*N_bit +1]+ pop_s[(I[-i_ind])*N_prop*N_bit +1: I[-i_ind]*N_prop*N_bit] + pop_sons[i_ind*N_prop*N_bit+1:]


    if (N_ind-N_elit) % 2 != 0:
        print('Erro: N_ind - N_elit ímpar!')
    
    for i_ind in range(N_elit,N_ind,2):
        par1_ind, par2_ind = roulette(phi_P)

        for i_prop in range(N_prop):
            #Parent 1
            s1 = pop_s[ (par1_ind[0])*N_prop*N_bit + (i_prop)*N_bit     : (par1_ind[0])*N_prop*N_bit + (i_prop)*N_bit + N_bit]
            #Parent 2      
            s2 = pop_s[ (par2_ind[0])*N_prop*N_bit + (i_prop)*N_bit     : (par2_ind[0])*N_prop*N_bit + (i_prop)*N_bit + N_bit]

            son_1,son_2 = crossover(s1, s2, N_bit, ProbCross)

            son_1 = mutation(son_1, N_bit, ProbMut)
            son_2 = mutation(son_2, N_bit, ProbMut)

        
            pop_sons=pop_sons[0:(i_ind)*N_prop*N_bit + (i_prop)*N_bit + 1 ]+son_1+pop_sons[(i_ind)*N_prop*N_bit + (i_prop)*N_bit + N_bit+1:]
        
            pop_sons=pop_sons[0:i_ind*N_prop*N_bit + (i_prop)*N_bit + 1 ]+son_2+pop_sons[i_ind*N_prop*N_bit + (i_prop)*N_bit + N_bit+1:]

    return pop_sons