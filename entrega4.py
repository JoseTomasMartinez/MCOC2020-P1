#Jose Tomas Martinez Lavin	
from matplotlib.pylab import *
from scipy.integrate import odeint

m= 1.
f= 1.
chi= 0.2
w= 2.*pi*f
wd= w * sqrt(1.-chi**2)
k= m*w**2
c= 2.*chi*w*m


def eulerint(zp, z0, t, Nsubdivisiones=1):
	Nt = len(t)
	Ndim = len(z0)

	z = zeros((Nt, Ndim))
	z[0,:] = z0[0]
	z[1,:] = z0[1]
	
	#z (i+1) = zp_i *dt + z_i
	for i in range(1, Nt):
		t_anterior = t[i-1]
		dt = (t[i] - t[i-1])/Nsubdivisiones
		z_temp = z[i-1,:].copy()

		for k in range(Nsubdivisiones):
			z_temp += dt * array(zp(z_temp, t_anterior + k*dt))
		z[i,:] = z_temp

	return z


def zp(z,t):
	x,p = z[0], z[1]
	dx = p
	dp = -2 * chi * w * p - w**2*x
	return dx, dp

z0= [1., 1.]
t= linspace(0, 4., 100)

sol= odeint (zp,z0,t)
z_odeint= sol[:,0]

z_analitica = exp(-chi*w*t) * (1.*cos(wd*t) + ((1. + w*chi*1.)/wd) * sin(wd*t) )

sol= eulerint (zp,z0,t)
z_euler1= sol[:,0]

sol= eulerint (zp,z0,t, Nsubdivisiones=10)
z_euler10= sol[:,0]

sol= eulerint (zp,z0,t, Nsubdivisiones=100)
z_euler100= sol[:,0]

plot(t,z_odeint, label="odeint")
plot(t,z_euler1,"g--", label="eulerint1")
plot(t,z_euler10,"r--", label="eulerint10")
plot(t,z_euler100,"--", label="eulerint100")
plot(t,z_analitica, "k",label="analitica", linewidth=2)
legend()
savefig("Entrega4.png")
show()
