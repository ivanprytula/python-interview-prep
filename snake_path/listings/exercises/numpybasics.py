import numpy as np

"""
Numpy basics
"""

# basic arrays - think matrices
a = np.array([[1, 2], [1, 1], [0, 0]])
print(np.shape(a))  # (3, 2)
print(np.ndim(a))  # 2

# operators and methods
x = np.array([[2, 0], [0, 2]])
y = np.array([[1, 1], [2, 2]])
print(x * y)  # element-wise multiplication of equal shape arrays

print(np.matmul(x, y))  # matrix multiplication
print(x @ y)

newArray = np.arange(0, 10, 3)  # creates 1D array with constant spacing
print(newArray)

newArray = np.linspace(
    0, 10, 3
)  # creates 1D array with constant spread (note the difference)
print(newArray)

b = np.average(newArray)
print(b)

a = np.array([0, 1, 0, 0, 0])
a[::2] = 2  # array slicing: it's in form of [start:stop:step]
print(a)

variance = np.var(newArray)
std = np.std(newArray)
print("variance: ", variance, "std dev: ", std)

diff = np.diff(
    newArray
)  # calculates the difference between subsequent values in an array
print(diff)

cummsum = np.cumsum(
    np.arange(5)
)  # cummulative sum of array elements [0,1,2,3,4,5] - note new array shape
print(cummsum, cummsum.shape)

rando = np.array([10, 3, 7, 8, 3, 0, 1, 0])
sorto = np.sort(rando)  # sorted ascending order
print(sorto)

argsorted = np.argsort(
    rando
)  # returns the index of the values if they were sorted in ascending order... cool!
print(argsorted)

maxval = np.max(rando)
maxarg = np.argmax(rando)
print(maxval, maxarg)

print(
    np.nonzero(sorto), sorto[np.nonzero(sorto)]
)  # will return the non-zero indices, values
