import matplotlib
import numpy
import pylab

x = numpy.linspace(0, 5, 10)
y = x ** 2
print(x)
print(y)

matplotlib.pyplot.figure()
matplotlib.pyplot.plot(x, y, 'r')
matplotlib.pyplot.xlabel('x')
matplotlib.pyplot.ylabel('y')
matplotlib.pyplot.title('title')
matplotlib.pyplot.show()

