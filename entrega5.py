#Jose Tomas Martinez Lavin	
from matplotlib.pylab import *
from scipy.integrate import odeint
from leer_eof import leer_eof
from time import perf_counter

hr=3600. #s
km= 1000. #m
km5= 1000**5
rt=6371*km #kms radio tierra
mt=5.972e24 #masa tierra kg
w=2*pi/86400. #velocidad angular tierra
G=6.674e-11  #cte gravitatoria
Fgmax=G*mt/rt**2
J2= 1.75553e10*km5 #km5 / s2

def eulerint(zp, z0, t, Nsubdivisiones=1):
	Nt = len(t)
	Ndim = len(z0)

	z = zeros((Nt, Ndim))
	z[0,:] = z0

	#z (i+1) = zp_i *dt + z_i
	for i in range(1, Nt):
		t_anterior = t[i-1]
		dt = (t[i] - t[i-1])/Nsubdivisiones
		z_temp = z[i-1,:].copy()
		for k in range(Nsubdivisiones):
			z_temp += dt * zp(z_temp, t_anterior + k*dt)
		z[i,:] = z_temp

	return z

def satelite(z,t):
	zp=zeros(6)
	R=array([[cos(w*t),-sin(w*t),0],[sin(w*t),cos(w*t),0],[0,0,1]])
	Rp=array([[-sin(w*t),-cos(w*t),0],[cos(w*t),-sin(w*t),0],[0,0,0]])*w
	Rdp=array([[-cos(w*t),sin(w*t),0],[-sin(w*t),-cos(w*t),0],[0,0,0]])*w**2
	
	z1=z[0:3]
	z2=z[3:6]
	r2=dot(z1,z1)
	r=sqrt(r2)
	Fg=(-G*mt/r**3) * z1
	
	zp[0:3]= z2
	zp[3:6]= Fg-R.T@(Rdp@z1+2*Rp@z2)

	return zp

def sateliteJ2(z,t):
	zp=zeros(6)
	R=array([[cos(w*t),-sin(w*t),0],[sin(w*t),cos(w*t),0],[0,0,1]])
	Rp=array([[-sin(w*t),-cos(w*t),0],[cos(w*t),-sin(w*t),0],[0,0,0]])*w
	Rdp=array([[-cos(w*t),sin(w*t),0],[-sin(w*t),-cos(w*t),0],[0,0,0]])*w**2
	
	z1=z[0:3]
	z2=z[3:6]
	r2=dot(z1,z1)
	r=sqrt(r2)
	Fg=((-G*mt/r**3) * (J2/r**7)) * (6*(z1[2]**2) - 0.5*((z1[0]**2) + (z1[1]**2))) * z1
	
	zp[0:3]= z2
	zp[3:6]= Fg-R.T@(Rdp@z1+2*Rp@z2)

	return zp

t, x, y, z, vx, vy, vz = leer_eof("S1A_OPER_AUX_POEORB_OPOD_20200818T121207_V20200728T225942_20200730T005942.EOF")

z0=array([x[0],y[0],z[0],vx[0],vy[0],vz[0]])
zf_real=array([x[-1],y[-1],z[-1],vx[-1],vy[-1],vz[-1]])

pc1=perf_counter()
sol_odeint=odeint(satelite,z0,t)
pc2=perf_counter()
sol_eulerint=eulerint(satelite,z0,t)
pc3=perf_counter()

t_odeint = pc2-pc1
t_euler = pc3-pc2
print ("Odeint demora: " + str(t_odeint))
print ("Eulerint demora: " + str(t_euler))

for i in range(len(t)):
	t[i]/=hr
	x[i]/=km
	y[i]/=km
	z[i]/=km
	vx[i]/=km
	vy[i]/=km
	vz[i]/=km
	sol_odeint[i,0]/=km
	sol_odeint[i,1]/=km
	sol_odeint[i,2]/=km
	sol_odeint[i,3]/=km
	sol_odeint[i,4]/=km
	sol_odeint[i,5]/=km
	sol_eulerint[i,0]/=km
	sol_eulerint[i,1]/=km
	sol_eulerint[i,2]/=km
	sol_eulerint[i,3]/=km
	sol_eulerint[i,4]/=km
	sol_eulerint[i,5]/=km


Dpfr_odeint=zf_real - sol_odeint[-1] #Diferencia entre posicion final real y prediccion odeint
Dpfr_eulerint=zf_real - sol_eulerint[-1] #Diferencia entre posicion final real y prediccion euler
Dpfr_ode_euler=sol_eulerint[-1] - sol_odeint[-1] #Diferencia entre predicciones

posicion_odeint=Dpfr_odeint[0:3]
posicion_eulerint=Dpfr_eulerint[0:3]
posicion_ode_euler=Dpfr_ode_euler[0:3]


#P1

subplot(3,1,1)
ylabel("X (KM)")
title("Posicion")
plot(t,x)
#plot(t,sol_odeint[:,0])
plot(t,sol_eulerint[:,0])

subplot(3,1,2)
ylabel("Y (KM)")
plot(t,y)
#plot(t,sol_odeint[:,1])
plot(t,sol_eulerint[:,1])

subplot(3,1,3)
ylabel("Z (KM)")
xlabel("Tiempo, t (horas)")
plot(t,z)	
#plot(t,sol_odeint[:,2])
plot(t,sol_eulerint[:,2])
savefig("P1 Vector de Estado (X,Y,Z)")
show()



"""
# P2 
Deriva_ode_euler=[]
for i in range(len(t)):
	D=sol_odeint[i,0:3] - sol_eulerint[i,0:3]
	Deriva_ode_euler.append(norm(D))

plot(t,Deriva_ode_euler)
title((r'Distancia entre predicciones euler y odeint $\delta_{max}$ = ') + str(int(Deriva_ode_euler[-1])) + "(km)")
ylabel(r'Deriva, $\delta$ (KM)')
xlabel("Tiempo, t(horas)")
savefig("Deriva entre predicciones Euler y Odeint")
show()

npe=norm(posicion_eulerint) #norma posicion final euler
npr=norm(array([x[-1],y[-1],z[-1]])) #norma posicion final real
Error_euler=abs(npr-npe)/npr*100
print (Error_euler)"""


sol_eulerintJ2=eulerint(sateliteJ2,z0,t)

for i in range(len(t)):
	sol_eulerintJ2[i,0]/=km
	sol_eulerintJ2[i,1]/=km
	sol_eulerintJ2[i,2]/=km



subplot(3,1,1)
ylabel("X (KM)")
title("Posicion")
plot(t,x)
plot(t,sol_eulerintJ2[:,0])

subplot(3,1,2)
ylabel("Y (KM)")
plot(t,y)
plot(t,sol_eulerintJ2[:,1])

subplot(3,1,3)
ylabel("Z (KM)")
xlabel("Tiempo, t (horas)")
plot(t,z)	
plot(t,sol_eulerintJ2[:,2])
#savefig("P1 Vector de Estado (X,Y,Z)")
show()