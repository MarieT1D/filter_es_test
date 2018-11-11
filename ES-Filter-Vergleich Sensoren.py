import numpy as np
import matplotlib.pyplot as plt
dat1=list(np.loadtxt('es-readings-20180226-20180315-GOOD - Kopie.txt', dtype='unicode_'))
dat2=list(np.loadtxt('entriesG5-20180226bis20180313-BAD - Kopie.txt', dtype='unicode_'))


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
#Daten1
taga1=[]
for j in range(100):
    taga1.append([])
    for i in range(len(zeit1)):
          if zeit1[i]<=(j+2)*24*60 and zeit1[i]>(j+1)*24*60:
            taga1[j].append(zeit1[i]) 
b1=[]
for i in range(len(taga1)):
    b1.append([a1[taga1[i][j]] for j in range(len(taga1[i]))])
    

#Daten2
taga2=[]
for j in range(100):
    taga2.append([])
    for i in range(len(zeit2)):
          if zeit2[i]<=(j+2)*24*60 and zeit2[i]>(j+1)*24*60:
            taga2[j].append(zeit2[i]) 
b2=[]
for i in range(len(taga2)):
    b2.append([a2[taga2[i][j]] for j in range(len(taga2[i]))])
    
    
#Plot
for i in range(13):
    plt.figure()
    plt.plot(taga2[i],b2[i], marker='.', markersize=0.5, linestyle='none', label='G5')
    plt.plot(taga1[i],b1[i], marker='.', markersize=0.5, linestyle='none', label='ES')
    plt.title("Tag"+str(i))
    plt.legend()
    plt.savefig('Vergleich ES G5 - Tag ' +str(i)+ ".pdf") 
    





"""
TO DO:
Gnuplot einrichten http://gnuplot-py.sourceforge.net/
richtige Beschriftung mit richtigem Datum
Monate
"""

"""
Wiedernutzung beachten:
Monate
Anzahl Tage zum Schluss beim Plotten
"""

