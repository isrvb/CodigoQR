#Convertidor de texto a Imagen QR/QR

import qrcode
from PIL import Image

cadena = input("Ingrese el texto para el Codigo QR: ")
imagen = qrcode.make(cadena)

nombre_imagen = input("Ingrese el nombre de la Imagen: ") + '.png'
archivo_imagen = open(nombre_imagen,'wb')
imagen.save(archivo_imagen)
archivo_imagen.close()

ruta_imagen = './'+nombre_imagen
Imagen.open(ruta_imagen).show()

#VB
