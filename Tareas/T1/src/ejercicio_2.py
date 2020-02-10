'''
Created on 9 feb. 2020

@author: felipe,marco
'''
sustitucion = { "A":"W","B":"P","C":"U","D":"B","E":"A","F":"Q","G":"O",
                    "H":"Y","I":"G","J":"C","K":"Z","L":"E","M":"F","N":"M",
                    "O":"J","P":"V","Q":"D","R":"K","S":"I","T":"R","U":"H",
                    "V":"L","W":"T","X":"S","Y":"N","Z":"X"}


def get_key(val, dic): 
    for key, value in dic.items(): 
        if val == value: 
            return key 
  
    return "key doesn't exist"

def a(mensaje):
    resultado = ""
    for letra in mensaje.replace(" ","").upper():
        resultado += sustitucion.get(letra)
    print(resultado)
    
def c(mensaje):
    resultado = ""
    for letra in mensaje.replace(" ","").upper():
        resultado += get_key(letra, sustitucion)
    print(resultado)
        
        
if __name__ == "__main__":
    a("Criptografia y seguridad")
    c("RGFGMOWRRWUZIWKAWIGOMGQGUWMRRYKAWRRJUKNVRJGFVEAFAMRWRGJMI")