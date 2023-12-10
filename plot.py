import matplotlib.pyplot as plt
import numpy as np

a=np.arange(100)
b=np.ones(100)

plt.plot(a,b)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.savefig('test_plot.png')
