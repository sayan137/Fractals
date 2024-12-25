import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation 
from matplotlib.animation import PillowWriter

def f(z,c):
    return z**2+c 

x_min,x_max=-1.5, 1.5
y_min, y_max = -1.5, 1.5
n_points= 500
x=np.linspace(x_min, x_max, n_points)
y=np.linspace(y_min, y_max, n_points)
X,Y = np.meshgrid(x, y)
Z = X + 1j*Y

c = complex(-0.89511414, 0.521295573094847167)

max_iterations = 300
julia_set = np.zeros_like(Z, dtype=int)
for i in range(max_iterations):
    Z=f(Z,c)
    mask= np.abs(Z)<100
    julia_set[mask]=i

fig,ax=plt.subplots(figsize=(12,12))
img= ax.imshow(julia_set, extent=(x_min, x_max, y_min, y_max), cmap='inferno', origin='lower')
# plt.xlabel('Re(z)')
# plt.ylabel('Im(z)')
# plt.savefig('enigmas/julia.png',dpi=300)

def animate(i):
    c_real = np.linspace(-0.9, -0.3, 150)[i]
    c = complex(c_real,0.521295573094847167)
    Z= X+ 1j*Y
    julia_set = np.zeros_like(Z, dtype=int)
    for k in range (max_iterations):
        Z= f(Z,c)
        mask= np.abs(Z)<100
        julia_set[mask]=k
    img.set_data(julia_set)  
    return [img]
    # ax.clear()
    # ax.imshow(julia_set, extent=(x_min, x_max, y_min, y_max), cmap='turbo', origin='lower')
    # ax.colorbar(Label='iterations')
    # ax.set_xlabel('Re(z)')
    # ax.set_ylabel('Im(z)')

ani=animation.FuncAnimation(fig,animate,frames=150,interval=50, blit=True)
ani.save('Enigmas/ani.gif',writer='pillow',fps=30,dpi=100)