# Detección de Movimiento 
import cv2
import numpy as np

# Activamos la camara para la captura de video
video = cv2.VideoCapture(0)

# Inicializamos un contador para tomar la imagen de fondo
i = 0
# Almacenamos todas las imagenes del video en la variable frame y en caso de que no pueda 
# tomar una imagen se rompe el bucle while
while True:
  ret, frame = video.read()
  if ret == False: break
  # Las imagenes capturadas del video se pasan a escala de grises
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  # Nos quedamos con la veinteava imagen de fondo para evitar problemas con la camara 
  if i == 20:
    bgGray = gray
  # Pasada la veinteava iteracion ahora se restaran la imagen de fondo y la actual
  # con la funcion cv2.absdiff, de esta manera podremos saber que se encuentra en 
  # movimiento
  if i > 20:
    dif = cv2.absdiff(gray, bgGray)
    # Aplicamos umbralización simple, es decir, transformar a binaria la imagen
    # en blanco y negro, si el pixel supera los 40 se le asignara 255 haciendo 
    # lo que se este movimiento se convierta en un pixel totalmente blanco
    _, th = cv2.threshold(dif, 40, 255, cv2.THRESH_BINARY)
    # Para OpenCV 3
    #_, cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Para OpenCV 4
    # Con la funcion cv2.findContours encontramos los contornos, en este caso esas
    # areas blancas
    cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, cnts, -1, (0,0,255),2)        
    
    for c in cnts:
      area = cv2.contourArea(c)
      if area > 9000:
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)

  cv2.imshow('Frame',frame)

  i = i+1
  if cv2.waitKey(30) & 0xFF == ord ('q'):
    break
video.release()