'''
Created on 9 feb. 2020

@author: felipe, marco
'''

sustitucion = { "A":"N",
               "B":"I",
               "C":"B",
               "D":"M",
               "E":"",
               "F":"",
               "G":"E",
               "H":"S",
               "I":"R",
               "J":"O",
               "K":"Y",
               "L":"T",
               "M":"Q",
               "N":"D",
               "O":"V",
               "P":"H",
               "Q":"L",
               "R":"A",
               "S":"",
               "T":"C",
               "U":"X",
               "V":"J",
               "W":"F",
               "X":"",
               "Y":"U",
               "Z":""}

def descifra_texto(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    for linea in archivo.readlines():
        resultado = open("resultados/ejercicio3.txt","w")
        for letra in linea:
            if letra not in sustitucion:
                resultado.write(letra)
            else:
                resultado.write(sustitucion[letra])
    resultado.close()
            

if __name__ == "__main__":
    descifra_texto("recursos/texto.enc")
                
    