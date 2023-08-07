from scipy import signal
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

t= np.linspace(0,1,500,endpoint=False)
square_wave = signal.square(2*np.pi*5*t)
#plt.plot(t,square_wave)
#plt.ylim(-2,2)
#plt.show()

sin_sig = np.sin(2*np.pi*t)
pwm = signal.square(2*np.pi*30*t,duty = (sin_sig+1)/2)

style.use('dark_background')

plt.figure()

plt.subplot(2,1,1)
plt.plot(t,sin_sig)


plt.subplot(2,1,2)
plt.plot(t,pwm)

plt.ylim(-1.5,1.5)

plt.show()
