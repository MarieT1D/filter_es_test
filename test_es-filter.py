import numpy as np
import matplotlib.pyplot as plt

daten=np.loadtxt("Daten 2.txt", dtype='unicode_')


werte=np.array(daten, dtype=int)


x=np.zeros_like(werte)
for i in range(len(x)):
    x[i]=i*5
print(werte,x)


#forecasting
p=0.6 #Parameter für Stärke des Filters
fc=[werte[0]]
for i in range(len(werte)-1):
    a=int(fc[i]+p*(werte[i]-fc[i]))
    fc.append(a)
    
#15 min average
av=[werte[0],werte[1]]
for i in range(len(werte)-2):
    a=int((werte[i]+werte[i+1]+werte[i+2])/3)
    av.append(a)
 
  


plt.plot(x,werte, linestyle='none', marker='.', label='origin')
plt.plot(x,fc, linestyle='none', marker='.', label='filtered, p=' + str(p))
plt.plot(x,av, linestyle='none', marker='.', label='15 min delta')
plt.legend()
plt.show()

