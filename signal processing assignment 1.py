# -*- coding: utf-8 -*-
"""
Created on Sun May 30 09:37:04 2021

@author: Musab Inamdar
"""

# make a random image  



from matplotlib import pyplot as plt
import numpy as np
import scipy.signal as signal

# 1)plot 3 sine wave 

# f1 = 2100
# f2 = 2400
# f3 = 2500


# 2) plot 3 cosine wave /

# f4 = 1200
# f5 = 1250
# f6 = 1300


f1 = 2100
n = 150
i = 0.001 
t = np.arange(0, n)
t1 = t * i
x = np.sin(2*np.pi*f1*t1)


plt.plot(t1, x)
plt.title("1 st sine wave")
plt.xlabel("Time in Sec")
plt.ylabel("Amplitude of X(t)")
plt.show()

f2 = 2400
n = 150
i = 0.001
t = np.arange(0, n)
t1 = t * i
x = np.sin(2*np.pi*f2*t1)

plt.plot(t1, x)
plt.title("2nd sine wave")
plt.xlabel("Time in Sec")
plt.ylabel("Amplitude of X(t)")
plt.show()

f3 = 2500
n = 150
i = 0.001
t = np.arange(0, n)
t1 = t * i
x = np.sin(2*np.pi*f3*t1)

plt.plot(t1, x)
plt.title("3rd sine wave")
plt.xlabel("Time in Sec")
plt.ylabel("Amplitude of X(t)")
plt.show()



f4 = 1200
n = 150
i = 0.001
t = np.arange(0, n)
t1 = t * i
x = np.cos(2*np.pi*f4*t1)

plt.plot(t1, x)
plt.title("1 st cosine wave")
plt.xlabel("Time in Sec")
plt.ylabel("Amplitude of X(t)")
plt.show()

f5 = 1250
n = 150
i = 0.001
t = np.arange(0, n)
t1 = t * i
x = np.cos(2*np.pi*f5*t1)

plt.plot(t1, x)
plt.title("2nd cosine wave")
plt.xlabel("Time in Sec")
plt.ylabel("Amplitude of X(t)")
plt.show()


f6 = 1300
n = 150
i = 0.001
t = np.arange(0, n)
t1 = t * i
x = np.cos(2*np.pi*f6*t1)

plt.plot(t1, x)
plt.title("3rd cosine wave")
plt.xlabel("Time in Sec")
plt.ylabel("Amplitude of X(t)")
plt.show()




# togather all

# ********************************/

Fs=8000
Fnyq = Fs/2
Ts = 1/Fs
L=800
n=np.arange(L)
t = n*Ts
N = 150
# ***********************************/.

# plotting the sine wave signal

x1 = np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t) + np.sin(2*np.pi*f3*t)

plt.plot(t,x1)
plt.title('Plot of signal x1(t)')  
plt.xlabel('Time')  
plt.ylabel('Amplitude of x1(t)') 
plt.figure() 
plt.show()

#plotting cosine wave

x2 = np.cos(2*np.pi*f4*t) + np.cos(2*np.pi*f5*t) + np.cos(2*np.pi*f6*t)


plt.plot(t,x2)
plt.title('Plot of signal x2(t)')  
plt.xlabel('Time')  
plt.ylabel('Amplitude of x2(t)') 
plt.figure() 
plt.show()


#adding x1 and x2

x = np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t) + np.sin(2*np.pi*f3*t) + np.cos(2*np.pi*f4*t) + np.cos(2*np.pi*f5*t) + np.cos(2*np.pi*f6*t)
plt.plot(t , x)
plt.title("plot of signal x(t)")

plt.ylabel("Amplitude of x(t)")
plt.figure()
plt.show()

#deffing filter
c = signal.firwin(N, cutoff=(1500/Fnyq, 3500/Fnyq), window="blackmanharris", pass_zero='bandpass')

#apply filter 

filteredSignal = signal.lfilter(c,1.0,x)
plt.plot(t, filteredSignal)
plt.title('Filtered signal')
plt.xlabel('Time')
plt.ylabel('Amplitude of x(t)')
plt.show()