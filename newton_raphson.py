import numpy as np
import matplotlib.pyplot as plt 

tol=1e-8

f= lambda z: z**4-1
f_prime= lambda z: 4*z**3

def newton(z0 ,f , f_prime, max_it=1000):
    z = z0
    for i in range(max_it):
        dz=f(z)/f_prime(z)
        if abs(dz) < tol:
            return z
        z -= dz
    return False

def plot_fractal(f, f_prime, n=200, domain=(-1,1,-1,1)):
    roots = []
    m = np.zeros((n,n))
    def root_index(roots,r):
        try:
            return np.where(np.isclose(roots,r,atol=tol))[0][0]
        except IndexError:
            roots.append(r)
            return len(roots) - 1
    
    xmin, xmax, ymin, ymax = domain
    for ix, x in enumerate(np.linspace(xmin, xmax, n)):
        for iy, y in enumerate(np.linspace(ymin, ymax, n)):
            z = x + 1j*y
            r = newton(z, f, f_prime)
            if r is not False:
                ir = root_index(roots, r)
                m[iy, ix] = ir
    
    plt.imshow(m, cmap='rainbow', origin='lower')
    plt.axis('off')
    plt.show()

plot_fractal(f, f_prime, n=500)