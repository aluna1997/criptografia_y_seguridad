"""
Created on 9 feb. 2020

@author: felipe, marco
"""

sustitucion = {"G": "E","I": "R","R": "A","D": "M","Y":"U","K":"Y",
               "S":"G","B":"I","L":"T","J":"O","A":"N","P":"H","Q":"L", 
               "Ñ":"P","N":"D","H":"S","O":"V","M":"Q","C":"B","T":"C",
               "W":"F","U":"X","E":"Z","V":"J","X":"W","F":"K" }

def ejercicio_3(nombre_archivo):
    for linea in open(nombre_archivo, "r").readlines():
        resultado = open("resultados/Ejercicio3.txt","w")
        for letra in linea:
            if letra not in sustitucion:
                resultado.write(letra)
            else:
                resultado.write(sustitucion[letra])
    resultado.close()
            

if __name__ == "__main__":
    ejercicio_3("recursos/texto.enc")
                
    