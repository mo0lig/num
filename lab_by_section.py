import numpy as np
import matplotlib.pyplot as plt

def gx(n): #function of our equation
    return (n**3 + 12*n -12)

fig,ax=plt.subplots()
ax.set_xlim((-15,15)) # interval of x axis
ax.set_ylim((-50,50)) # interval of y axis
ax.grid() #setka
ax.set_xlabel("x")
ax.set_ylabel("y")
x = np.linspace(-50,50,100) 
ax.plot(x,x**3 +12*x - 12,label=r'$f(x)=\ x^3 +12*x -12$')
ax.legend(loc='best', fontsize=8)
plt.savefig('figure_with_legend.png')
plt.show()

a=int(input("initial point:"))#value of initial x coordinate
b=int(input("final point:"))#value of final x coordinate
s=True
i=1
while s==True:
    if (gx(a)>=0 and gx(b)>=0) or (gx(a)<0 and gx(b)<0): #By this condition we can find out whether there roots in a given user interval
        print("a or b is not in correct interval") 
        break
    else: 
        c=(a+b)/2
        if gx(a)*gx(c)<0: 
            b=c
            if abs(c-a)<0.01:
                s=False
        else:
            a=c
            if abs(c-b)<0.01:
                s=False
    print("Iteration-" + str(i),"x"+str(i)+"="+str(round(c,4)))
    i+=1