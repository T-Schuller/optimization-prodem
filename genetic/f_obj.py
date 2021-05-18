import numpy as np

def f_obj (xy):

    

    N=len(xy)
    if N % 2 != 0:
        print("N is an odd number")
    
    #N - number of weights
    N = N//2
    #Li - length for each spring
    Li = 10
    L0 = Li*np.ones(N+1)
    X = np.transpose(xy[0:N])
    Y = np.transpose(xy[N:2*N+1])
    #K - stiffness of spring i
    K=np.ones(N+1)
    for i in range(N+1):
        K[i] = 500 + 200*(abs(N/3-(i+1))**2)

    #W - weight
    W =np.ones(N)
    for i in range(N):
        W[i] = 50*(i+1)
    Xt = np.insert(X,0,0)
    Xt = np.append(Xt,Li*(N+1))
    Yt = np.insert(Y,0,0)
    Yt = np.append(Yt,0)

    #Delta_L - deformation of spring i
    diff1=np.diff(Xt,1)
    diff2=np.diff(Yt,1)
    Delta_L = (diff1**2 + diff2**2)**(0.5)-L0
    #F - Potential energy
    F = 0.5*np.sum(K.conj()*Delta_L**2, axis=0)+np.sum(W.conj()*Y, axis=0)

    return F
