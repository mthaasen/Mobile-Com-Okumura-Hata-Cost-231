# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import math
from math import log10

cm=3
hm=1.5
ahm=(3.2*log10(11.75*hm)**2)-4.97
fc=1950
range=[1,2,3]
A=np.arange(30,101,1)
List1=[]
List2=[]
List3=[]

for hb in A:
    Lp1=46.3+33.9*(log10(fc))-13.82*(log10(hb))-ahm+(44.9-6.55*log10(hb))*(log10(range[0]))+cm
    List1.append(Lp1)
    Lp2=46.3+33.9*(log10(fc))-13.82*(log10(hb))-ahm+(44.9-6.55*log10(hb))*(log10(range[1]))+cm
    List2.append(Lp2)
    Lp3=46.3+33.9*(log10(fc))-13.82*(log10(hb))-ahm+(44.9-6.55*log10(hb))*(log10(range[2]))+cm
    List3.append(Lp3)

print(List1)
print(List2)
print(List3)

plt.title("Mobile Communication Homework 2")
plt.xlabel("Range(km)")
plt.ylabel("Path Loss(dB)")
plt.grid(True)
plt.plot(A, List1, color = 'r', label = "Range=1km Cost 231")
plt.plot(A, List2, color = 'g', label = "Range=2km Cost 231")
plt.plot(A, List3, color = 'b', label = "Range=3km Cost 231")
plt.legend(loc = "lower right")
plt.show()