import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([2, 0, 0.5, 1])

# assert the function is: lambda x: x**(-3/2) 

fig, ax = plt.subplots()
ax.plot(x, y**(-3/2), 'o')
ax.set_ylabel("$d^{-3/2}$")
ax.set_ylim(bottom=max(y[y!=0])**(-3/2) / 2)
ymin, ymax = ax.get_ylim()
print(ymin, ymax)
secax = ax.secondary_yaxis("right", functions=(lambda x: x**(-2/3), lambda x: x**(-3/2)))
secax.set_ylabel('d (m)')
plt.show()

