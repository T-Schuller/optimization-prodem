import numpy as np
import math
import random

def crossover (s1, s2, N_bit, ProbCross):

    if random.random() < ProbCross:


        j=random.randint(0,N_bit)
        s_sun1=s1[0:j]+s2[j:]
        s_sun2=s2[0:j]+s1[j:]


    else:
        s_sun1=s1
        s_sun2=s2
    return s_sun1, s_sun2