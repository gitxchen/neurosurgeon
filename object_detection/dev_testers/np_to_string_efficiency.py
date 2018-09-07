import io
import zlib
import numpy as np
from time import time as t

arr = np.random.rand(1, 1008)

f = io.BytesIO()

start = t()
np.save(f, arr)
print(str((t() - start) * 1000) + ' ms')

start = t()
s = np.array2string(arr)
print(str((t() - start) * 1000) + ' ms')

body = ''

with open('testing.txt', 'r') as f:
    body = f.read()
    f.close()



# print(body)
regexp = r"(\d+)"
# dt = [('num', np.float)]
start = t()
arr2 = np.fromstring(body, dtype=float, sep=' ')
print(arr2)
print(arr2.shape)
print(str((t() - start) * 1000) + ' ms')