#Задача на минимизацию гладкой функции
import numpy
import pylab
import scipy
from scipy.optimize import minimize


xmin = 1
xmax = 30

def func(x):
    return numpy.sin(x / 5) * numpy.exp(x / 10) + 5 * numpy.exp(-x / 2)
xmin = 1
xmax = 30
dx = 0.01
xlist = numpy.arange(xmin, xmax, dx)
ylist = [func(x) for x in xlist]
pylab.plot(xlist, ylist)
pylab.show()

f = minimize(func, 30, method='BFGS')
print(f)
