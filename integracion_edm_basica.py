#Jose Tomas Martinez Lavin
import scipy as sp
from scipy.integrate import odeint
from numpy import *

rt=6371 #kms radio tierra
G=6.674e-11 #cte gravitatoria
mt=5.9736e24 #masa tierra
dts=700 #kms distancia tierra satelite

t=linspace(0,30,1001)
w=2*pi/86400 #velocidad angular tierra
vt=w*(rt+dts)
z0=array([rt+dts,0,0,0,vt,0])



def satelite(z,t):
	zp=zeros(6)
	R=array([[cos(w*t),-sin(w*t),0],[sin(w*t),cos(w*t),0],[0,0,1]])
	Rp=array([[-sin(w*t),-cos(w*t),0],[cos(w*t),-sin(w*t),0],[0,0,0]])
	Rdp=array([[-cos(w*t),sin(w*t),0],[-sin(w*t),-cos(w*t),0],[0,0,0]])
	
	zp[0:3]= z[3:6]
	zp[3:6]=(((-G*mt)/rt**3)*z[0:3])-(R.T)@(Rdp@z[0:3]+2*Rp@z[3:6])
	return zp
sol=odeint(satelite,z0,t)
x= sol[:,0]
y= sol[:,1]
z= sol[:,2]

import matplotlib.pylab as plt

plt.plot(x,y)

plt.show()

