# August 11, 2017 @Toronto Pearson Airport

import numpy as np

a = np.array([[1,0],[0,-1]])#(2,2)
b = np.array([[1,0],[0,0],[0,-1]])#(3,2)
c = np.array([[1,0,0],[0,1,0],[0,0,1],[1,1,1]])#(4,3)
d = np.array([[-1,0,0],[0,1,0],[0,0,1]])#(3,3)
e = np.ones(10)

# broadcasting
print(np.dot(b,a))

# multiplications
'''np.matmul'''
print(np.matmul(a,a))
print(np.matmul(b,a))
print(np.matmul(e,e)) # matmul works for sum product


#difference between np.dot & np.matmul

'''np.dot'''
# matrix product
print("a = np.array([[1,0],[0,-1]])")
print("np.dot(a,a) gives")
print(np.dot(a,a))
# [ 1 0 ]   [ 1 0 ]   [ 1 0 ]
# [ 0 -1] * [ 0 -1] = [ 0 1 ]


'''*'''
print(a*a)
#print(b*a)

print(np.dot(c,d))
#print(c*d) won't run
