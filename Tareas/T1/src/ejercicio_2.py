'''
Created on 9 feb. 2020

@author: felipe,marco
'''
sustitucion = {"A":"W","B":"P","C":"U","D":"B","E":"A","F":"Q","G":"O",
               "H":"Y","I":"G","J":"C","K":"Z","L":"E","M":"F","N":"M",
               "O":"J","P":"V","Q":"D","R":"K","S":"I","T":"R","U":"H",
               "V":"L","W":"T","X":"S","Y":"N","Z":"X"}


def get_key(valor, dic): 
    for llave, value in dic.items(): 
        if valor == value: 
            return llave 
    return None

def ejercicio_2_a(mensaje):
    resultado = ""
    for letra in mensaje.replace(" ","").upper():
        resultado += sustitucion.get(letra)
    print(resultado)
    
def ejercicio_2_c(mensaje):
    resultado = ""
    for letra in mensaje.replace(" ","").upper():
        resultado += get_key(letra, sustitucion)
    print(resultado)
        
        
if __name__ == "__main__":
    ejercicio_2_a("Criptografia y seguridad")
    ejercicio_2_c("RGFGMOWRRWUZIWKAWIGOMGQGUWMRRYKAWRRJUKNVRJGFVEAFAMRWRGJMI")