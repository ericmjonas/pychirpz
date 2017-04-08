import numpy as np
import time
import chirpz.cychirpz

# This is a relatively simple benchmark to let us evaluate
# how quickly we can do PSF evaluation for a 2d field, a common
# use case


ITERS = 20

MASKN = 256
mask = np.random.rand(MASKN, MASKN).astype(np.complex64)

theta_step = np.pi/512.0
N = 32
theta_start =  - N//2 * theta_step
ITERS = 300
A = np.exp(1j * theta_start)
W = np.exp(-1j * theta_step)
pCZ = chirpz.cychirpz.PyChirpZ2d32(len(mask), N, A, W)

t1 = time.time()
for i in range(ITERS):
    zft = pCZ.compute(mask)
t2 = time.time()
print (t2-t1)/ITERS * 1000, "ms"
