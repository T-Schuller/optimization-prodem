def g_sec (alpha_L, alpha_U, xy, S):


    import numpy as np
    import math
    from f_obj import f_obj
    #from find_bounds import find_bounds



    tol_r = 1e-2 
    tau = (3-(5)**0.5)/2
    N_iter = np.ceil((math.log(tol_r)/(math.log(1-tau)))+3)


    FL = f_obj(xy+alpha_L*S*np.ones(len(xy)))
    FU = f_obj(xy+alpha_U*S*np.ones(len(xy)))

    alpha_1 = (1-tau)*alpha_L+tau*alpha_U
    F1 = f_obj(xy+alpha_1*S*np.ones(len(xy)))
    alpha_2 = tau*alpha_L+(1-tau)*alpha_U
    F2 = f_obj(xy+alpha_2*S*np.ones(len(xy)))

    alp = np.zeros((int(N_iter+2),2))
    Falp = np.zeros((int(N_iter+2),2))
    alp[0,:] = [alpha_L, alpha_U]
    alp[1,:] = [alpha_1, alpha_2]
    Falp[0,:] = [FL, FU] 
    Falp[1,:] = [F1, F2]
  
    k=3
    while k < N_iter:
        k = k+1
        if F1 > F2:
            alpha_L = alpha_1
            FL = F1
            alpha_1 = alpha_2
            F1 = F2
            alpha_2 = tau*alpha_L+(1-tau)*alpha_U
            F2 = f_obj(xy+alpha_2*S*np.ones(len(xy)))
        else:
            alpha_U = alpha_2
            FU = F2
            alpha_2 = alpha_1
            F2 = F1
            alpha_1 = (1-tau)*alpha_L+tau*alpha_U
        F1 = f_obj(xy+alpha_1*S*np.ones(len(xy)))

        alp[int(N_iter+1),:] = [alpha_L, alpha_U]
        Falp[int(N_iter+1),:] = [f_obj(xy+alpha_L*S*np.ones(len(xy))), f_obj(xy+alpha_U*S*np.ones(len(xy)))]

  
    index_min = np.argmin([FL,F1,F2,FU])
    if index_min == 0:
        alpha=alpha_L
    elif index_min == 1:
        alpha=alpha_1
    elif index_min == 2:
        alpha=alpha_2
    elif index_min == 3:
        alpha=alpha_U  
 

    return alpha