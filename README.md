# SeguimientoRostrosArduino
El proyecto se basa en un dispositivo capaz de seguir un rostro haciendo uso de una cámara, gestionado en Arduino.
Nuestro proyecto crea una comunicación entre Python y Arduino, con la finalidad de que Python haga la detección facial y el análisis, este se lo comunicará a Arduino que a su vez iniciará un protocolo de rotación de un servomotor.
## Sobre El Proyecto
Para el desarrollo de nuestro proyecto usamos una placa Arduino UNO, el IDE de Arduino y Visual Studio Code para la programación en Python.
### El proyecto hace uso de las siguentes tecnologías.
#### Para Arduino UNO:
```
C++
Servo
```
#### Para el seguimiento de rostros:
```
Python 
OpenCV
```
#### Para la comunicación entre Python y Arduino:
```
Threading
Pyserial
```
