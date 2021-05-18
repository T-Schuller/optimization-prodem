import random
import numpy as np
random.seed(0)
def population (N_ind,N_prop,N_bit):

    pop_array=np.zeros(N_ind*N_prop*N_bit)

    for i in range(1,N_ind*N_prop*N_bit):
        pop_array[i] = random.randint(0, 1)
    pop_s = ' '.join([str(elem) for elem in pop_array])

    pop_s=pop_s.replace(".0", "")
    pop_s=pop_s.replace(" ", "")
    print(len(pop_s))
    return pop_s