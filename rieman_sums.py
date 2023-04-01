import math
import random

import numpy as np
import matplotlib.pyplot as plt


def random_point(a, b):
    return np.random.uniform(a, b)


def left_riemann_sum(a, b, N):
    dx = (b-a)/N
    x_l = np.linspace(a, b-dx,N)
    return np.sum(f(x_l)*dx)


def middle_riemann_sum(a, b, N):
    dx = (b-a)/N
    x_m = np.linspace(dx/2, b-dx/2, N)
    return np.sum(f(x_m)*dx)


def right_riemann_sum(a, b, N):
    dx = (b-a)/N
    x_r = np.linspace(dx, b, N)
    return np.sum(f(x_r)*dx)


def random_riemann_sum(a, b, N):
    dx = (b-a)/N
    x_rands = []
    y_rands = []
    for i in range(N):
        x_rands.append(random_point(a+i*dx, dx*(i+1)))
        y_rands.append(f(x_rands[i]))
    summ = 0
    for i in range(N):
        summ += y_rands[i]*dx

    return x_rands, y_rands, summ


def f(x):
    return pow(math.exp(1), -x)


a = 0
b = 1
N = int(input("число промежутков: "))
n = 10

x = np.linspace(a, b, N+1)
y = f(x)
X = np.linspace(a, b, n*N+1)
Y = f(X)

dx = (b - a) / N

#left points
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(X, Y, 'r')
x_left = x[:-1]
y_left = y[:-1]
plt.plot(x_left, y_left, 'r', markersize=10)
plt.bar(x_left, y_left, dx, alpha=0.3, align='edge', edgecolor='white')
plt.title("left Riemann sum, N={}".format(N))
# plt.show()
plt.savefig("figure-l")

#right points
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(X, Y, 'b')
x_right = x[1:]
y_right = y[1:]
plt.plot(x_right, y_right, 'b', markersize=10)
plt.bar(x_right, y_right, dx, alpha=0.3, align='edge', edgecolor='white')
plt.title("right Riemann sum, N={}".format(N))
# plt.show()
plt.savefig("figure-r")

#middle points
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(X, Y, 'm')
x_middle = (x[1:]+x[:-1])/2
y_middle = (y[1:]+y[:-1])/2
plt.plot(x_middle, y_middle, 'm', markersize=10)
plt.bar(x_middle, y_middle, dx, alpha=0.3, align='edge', edgecolor='white')
plt.title("middle Riemann sum, N={}".format(N))
# plt.show()
plt.savefig("figure-m")

#random points
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(X, Y, 'cyan')
x_random, y_random, summ = random_riemann_sum(a, b, N)
plt.plot(x_right, y_right, 'cyan', markersize=10)
plt.bar(x_random, y_random, dx, alpha=0.3, align='edge', edgecolor='white')
plt.title("random Riemann sum, N={}".format(N))
# plt.show()
plt.savefig("figure-random")


right = right_riemann_sum(a, b, N)
middle = middle_riemann_sum(a, b, N)
left = left_riemann_sum(a, b, N)
rand = summ

print("Правые точки: " + str(right))
print("Средние точки: " + str(middle))
print("Левые точки: " + str(left))
print("Случайные точки: " + str(rand))
print("Вычисление по формуле Ньютона-Лейбница: 1-1/e ~ 0.6321205588")








