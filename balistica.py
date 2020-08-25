#Jose Tomas Martinez Lavin
import scipy as sp
from scipy.integrate import odeint
from numpy import *

# Unidades base
cm=0.01 #m
inch=2.54*cm
g=9.81 #m/s2

# Coeficiente de arrastre
rho=1.225 #kg/m3
cd=0.47
D=8.5*inch
r=D/2
A=sp.pi * r**2
CD=0.5*rho*cd*A

#Masa
m=15. #kg

#Viento
V= [0.,10.,20.] #m/s

# Funcion a integrar
# z es vector de estado
# z = [x,y,vx,vy]
# dz/dt = bala(z,t)
#         [ z2       ]
# dz/dt = [          ] (modelo) 
#		  [ FD/m -g  ]	

# Vector de estado
# z[0]  -> x
# z[1]  -> y
# z[2]  -> vx
# z[3]  -> vy

#vector de tiempo
t=linspace(0,30,1001)
# Parte en el origen y tiene vx=vy=2 m/s
vi=100*1000./3600.
z0=array([0,0,vi,vi])

for i in range(len(V)):
	def bala(z,t):
		zp=zeros(4)

		zp[0]= z[2]
		zp[1]= z[3]

		v= z[2:4] #saca las ultimas dos componentes
		v[0]= v[0]-V[i]
		v2= dot(v,v)
		vnorm= sqrt(v2)
		FD= -CD*v2*(v/vnorm)
		zp[2]= FD[0] / m
		zp[3]= FD[1] / m-g
		return zp
	if V[i]==0.:
		sol=odeint(bala,z0,t)
	elif V[i]==10.:
		sol1=odeint(bala,z0,t)
	else:
		sol2=odeint(bala,z0,t)	


import matplotlib.pylab as plt

x= sol[:,0]
y= sol[:,1]
x1= sol1[:,0]
y1= sol1[:,1]
x2= sol2[:,0]
y2= sol2[:,1]

plt.plot(x,y,label="$V$ = 0 m/s")
plt.plot(x1,y1,label="$V$ = 10.0 m/s")
plt.plot(x2,y2,label="$V$ = 20.0 m/s")
plt.ylim(0,50)
plt.xlim(0,150)
plt.grid()
plt.title("Trayectoria para distintos vientos")
plt.ylabel("Y(m)")
plt.xlabel("X(m)")
plt.legend()
plt.savefig("Trayectoria para distintos vientos.png")	
