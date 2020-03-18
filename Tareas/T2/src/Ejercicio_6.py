"""
Luna Felipe
Marco Antonio Hurtado
"""
import base64

def ejercicio_6():
    cinta = open("../recursos/cinta_aleatoria.txt","rb").read()
    cinta_decode = base64.b64decode(cinta)
    cinta_bytes = bytearray(cinta_decode)
    
    img = open("../recursos/imagen.png","rb").read()
    img_bytes = bytearray(img)
    
    
    if len(cinta_bytes) == len(img_bytes):
        print "Las longitudes son iguales!"
    
        resultado = open("resultados/resultado.mp3",'wb')
        
        for b in range(len(cinta_bytes)):
            resultado.write(chr(cinta_bytes[b] ^ img_bytes[b]))
    
    resultado.close()    
    
if __name__ == "__main__":
    ejercicio_6()
        
        