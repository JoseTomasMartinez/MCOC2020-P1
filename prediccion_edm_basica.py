#Jose Tomas Martinez Lavin
#http://aux.sentinel1.eo.esa.int/POEORB/2020/08/18/S1A_OPER_AUX_POEORB_OPOD_20200818T121207_V20200728T225942_20200730T005942.EOF
from matplotlib.pylab import *
from scipy.integrate import odeint
from numpy import *

hr=3600 #s
km= 1000 #mt
rt=6371*km#kms radio tierra
mt=5.972e24 #masa tierra kg
w=2*pi/86400 #velocidad angular tierra
G=6.674e-11 #cte gravitatoria
H0=700*km #kms distancia tierra satelite
Fgmax=G*mt/rt**2


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

#t=linspace(0,5*hr,1001) #prueba entrega anterior
#x0=rt+H0 #prueba entrega anterior
#vt=6830 #6830 #prueba entrega anterior


#Datos satelite inicial
xi= -2089508.529110
yi= 6353851.350975
zi= 2302249.620335
vxi= 778.560405
vyi= 2809.774736
vzi= -7015.920114

#Datos satelite final
xf= -1029864.551062
yf= 35526.865598
zf= 6989883.772777
vxf= 1865.653900
vyf= 7345.588540
vzf= 237.088688

#Delta tiempo
import datetime as dt

utc_EOF_format= "%Y-%m-%dT%H:%M:%S.%f"
ti= dt.datetime.strptime("2020-07-28T22:59:42.000000",utc_EOF_format)
tf= dt.datetime.strptime("2020-07-30T00:59:42.000000",utc_EOF_format)
intervalo_segundos=(tf-ti).total_seconds()

t=linspace(0,intervalo_segundos,9361)
z0=array([xi,yi,zi,vxi,vyi,vzi])

sol=odeint(satelite,z0,t)
x= sol[:,:]
Dpfr=array([xf,yf,zf,vxf,vyf,vzf]) - sol[-1] #Diferencia entre prediccion y posicion final real

posicion=Dpfr[0:3]
print("La diferencia en metros entre el vector final predicho y el real es: "+ str(norm(posicion)))


"""
Datos iniciales
 <UTC>UTC=2020-07-28T22:59:42.000000</UTC>
      <UT1>UT1=2020-07-28T22:59:41.788840</UT1>
      <Absolute_Orbit>+33661</Absolute_Orbit>
      <X unit="m">-2089508.529110</X>
      <Y unit="m">6353851.350975</Y>
      <Z unit="m">2302249.620335</Z>
      <VX unit="m/s">778.560405</VX>
      <VY unit="m/s">2809.774736</VY>
      <VZ unit="m/s">-7015.920114</VZ>

Datos finales
<UTC>UTC=2020-07-30T00:59:42.000000</UTC>
      <UT1>UT1=2020-07-30T00:59:41.789813</UT1>
      <Absolute_Orbit>+33677</Absolute_Orbit>
      <X unit="m">-1029864.551062</X>
      <Y unit="m">35526.865598</Y>
      <Z unit="m">6989883.772777</Z>
      <VX unit="m/s">1865.653900</VX>
      <VY unit="m/s">7345.588540</VY>
      <VZ unit="m/s">237.088688</VZ>