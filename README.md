![myimage-alt-tag](https://github.com/JoseTomasMartinez/MCOC2020-P1/blob/master/Trayectoria%20para%20distintos%20vientos.png)
# Entrega 5
* P1. Utilizando la función leer_eof.py se pudieron determinar las coordenadas de cada posición en todos los tiempos. Luego, con los metodos odeint y eulerint se predijo la orbita utilizando las primeras coordenadas del archivo con los datos reales. Los gráficos quedan de la siguiente forma:

![myimage-alt-tag](https://github.com/JoseTomasMartinez/MCOC2020-P1/blob/master/P1%20Vector%20de%20Estado%20(X%2CY%2CZ).png)

 La línea naranja se sobrepone a la azul que apenas se nota. La naranja corresponde a la predicción del metodo odeint. Se nota que es muy preciso. Por otro lado, la línea verde representa la predicción hecha con el método de euler (utilizando una subdivision). Se ve claramente que el método de euler es bastante impreciso. 

* P2. La deriva en el tiempo final de la prediccion realizada con eulerint comparada con la realizada con odeint en kilometros es en 19303.El gráfico de la deriva en todos los tiempos es el siguiente:

![myimage-alt-tag](https://github.com/JoseTomasMartinez/MCOC2020-P1/blob/master/Deriva%20entre%20predicciones%20Euler%20y%20Odeint.png)

* El metodo odeint demora aproximadamente 0,3 segundos, mientras que el de eulerint demora 0,9 (considerando una subdivision)

* P3. Se tomó el último punto para determinar el error. Sin embargo, para 100 subdivisiones el error era altísimo y se demoró mas de una hora en ser calculado. Por lo que era muy dificil saber cuantas subdivisiones se debían hacer.

 Desde aquí la parte que no fue agregada la primera vez que se entregó
* P4. Se logra implementar J2 y J3, reduciendo la deriva a 7000 km aproximadamente.

![myimage-alt-tag](https://github.com/JoseTomasMartinez/MCOC2020-P1/blob/master/Deriva%20entre%20predicciones%20Euler%20y%20Odeint%20J2%20y%20J3.png)

El programa demora 13.9 segundos en correr.
* Para la última entrega no hay antecedentes, por lo que la entrega 7 es la primera y última. No hubo trials.
