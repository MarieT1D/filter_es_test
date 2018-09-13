import numpy as np
import matplotlib.pyplot as plt

daten=np.loadtxt("Daten 2.txt", dtype='unicode_')

#time=daten[:,0]
t=time[0] 
werte=np.array(daten, dtype=int)


x=np.zeros_like(werte)
for i in range(len(x)):
    x[i]=i*5
print(werte,x)
plt.plot(x,werte, linestyle='none', marker='.')


#forecasting
p=0.6#Parameter für Fehler
fc=[0, werte[0]]
for i in range(len(werte)-1):
    i=i+1
    a=int(fc[i]+p*(werte[i]-fc[i]))
    fc.append(a)
fc.remove(0)    
print (fc)
print(len(fc), len(werte))

plt.plot(x,fc, linestyle='none', marker='.')


