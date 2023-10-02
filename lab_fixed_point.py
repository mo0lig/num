import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots()
ax.set_xlim((-5,5)) # interval of x axis
ax.set_ylim((-10,10)) # interval of y axis
ax.grid() #setka
ax.set_xlabel("x")
ax.set_ylabel("y")
x = np.linspace(-50,50,100) 
ax.plot(x,(12-x**3)/12, label=r'$g(x)=\ (12-x^3)/12$')
ax.plot(x,x, label=r'$y=\ x$')
ax.legend(loc='best', fontsize=8)
plt.savefig('figure_with_legend.png')
plt.show()

def fx(x):
    return x**3 +12*x - 12
def gx(x): #function of our equation
    return (12-x**3)/12
def gx_derivative(x):
    return (x**2 * (-1))/4

a=int(input("initial point:"))#value of initial x coordinate
b=int(input("final point:"))#value of final x coordinate
s=True

if fx(a)*fx(b)<0:
    if gx(a)>gx(b):
        print("Function g(x) is decreasing on ["+str(a)+"," +str(b)+"]")
    if gx_derivative(a)<1 and gx_derivative(b)<1:
        print("Function g(x) has fixed point on ["+str(a)+"," +str(b)+"]")
    nn=int(input("Number of needed iteration:"))
    i=1
    vv=True
    while vv:
        s=int(input("Enter required number to guess from your interval:"))
        if s==a or s==b:
            vv=False
        else:
            print("this number is not in our interval")  
    while i-1!=nn:
        s=gx(s)
        print("Iteration-"+str(i)+" x"+str(i)+"="+str(round(s,4)))
        i+=1
    print("error:",abs(fx(s)))
else:
    print("Your function don't have fixed-point in your entered interval6 please,try again")