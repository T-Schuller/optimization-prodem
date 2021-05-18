import random
import numpy as np


def roulette (phi_P):

    #index of Parent 1
    i_ind = np.argwhere(phi_P>random.random())
    #index of Parent 2
    j_ind = np.argwhere(phi_P>random.random())




    return i_ind[0], j_ind[0]