import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
from functools import partial


# zad1
k = 1240 * math.sqrt(7)
m = 4457
l = complex(2, 1)
d = k+m
c = d+l

# zad2
print("{}".format(d))
print("{0:.3f}".format(d))
print("{0:.20f}".format(d))

# zad3
"""

function which calculate the field of roller


"""


def field_of_roller(r, h):
    return 2*math.pi*(r**2) + 2*math.pi*r


field = field_of_roller(17, 33)

# zad4
"""

function which calulcate the b for any values of : {x,t,r}


"""


def calculate_B(x, t, r):
    return (x+r)/(r*math.sin(2+x)+3.3456) * x**(t*r)


# zad5
def create_matrx(a):
    return np.array([[a, 1, -a], [0, 1, 1], [-a, a, 1]])


def inv_matrx(matrix):
    return np.linalg.inv(matrix)


def det_matrix(matrix):
    return np.linalg.det(matrix)


def transpose_matrix(matrix):
    return matrix.T


matrix = create_matrx(math.sqrt(2))
inv_matrx(matrix)
det_matrix(matrix)
transpose_matrix(matrix)

# zad6


def print_matrix_el(matrix, col, row):
    print(f"Elemnt col: {col}, row: {row} is {matrix[col-1, row-1]}")


print_matrix_el(matrix, 1, 1)
print_matrix_el(matrix, 3, 3)
print_matrix_el(matrix, 3, 2)

w1 = matrix[:, 2]
w2 = matrix[1, :]

# zad7
coeff = [1, -7, -3, -43, -28, -60]
roots = np.roots(coeff)


# zad8
first = np.arange(1, 9, 1.5)
second = np.arange(1, 9, 1.5)

# zad9
def func(x):
    return x**3 - 3*x


def get_range(min, max, numbers):
    return np.linspace(min, max, numbers)


def plot(x, y):
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


first_range = get_range(-1, 1, 1000)
second_range = get_range(-5, 5, 10000)
thrid_range = get_range(0, 5, 5000)

first_values = [func(x) for x in first_range]
second_values = [func(x) for x in second_range]
thrid_values = [func(x) for x in thrid_range]

# plot(first_range, first_values)
# plot(second_range, second_values)
# plot(thrid_range, thrid_values)


# zad10
def caluclate_heat(m, v):
    return m*v**2/2


m = 2.5
v = 60


calculate_heat_m = first = caluclate_heat(m, v)

m2 = 3
vs = np.linspace(200, 0, 10000)
heats = [caluclate_heat(m2, vel) for vel in vs]


def plot_log(x, y):
    plt.semilogy(x, y)
    plt.show()

plot(vs, heats)
plot_log(vs,heats)





        
        
    

