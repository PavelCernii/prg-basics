import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 360, 361)
y = np.sin(np.radians(x))

plt.plot(x, y)
plt.xlabel('x (degrees)')
plt.ylabel('y = sin(x)')
plt.title('Graph of y = sin(x)')
plt.grid(True)
plt.show()
