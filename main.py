import cv2
import serial
import time
import threading

mensaje = ""
arduino = serial.Serial("COM3", 9600)
hilo=False


def sendMessage():
    global mensaje,hilo,arduino
    while True:
        try: 
            print("\n---------------------")
            print(f"\nHilo 2:\nEnviando: {mensaje}") 
            if(mensaje!=""):
                arduino.write((mensaje.lower()).encode("ascii"))
                time.sleep(1)
            if(hilo):
                break  
        except:
            pass 


# Creamos un metodo donde vamos a pasarle como parametro una imagen
def dectectarCara(imagen,cascadaCara):
    global mensaje
    imagen = cv2.flip(imagen, 1)
    alto, ancho, rgb = imagen.shape
    mitadPantalla = int(ancho/2)
    cv2.line(imagen, pt1=(mitadPantalla, 0), pt2=(
        mitadPantalla, alto), color=(0, 0, 255), thickness=5)
    # Hardcascade lo que hace es crear muchos rectangulos alrededor de la imagen para cada rostro detectado
    rectangulos = cascadaCara.detectMultiScale(imagen)
    # Para todos los rostros detectados
    for (x, y, w, h) in rectangulos:
        # Dibujamos un rectangulo
        cv2.rectangle(imagen, (x, y), (x+w, y+h), (255, 0, 0), 10)
        medio = int(((x+w)+(x))/2)
        fuente = cv2.FONT_ITALIC
        cv2.putText(imagen, text=str(x), org=(x, y), fontFace=fuente,
                    fontScale=1, color=(0, 0, 255), thickness=2, lineType=cv2.LINE_8)
        cv2.putText(imagen, text=str((x+w)), org=(x+w, y), fontFace=fuente,
                    fontScale=1, color=(0, 0, 255), thickness=2, lineType=cv2.LINE_8)
        cv2.putText(imagen, text=str(medio), org=(medio, y+h), fontFace=fuente,
                    fontScale=1, color=(0, 0, 255), thickness=2, lineType=cv2.LINE_8)
        cv2.line(imagen, pt1=(medio, 0), pt2=(
            medio, alto), color=(0, 0, 255), thickness=5)
        aprox = 30
        if(mitadPantalla-aprox <= medio <= mitadPantalla+aprox):
            cv2.putText(imagen, text="Centrado", org=(0, 10), fontFace=fuente,
                        fontScale=1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_8)
            mensaje = "0"
        elif (medio > mitadPantalla):
            cv2.putText(imagen, text="Derecha", org=(0, 10), fontFace=fuente,
                        fontScale=1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_8)
            mensaje = "1"
        elif (medio < mitadPantalla):
            cv2.putText(imagen, text="Izquierda", org=(0, 10), fontFace=fuente,
                        fontScale=1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_8)
            mensaje = "-1"

    return imagen


def main():
    global mensaje,hilo

    captura = cv2.VideoCapture(2)
    cascadaCara = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Usamos hardcascade para analizar la imagen
    # Cargamos el fichero con todos los emparejamientos del rostro
    # https://stackoverflow.com/questions/30508922/error-215-empty-in-function-detectmultiscale
    thread=threading.Thread(target=sendMessage, args=())
    thread.start()
    
    while True:
        resultado, video = captura.read()
        video = dectectarCara(video,cascadaCara)
        cv2.imshow("Detectar Rostros", video)
        tecla = cv2.waitKey(1)
        if tecla == 27:
            hilo=True
            break

    cv2.destroyAllWindows()
    thread.join()
    arduino.write(("end").encode("ascii"))
    arduino.close() 

if __name__ == "__main__":
    main()
