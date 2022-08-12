%matplotlib inline
import numpy
import pylab
import math
import matplotlib.pyplot as plt

xmin = 1
xmax = 15

def func(x):
    return numpy.sin(x / 5) * numpy.exp(x / 10) + 5 * numpy.exp(-x / 2)
xmin = 1
xmax = 15
dx = 0.01
xlist = numpy.arange(xmin, xmax, dx)
ref_ylist = [func(x) for x in xlist]
pylab.plot(xlist, ref_ylist)
pylab.show()

points = numpy.array([1, 4, 10, 15])
n = points.size
A = numpy.zeros((n, n))
for index in range(0, n):
    A[index] = numpy.power(numpy.full(n, points[index]), numpy.arange(0, n, 1))
    #numpy.full возвращает массив размерности n * points[index]
b = func(points)
solve = numpy.linalg.solve(A,b)
def polinom(x):
    tiles = numpy.tile(x, (n, 1))
    tiles[0] = numpy.ones(x.size)
    for index in range(1, n):
        tiles[index] = tiles[index] ** index
    return solve.dot(tiles)
x = numpy.linspace(1, 15, 100)
plt.plot(x, func(x))
plt.plot(x, polinom(x))

print(solve)

