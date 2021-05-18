from f_obj import f_obj
from g_sec import g_sec

def find_bounds (bounds, xy, S):
    L_min = min(bounds[:,0])
    U_max = max(bounds[:,1])
    a = (1+(5)**0.5)/2
    Lr = 1e-1
    alpha_max = U_max
    alpha_L = L_min*Lr
    alpha_U = U_max*Lr
    FL = f_obj(xy + alpha_L*S)
    FU = f_obj(xy + alpha_U*S)
    if FU > FL:
        print("alpha_U é o limite superior")
    else:
        while FU <= FL:
            alpha_1 = alpha_U
            F1 = FU
            alpha_U = (1+a)*alpha_1-a*alpha_L
            if alpha_U > alpha_max:
                print("Exit: não tem limites")
                break
            else:
                FU = f_obj(xy + alpha_U*S)
                if FU > F1:
                    print ("alpha_U é o limite superior")
                    break
                else:
                    alpha_L = alpha_1
                    FL = F1

    return alpha_L, alpha_U