![myimage-alt-tag](https://github.com/JoseTomasMartinez/MCOC2020-P1/blob/master/Trayectoria%20para%20distintos%20vientos.png)
# Entrega 5
* P1. Utilizando la función leer_eof.py se pudieron determinar las coordenadas de cada posición en todos los tiempos. Luego, con los metodos odeint y eulerint se predijo la orbita utilizando las primeras coordenadas del archivo con los datos reales. Los gráficos quedan de la siguiente forma:

![myimage-alt-tag](https://github.com/JoseTomasMartinez/MCOC2020-P1/blob/master/P1%20Vector%20de%20Estado%20(X%2CY%2CZ).png)
 La línea naranja se sobrepone a la azul que apenas se nota. La naranja corresponde a la predicción del metodo odeint. Se nota que es muy preciso. Por otro lado, la línea verde representa la predicción hecha con el método de euler (utilizando una subdivision). Se ve claramente que el método de euler es bastante impreciso. 

* P2. La deriva en el tiempo final de la prediccion realizada con eulerint comparada con la realizada con odeint en kilometros es en 19303.El gráfico de la deriva en todos los tiempos es el siguiente:

![myimage-alt-tag](https://github.com/JoseTomasMartinez/MCOC2020-P1/blob/master/Deriva%20entre%20predicciones%20Euler%20y%20Odeint.png)

* El metodo odeint demora aproximadamente 0,3 segundos, mientras que el de eulerint demora 0,9 (considerando una subdivision)





