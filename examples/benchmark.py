import numpy as np
import time
import chirpz
import chirpz.cychirpz

N = 256
x2d = np.zeros((N, N))
width = 8
x2d[128-width:128+width, 128-width:128+width] = 1.0


FFT_N = 4096
fft_df = 2*np.pi / FFT_N 
M = 128
phi_0 = fft_df / (2*np.pi)
W = np.exp(-1.0j * 2.0*np.pi * phi_0)
A = np.exp(-1j * np.pi/16)


cyCZ = chirpz.cychirpz.PyChirpZ2d32(N, M, A, W)

for i in range(5):

    fft2_t1 = time.time()
    out2dfft = np.fft.fft2(x2d, (FFT_N, FFT_N))
    fft2_t2 = time.time()
    print "fft took", fft2_t2 - fft2_t1

    t1 = time.time()
    out2d = chirpz.chirpz2d(x2d, M, A, W)
    t2 = time.time()

    print "fchirpz took", t2-t1


    t1 = time.time()
    out2d = cyCZ.compute(x2d)
    t2 = time.time()

    print "C++ chirpz took", t2-t1
