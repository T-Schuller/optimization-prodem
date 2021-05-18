from f_obj import f_obj
from bin2dec import bin2dec
import numpy as np
import math

def fitness (N_ind, N_prop, N_bit, bounds, pop_s):

    phi_min = bounds[:,0]
    phi_max = bounds[:,1]
    #matrix whose columns are the properties of each individual
    phi = np.zeros((N_prop, 0))
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




    return phi, phi_fitness
