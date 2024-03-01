import numpy as np

# membuat vector
a = np.array([1,2,3,4,5])
b = np.array([1.5,2.5,6,8])

# membuat vector dengan range

c = np.arange(1,10,2) #start,stop,step

# membuat linspace

d = np.linspace(1,10,4) #start, end, jumlah yg ditampilkan based on dibagi rata, mungkin nilai tengahnya

# membuat matrix

e = np.array([(1,2,3),(4,5,6)])

# matrix nilai nol

f = np.zeros((5,5)) #nilai x,y

# matrix nilai satu

g = np.ones ((5,5)) #nilai x,y

# matrix identitas

h1 = np.identity(5)
h2 = np.eye(5)

# display
print('vector')
print(a)
print(b,'\n')
print('vector dengan range')
print(c,'\n')
print('linspace')
print(d,'\n')
print('matrix')
print(e,'\n')
print('matrix nilai nol')
print(f,'\n')
print('matrix nilai satu')
print(g,'\n')
print('matrix identitas')
print(h1)
print(h2)