from find_bounds import find_bounds
from f_obj import f_obj
from g_sec import g_sec
import numpy as np
import math


# Powell's method
# This function calculates the S-direction and calculates the minimum

def find_bounds (xy_0, bounds):
    #Number of variables
    N = length(xy_0)
    if N % 2 != 0:
        print("N is an odd number")
    N = N/2
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
    i = 1
    #Counter to restart matrix H
    count = 0
    #Stop criterion counter
    j = 0
    #Matrix H
    H = np.eye(2*N)
 
    #xy initial
    xy= xy_0 
    xy_new = np.zeros((2*N+1)*N+1, 2*N)
    f_obj_new = np.zeros((2*N+1)*N+1, 0)
    xy_new[0,:]= xy
    f_obj_new[0] = f_obj(xy)
  
    while true:
        #xy initial
        for i in np.arange(1,2*N): #cycle through all columns
            S = H(:,q)
            #find_bounds - function
            [alpha_L, alpha_U] = find_bounds(bounds, xy, S)
            #g_sec - function
            alpha = g_sec(alpha_L, alpha_U, xy, S)
            #updates the solution
            xy = xy + alpha*S
            #Results
            xy_new((i-1)*2*N+i+q,:) = xy
            f_obj_new((i-1)*2*N+i+q) = f_obj(xy)

        #Look for the new direction
        S = xy-xy_0
        #S normalization 
        S = S/max(abs(S))
        #Find_bound - function
        [alpha_L, alpha_U] = find_bounds(bounds, xy, S)
        #g_sec - função
        [alpha] = g_sec(alpha_L, alpha_U, xy, S)
        #updates the solution
        xy = xy + alpha*S
        #Results
        xy_new((1+2*N)*i+1,:) = xy
        f_obj_new((1+2*N)*i+1) = f_obj(xy)
    
        #Stopping criteria
        #1º Criterion: maximum number of iterations
        if i == Ni:
            true
            break
        else:
        i = i+1

        #2º Criterion: relative change in objective function
        if (i > 1 and (abs(f_obj(xy)-f_obj(xy_0))/ max(abs(f_obj(xy)),1E-10))<=Tol)
            j = j+1
            if j >= m:
                true
                break
        else:
            j = 0

    
        #Update matrix H
        count = count + 1
        if count > r:
            H = eye(2*N)
            count = 0
        else:
            H = np.roll(H, -1, axis=1)
            H(:, end) = alpha*S/max(abs(S))



  fprintf('========================\n')
  fprintf('Results from Powell''s method\n')
  fprintf('========================\n')
  fprintf('\nObjective Function value: %.8g\n',f_obj_new((1+2*N)*i+1))
  fprintf(['\nFinal configuration:\n %.6g\t %.6g\t %.6g\t %.6g\t %.6g\n',...
'%.6g\t%.6g\t%.6g\t%.6g\t%.6g\n'], xy_new((1+2*N)*i+1,:))
  fprintf('\nStopping criterion:')
  if false
    fprintf('\tMaximum number of iterations reached.')
  elseif false
    fprintf('\tRelative change in objective function.')
  end
  fprintf('\n\nTotal number of iterations: %i\n',i)
  fprintf('\nTotal number of function evaluations: %i\n',(1+2*N)*i)
  
  #Objective funtion evolution
  figure('Name','Objective funtion evolution','Position',[200,300,700,350],'Color',[1 1 1])
  hold on
  plot(0:(1+2*N)*i,f_obj_new(1:(1+2*N)*i+1),'k-','linewidth',2)
  grid on
  xlabel('Unidirectional searches','FontSize',12,'Interpreter','latex')
  ylabel('$PE$','FontSize',12,'Interpreter','latex') 
  
    
  # Plot of the evolution of spatial coordinates
  figure('Name','Evolution of the objective function',...
         'Position',[900,350,700,250],'Color',[1 1 1])
  Colors=flipud(parula(i))
  hold on
  var = [0,2*N+1:2*N+1:(1+2*N)*i-1]
  for t=1:size(var,2)
    v=var(t)+1
  plot([0,xy_new(v,1:N),(N+1)*Li],[0,xy_new(v,N+1:end),0],'o-',...
         'Color',Colors(t,:),'MarkerFaceColor',Colors(t,:),'MarkerSize',7)
  end
  grid on
  xlabel('$X$','FontSize',12,'Interpreter','latex')
  ylabel('$Y$','FontSize',12,'Interpreter','latex')
  return xy


