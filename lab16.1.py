import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(0.1, 8, 100)
y = 1 / x + 2.4 * np.exp(x)

plt.plot(x, y, 'g--', label='y = 1/x + 2.4 * e^x')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік функції y = 1/x + 2.4 * e^x')
plt.legend(loc='upper left')
plt.grid(True)

plt.savefig('image.png', dpi=300)
plt.show()
