import numpy
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x=numpy.random.randint(0,100,size=60)
y=numpy.random.randint(0,100,size=60)
z=numpy.random.rand(60)
plt.scatter(x, y, c=z, s=100, cmap=plt.cm.cool, edgecolors='None', alpha=0.75)
plt.colorbar()
plt.show()