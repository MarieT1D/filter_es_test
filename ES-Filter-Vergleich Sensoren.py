import numpy as np
import matplotlib.pyplot as plt
dat1=list(np.loadtxt('es-readings-20180226-20180315-GOOD - Kopie.txt', dtype='unicode_'))
dat2=list(np.loadtxt('entriesG5-20180226bis20180313-BAD - Kopie.txt', dtype='unicode_'))

#Tag
z=8
#doppelte xDrip Einträge löschen  ( nur ES)
#Daten1
a1=len(dat1)
la1=0
for i in range(a1):    
    if 'xDrip' in dat1[i]:       
        dat1[i]=0
        la1+=1
for i in range(la1):
    dat1.remove(0)
    
#leere Einträge oder ESEL löschen  ( nur G5, xDrip)
#Daten1
a2=len(dat2)
la2=0
for i in range(a2):    
    if len(dat2[i])<=44:       
        dat2[i]=0
        la2+=1
for i in range(la2):
    dat2.remove(0)
    
#Werte 
#Daten1 ES
bz1=[]
zeit1=[]
for i in range(len(dat1)):
    #Zeitskala, m=Monattage
    t=(dat1[i])

    m=28 #Tage im Monat

    monat=int(t[11])
    tag=int(t[13])*10+int(t[14])
    stunde=int(t[16])*10 + int(t[17])
    minute=int(t[19])*10 + int(t[20])

    zeit1.append((monat-2)*28 + tag*24*60 + stunde*60 + minute)

    #BZ-Werte
    if t[-3]==',':
        bz1.append(int(t[-2:]))
    elif t[-4]==',':
        bz1.append(int(t[-3:]))    
a1=dict(zip(zeit1, bz1)) 


#Daten2 xDrip G5
bz2=[]
zeit2=[]
for i in range(len(dat2)):
    #Zeitskala, m=Monattage
    t=(dat2[i])

    m=28 #Tage im Monat
#
    monat=int(t[21])
    tag=int(t[23])*10+int(t[24])
    stunde=int(t[26])*10 + int(t[27])
    minute=int(t[29])*10 + int(t[30])

    zeit2.append((monat-2)*28 + tag*24*60 + stunde*60 + minute)

    #BZ-Werte
    if t[-3]==',':
        bz2.append(int(t[-2:]))
    elif t[-4]==',':
        bz2.append(int(t[-3:]))    
a2=dict(zip(zeit2, bz2)) 


#Daten auftrennen nach Datum
#Tage erstellen
#Daten1 ES
taga1=[]
for j in range(100):
    taga1.append([])
    for i in range(len(zeit1)):
          if zeit1[i]<=(j+2)*24*60 and zeit1[i]>(j+1)*24*60:
            taga1[j].append(zeit1[i]) 
b1=[]
for i in range(len(taga1)):
    b1.append([a1[taga1[i][j]] for j in range(len(taga1[i]))])
    

#Daten2 G5
taga2=[]
for j in range(100):
    taga2.append([])
    for i in range(len(zeit2)):
          if zeit2[i]<=(j+2)*24*60 and zeit2[i]>(j+1)*24*60:
            taga2[j].append(zeit2[i]) 
b2=[]
for i in range(len(taga2)):
    b2.append([int(a2[taga2[i][j]]) for j in range(len(taga2[i]))])
    

    
#Filter Daten1 ES 
p=0.2 #Parameter für Stärke des Filters
fc=[b1[z][0]]

for i in range(len(b1[z])-1):
    a=int(fc[i]+p*(b1[z][i]-fc[i]))
    fc.append(a)
    
"""#Filter Daten2 ???Bernhard???? aber irgendwie habe ich da einen Fehler drinnen
pb=0.2 #Parameter für Stärke des Filters
ffc=[b1[z][0]]

for i in range(len(b1[z])-1):
    a=(pb*b1[9][i]+(1-pb)*(ffc[i]))
    ffc.append(a)"""
    


#15 min average
av=([b1[z][0],b1[z][1]])
for i in range(len(b1[z])-2):
    a=(b1[z][i]+b1[z][i+1]+b1[z][i+2])/3
    av.append(a)




#Plot Tag 9
print(b1[z])
print(fc)
marker=0.5  #Punktgroesse
plt.figure()
plt.plot(taga2[z],b2[z], marker='.', linestyle='none', label='G5', markersize=marker)
plt.plot(taga1[z],b1[z], marker='.', linestyle='none', label='ES', markersize=marker)
"""plt.plot(taga1[z],ffc, linestyle='none', marker='.', label='filtered ES, pb=' + str(pb), markersize=marker)"""
plt.plot(taga1[z],fc, linestyle='none', marker='.', label='filtered ES, p=' + str(p), markersize=marker)
plt.plot((taga1[z]),av, linestyle='none', marker='.', label='15 min delta ES', markersize=marker)
plt.title("Tag"+str(z))
plt.legend()
plt.show()

plt.savefig('ES-G5  '+str(p)+'tag' + str(z)+'.pdf') 



