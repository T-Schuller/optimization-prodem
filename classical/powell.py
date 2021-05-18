from find_bounds import find_bounds
from f_obj import f_obj
from g_sec import g_sec
import numpy as np
import math



# Powell's method
# This function calculates the S-direction and calculates the minimum

def powell (xy_0, bounds):
    #Number of variables
    N = len(xy_0)
    if N % 2 != 0:
        print("N is an odd number")
    N = int(N/2)
    Li = 10
    #Maximum number of iterations
    Ni = 200
    #Relative change in f_obj
    Tol = 1E-7
    #Number of iterations in a row that check the stop criterion
    m = 5
    #Number of iterations to restart matrix H
    r = 11
    #Iteration counter
    iter = 0
    #Counter to restart matrix H
    count = 0
    #Stop criterion counter
    j = 0
    #Matrix H
    H = np.eye(int(2*N))
 
    #xy initial
    xy = xy_0 
    F_list=f_obj(xy_0)
    f_obj_new = np.zeros((2*N+1)*N+1)
    xy_new= xy
  
    while True:
        #xy initial
        for q in np.arange(0,2*N): #cycle through all columns
            S = H[:,q]
            #find_bounds - function
            [alpha_L, alpha_U] = find_bounds(bounds, xy, S)
            #g_sec - function
            alpha = g_sec(alpha_L, alpha_U, xy, S)
            #updates the solution
            xy = xy + alpha*S*np.ones(len(xy))
            #Results
            xy_new=np.vstack((xy_new,xy))

        #Look for the new direction
        S = xy-xy_0
        #S normalization
        S_max=max(abs(S))
        for l in range(len(S)):
            S[l]= S[l]/S_max
        #Find_bound - function
        [alpha_L, alpha_U] = find_bounds(bounds, xy, S)
        #g_sec - função
        alpha = g_sec(alpha_L, alpha_U, xy, S)
        #updates the solution
        xy = xy + alpha*S*np.ones(len(xy))
        #Results
        
        F_list=np.append(F_list,f_obj(xy))
        xy_new=np.vstack((xy_new,xy))
    
        #Stopping criteria
        #1st Criterion: maximum number of iterations
        
        
        if iter == Ni:
            break
        iter = iter+1
            

        #2nd Criterion: relative change in objective function
        if (iter > 1 and (abs(f_obj(xy)-f_obj(xy_0))/ max(abs(f_obj(xy)),1E-10))<=Tol):
            j = j+1
            if j >= m:
                break
        else:
            j = 0

    
        #Update matrix H
        count = count + 1
        if count > r:
            H = np.eye(2*N)
            count = 0
        else:
            H = np.roll(H, -1, axis=1)
            H[:, -1] = alpha*S/max(abs(S))


    return xy,F_list,xy_new


