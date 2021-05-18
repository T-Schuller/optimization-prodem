import numpy as np
import math
import random

def mutation (s_sun, N_bit, ProbMut):
    s_sun_M = s_sun
    for i_bit in range(N_bit):
        if random.random() < ProbMut:
            if s_sun_M[i_bit]=='1':
                s_sun_M=s_sun_M[:i_bit]+'0'+s_sun_M[i_bit+1:]
            else:
                s_sun_M=s_sun_M[:i_bit]+'1'+s_sun_M[i_bit+1:]



    return s_sun_M