# \bruce_ret\py2004\terminal_vel.py, B. Harmon 3/21/2024
# Numerical integration via Euler's method
#   of first order ODE m*dv/dt = m*g - 0.5*rho*v*v*CD*A
# Initial condition is v[tmin] = 0
# Compute and visualize the velocity of a freefalling man
#   Wikipedia says the terminal velocity is about 120 mph
# Coefficent of drag CD 0.50
# Reference area of a man A 0.75 m^2
# Air density rho 1.225 kg/m^3
# Mass of man 80 kg
# Acceleration of gravity g 9.8 m/s^2
# Velocity toward the ground v in m/s
# Time t in seconds s

import numpy as np
import matplotlib.pyplot as plt

CD = 0.50; A = 0.75; rho = 1.225; m = 80; g = 9.8

tmin=0; tmax=25; npts=10001
dt = (tmax-tmin) / (npts-1)
t = np.linspace(tmin, tmax, npts)
v  = np.zeros(npts)         # initialize v(t)
vp = np.zeros(npts)         # initialize dv/dt

v[0] = 0                    # IC given
vp[0] = g

for i in range(1,npts):
    vp[i] = g - (1/m)*0.5*rho*(v[i-1]**2)*CD*A
    v[i] = v[i-1] + dt*vp[i]

print(f'Terminal velocity is {v[npts-1] * 2.237:.1f} miles/hour')

fig,ax=plt.subplots(nrows=1,ncols=1,figsize=(8,4.5))
ax.plot(t,v,  color='b', label='Velocity')
ax.plot(t,vp, color='k', label='Acceleration')
ax.set_title('Velocity of a man in freefall')
ax.set_xlabel('Time t in seconds')
ax.set_ylabel('Velocity in meters/second')
ax.legend(loc=0)
ax.grid()
plt.show()
