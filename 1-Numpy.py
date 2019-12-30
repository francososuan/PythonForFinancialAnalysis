import numpy as np

#Creating Numpy Array

my_list = [1,2,3]

x = np.array(my_list)

print(x)

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]

y = np.array(my_matrix)

print(y)

a = list(range(0,5))

print(a)

b = np.arange(0,5)

print(b)

c = np.zeros((3,5))

print(c)

d = np.ones((2,3))

print(d)

e = np.linspace(0,10,21)

print(e)

f = np.eye(5)

print(f)

g = np.random.rand(5,2)

print(g)

h = np.random.randn(5,4)

print(h)

arr = np.arange(25)

ranarr = np.random.randint(0,50,10)

arr.reshape(5,5)

