import numpy as np
import scipy.signal as sc
import matplotlib.pyplot as plt

Os = 0.7
Op = 0.35
Ap = 20*np.log(0.6)
As = 20*np.log(0.1)


N, wc = sc.buttord(Op, Os, Ap, As)
b, a = sc.butter(N , wc, btype = 'low', analog = False, output = 'ba')
w, H = sc.freqz(b ,a)

plt.subplot(3,1,1)
plt.plot(w, H)
plt.xlabel('w')
plt.ylabel('Mag')
plt.subplot(3,1,2)
plt.plot(w, np.angle(H))
plt.xlabel('w')
plt.ylabel('ph')
plt.subplot(3,1,3)
plt.plot(w, 20*np.log(H))
plt.xlabel('w')
plt.ylabel('Mag (dB)')