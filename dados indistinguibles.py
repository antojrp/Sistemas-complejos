# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:13:37 maxi24

@author: ajrp
"""



from matplotlib import pyplot as plt
import numpy as np
import scipy as sp
from sklearn.metrics import r2_score 


"""
First I define a function to obtain the number of combinations of a number of 
of N dice that add up to a value S. 
The following parameters are passed to the function:
    N=number of dice
    n=number of dice (will be used for recursion)
    S=sum of the dice values
    j=start at 1, needed for recursion
    comb=empty vector of the size of the number of dice
    cont=will be the counter of the combinations, start at 0

Translated with DeepL.com (free version)
"""

def combination(N,n,S,j,comb,cont):
                   
   if n==0:
      if sum(comb)==S:
          cont=cont+1

      
      return cont
       
   else:
      for i in range(j,7):
          comb[N-n]=i
          cont=combination(N,n-1,S,i,comb,cont)
          
      return cont
         
  
    
  
maxi=50 #the maximum number of dice up to which the combinations will be calculated (maxi).
x1=list(range(1,maxi+1))
y=[0]*(maxi)
z=[0]*(maxi)

for i in range(1,maxi+1):
    comb=[0]*i
    S=int(3.5*i)
    y[i-1]=combination(i,i,S,1,comb,0)
    z[i-1]=np.log(y[i-1])
    
"""Plot of the entropy as a function of the number of dice"""
plt.figure()
plt.scatter(x1,z, color='purple',s=5)
plt.xlabel('Number of dice')
plt.ylabel('Entropy')
plt.title('Entropy of the macrostate with higher entropy')
plt.show()
    


"""Fitting of the results obtained to a function of the type a*ln(x)**b"""
def f1(x,a,b):
    return a*(np.log(x))**b
x2=np.linspace(1,maxi)
p1,p2=sp.optimize.curve_fit(f1,x1,z)
a,b=p1
r2 = r2_score(z, f1(x1,a,b))

plt.figure()
plt.plot(x2,f1(x2,a,b),color="#F4C2C2",label='Fitted curve',zorder=5)
plt.scatter(x1,z,color='purple',label='Numerical calculations',s=5,zorder=10)
plt.xlabel('Number of dice')
plt.ylabel('Entropy')
plt.title('Regression of numerical calculations.\n f(x)= '+str(round(a,3))+'$\cdot$ln(x)$^{'+str(round(b,3))+'}$,  R$^2$= '+str(round(r2,5)))
plt.legend(loc='upper left')
plt.show()

