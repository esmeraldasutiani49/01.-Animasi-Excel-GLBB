import numpy as np
import matplotlib.pyplot as plt

alpha = np.radians(45)
g = 9.8
v0 = 1.4e-3
x0 = 0.0
y0 = 0.0
t0 = 0.0
tmax = 0.1

v0x = v0*np.cos(alpha)
v0y = v0*np.sin(alpha)

X = ((v0**2)*np.sin(2*alpha))/(2*g)
print("jarak horizontal maksimum = ",X,"m")
Y = ((v0**2)*np.sin(alpha)**2)/(2*g)
print ("jarak vertikal maksimum = ",Y,"m")
T = (2*v0*np.sin(alpha))/g
print("waktu mencapai jarak horizontal maksimum = ",T,"s")
print("\n")

t = np.arange(0.0, tmax, 10**(-6))
y = v0y*t - 0.5*g*t**2
x = v0x*t

fig, ax = plt.subplots()
ax.plot(x,y)
ax.set(label='x (m)', ylabel= 'y (m)', title = 'grafik gerak parabola')
ax.grid()
plt.show()
