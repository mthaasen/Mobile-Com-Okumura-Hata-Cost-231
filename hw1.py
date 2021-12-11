# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import math
from math import log10

cm=3
hb=30
hm=1.5
ahm=(3.2*log10(11.75*hm)**2)-4.97

fc=[450,900,1800,1950]

range=np.arange(1,8,0.3)
List1=[]
List2=[]
List3=[]
List4=[]

for R in range:
    Lp1=69.5+26.16*(log10(fc[0]))-13.82*(log10(hb))-ahm+(44.9-6.55*log10(hb))*(log10(R))
    List1.append(Lp1)
    Lp2=69.5+26.16*(log10(fc[1]))-13.82*(log10(hb))-ahm+(44.9-6.55*log10(hb))*(log10(R))
    List2.append(Lp2)
    Lp3=46.3+33.9*(log10(fc[2]))-13.82*(log10(hb))-ahm+(44.9-6.55*log10(hb))*(log10(R))+cm
    List3.append(Lp3)
    Lp4=46.3+33.9*(log10(fc[3]))-13.82*(log10(hb))-ahm+(44.9-6.55*log10(hb))*(log10(R))+cm
    List4.append(Lp4)

print(List1)
print(List2)
print(List3)
print(List4)
print(ahm)

plt.title("Mobile Communication Homework 1")
plt.xlabel("Range(km)")
plt.ylabel("Path Loss(dB)")
plt.grid(True)
plt.plot(range, List1, color = 'r', label = "450MHz Okumura-Hata")
plt.plot(range, List2, color = 'g', label = "900MHz Okumura-Hata")
plt.plot(range, List3, color = 'b', label = "1800MHz Cost 231")
plt.plot(range, List4, color = 'purple', label = "1950MHz Cost 231")
plt.legend(loc = "lower right")
plt.show()