import numpy as np

"""Lists in python act as any data structure should. 
In NumPy, everything is specifically to do math"""

L = [1,2,3]
A = np.array([1,2,3])

# print("Py List***********************")
# for e in L:
#     print(e)

# this works as expected, it adds a new index
# L.append(4)
# L += [5]

# this appends the L array to itself sequentially. In the same way that L += L would.
# L *= 2

# Didn't know you could do this, kind of cool
# L2 = [e + 3 for e in L]
# for e in L2:
#     print(e)

# This works to square each value in the array but could be simpler in NumPy
# L2 = []
# for e in L:
#     L2.append(e**2)

# for e in L:
#     print(e)

print("NP Array***********************")

# A.append(4) //this wont work, not able to append this way

# this will add 4 to each value in the array
# A += np.array([4])

# this performs as expected, adding each index to each other
# A += np.array([4,5,6])

# this results in an error, as vectors are of different size
# A += np.array([4,5])

# this performs as expected in scalar, just multiplies each index by 2
# A *= 2

# This is so much easier for squaring values in an array in NumPy
# A **= 2

# ...or square roots
# A = np.sqrt(A)

# ...or logs
# A = np.log(A)

# ...or exponentials
# A = np.exp(A)

# ...or Tangents
# A = np.tanh(A)

for e in A:
    print(e)

