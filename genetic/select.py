import numpy as np
import math

def select_o (phi_fitness, Boolean_M):



    phi_P = Boolean_M*phi_fitness
    #lowest value of FObj function
    phi_P_min = min(phi_P)
    #highest value of the FObj function
    phi_P_max = max(phi_P)
  
    phi_P = phi_P-phi_P_min + 0.01*(phi_P_max-phi_P_min)
  
    phi_P = np.cumsum(phi_P)
  
    temp = phi_P[-1]
    phi_P = phi_P/temp

    return phi_P