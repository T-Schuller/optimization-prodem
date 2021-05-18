
def newGeneration (phi_fitness, Boolean_M):
    pop_suns = pop_s
  
    #Apply elitism
    I = Boolean_M*phi_fitness.sort()  
    for i_ind = range(len(N_elit)):
      pop_suns[(i_ind-1)*N_prop*N_bit +1: i_ind*N_prop*N_bit] = pop_s[(I(end+1-i_ind)-1)*N_prop*N_bit +1: I(end+1-i_ind)*N_prop*N_bit]
    end
  
    if (N_ind - N_elit) % 2 != 0:
        disp('Erro: N_ind - N_elit ímpar!')
        return
    end
  
    #Apply reproduction
    for i_ind = range(N_elit+1,N_ind,2): 
      #apply the Roulette method to find the index of Parent 1 and Parent 2
    	[par1_ind, par2_ind] = roulette(phi_P)
        for i_prop = range(len(N_prop)):
            #Parent 1
    	    s1 = pop_s[ (par1_ind-1)*N_prop*N_bit + (i_prop-1)*N_bit + 1 : (par1_ind-1)*N_prop*N_bit + (i_prop-1)*N_bit + N_bit]
            #Parent 2      
            s2 = pop_s[ (par2_ind-1)*N_prop*N_bit + (i_prop-1)*N_bit + 1 : (par2_ind-1)*N_prop*N_bit + (i_prop-1)*N_bit + N_bit]
           
            #crossover Parents
            [s_sun1, s_sun2] = Crossover(s1, s2, N_bit, ProbCross)
            
            #Apply mutation
            s_sun1 = Mutation(s_sun1, N_bit, ProbMut)
            s_sun2 = Mutation(s_sun2, N_bit, ProbMut)
            # Population of Sons
            pop_suns((i_ind-1)*N_prop*N_bit + (i_prop-1)*N_bit + 1    : ...
                 (i_ind-1)*N_prop*N_bit + (i_prop-1)*N_bit + N_bit) = s_sun1
            pop_suns(i_ind*N_prop*N_bit + (i_prop-1)*N_bit + 1    : ...
                 i_ind*N_prop*N_bit + (i_prop-1)*N_bit + N_bit) = s_sun2