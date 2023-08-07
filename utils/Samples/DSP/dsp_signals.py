from matplotlib import pyplot as plt
from matplotlib import style
from DSP import mysignals as sig

f,pltr_arr = plt.subplots(3,sharex = True)
f.suptitle('Multiplots')

pltr_arr[0].plot(sig.InputSignal_1kHz_15kHz)
pltr_arr[1].plot(sig.InputSignal_1kHz_15kHz)
pltr_arr[2].plot(sig.InputSignal_1kHz_15kHz)

plt.show()