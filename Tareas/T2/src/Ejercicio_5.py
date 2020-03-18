"""
Luna Felipe
Marco Antonio Hurtado
"""

import base64

def ejercicio_5(ruta_img):
    img_b64 = open(ruta_img,'rb').read()
    img_decode = base64.decodestring(img_b64)
    resultado = open('resultados/ejercicio_5.png','wb')
    resultado.write(img_decode)
    resultado.close()

if __name__ == '__main__':
    ejercicio_5('../recursos/img_5.txt')