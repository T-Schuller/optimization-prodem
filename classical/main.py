from f_obj import f_obj
from find_bounds import find_bounds
from g_sec import g_sec
from powell import powell
import numpy as np
import math

import seaborn as sns
from cycler import cycler
import matplotlib.patches as patches
# matplotlib and seaborn for plotting
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib
from mpltools import layout
from mpltools import color
from mpltools import style


N = 5
x_min = 0
x_max = 60
y_min = -20
y_max = 20

#Initial bounds
bounds = np.zeros((2*N,2))
bounds[0:N,0] = x_min
bounds[0:N,1] = x_max
bounds[N+1:2*N,0] = y_min
bounds[N+1:2*N,1] = y_max

x = np.arange(10,60,10)
y = np.zeros(len(x))
xy = np.append(x,y)

#Powell_method
xy,F_list,xy_new = powell(xy, bounds)
F = f_obj(xy)
np.append(F_list,F)
print(xy)
print(F)



fig1, ax1 = plt.subplots(figsize = (16, 8))
ax1.plot(F_list,  label='PE')

ax1.set_ylim([-4500, 0])
ax1.set_xlim([0, 200])
ax1.set_ylabel('PE' ,family='serif', size=20)
ax1.set_xlabel('1D searches' ,family='serif', size=20)
plt.show()
C=np.zeros(len(xy))
for i in np.arange(0,len(xy_new),20):
    C=np.vstack((C,xy_new[i, :]))
exes=C[:,:5]
ys=C[:,5:]

exes = np.column_stack((exes,60*np.ones(len(exes))))
exes = np.insert(exes,0,np.zeros(len(exes)),axis=1)
ys = np.column_stack((ys,np.zeros(len(ys))))
ys = np.insert(ys,0,np.zeros(len(ys)),axis=1)

fig2,ax2=plt.subplots(figsize = (16, 8))
cmap = plt.get_cmap('cividis_r')

for i in range(len(exes)):
    plt.plot(exes[i],ys[i],'o-', color=cmap(float(i)/len(exes)))

plt.annotate(r'$W_1$', xy=(10, 0),xytext=(10.5, -0.5),family='serif')
plt.annotate(r'$W_2$', xy=(20, 0),xytext=(20.5, -0.5),family='serif')
plt.annotate(r'$W_3$', xy=(30, 0),xytext=(30.5, -0.5),family='serif')
plt.annotate(r'$W_4$', xy=(40, 0),xytext=(40.5, -0.5),family='serif')
plt.annotate(r'$W_5$', xy=(50, 0),xytext=(50.5, -0.5),family='serif')
ax2.set_ylabel('Y', family='serif', size=20)
ax2.set_xlabel('X' , family='serif', size=20)

plt.show()