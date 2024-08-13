cadena="El Monte Everest, la montaña más alta del mundo con una altitud de 8,848 metros, no está completamente inmóvil. Debido a la colisión de las placas tectónicas indoaustraliana y eurasiática, el Everest sigue aumentando de altura a una tasa de aproximadamente 4 milímetros por año. Además, los terremotos pueden afectar su altura, como ocurrió en el terremoto de Nepal de 2015, que redujo su altura en unos pocos centímetros."

clave="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-=_+[]|;:',.<>?/~`"

# El problema consiste en lo siguiente: 
# 1. Crea una función caracteres_distintos(cadena): que identifique todos los caracteres distintos del str guardado en la variable 'cadena' y los guarde en una nueva lista.
# 2. Convierte la es str 'clave' en una lista, lista_clave.
# 3. crea una función que reemplace cada elemento de lista de caracteres distintos encontrados por su correspondiente caracter de la lista cadena, es decir, el primer caracter de la lista de caracteres distintos se debe reemplazar por el primer elemento de la lista_clave, el segundo por el segundo, y asi sucesivamente hasta reemplazar todos los caracteres.
# 4. Reescribe la cadena original por una nueva cadena con los nuevos caracteres.

def caracteres_distintos(cadena):
    list_caracteres_distintos=[]
    for a in cadena:
        if a not in list_caracteres_distintos:
            list_caracteres_distintos.append(a)
    return list_caracteres_distintos

def convertir_str_a_lista(cadena):
    lista=[]
    for a in cadena:
        lista.append(a)
    return lista

def cifrar(cadena_original: str,clave_cifrado: str,reverse: bool=False):
    lista_distintos=caracteres_distintos(cadena_original)

    cadena_cifrada=""
    lista_clave=convertir_str_a_lista(clave_cifrado)
    for c in cadena:
        indice=lista_distintos.index(c)

        cadena_cifrada+=lista_clave[indice]
    return cadena_cifrada

def decifrar(cadena_cifrada: str):
    global cadena
    car_dis=caracteres_distintos(cadena_cifrada)
    car_dis_original=caracteres_distintos(cadena)
    cadena_decifrada=""
    for c in cadena_cifrada:
        indice=car_dis.index(c)
        cadena_decifrada+=car_dis_original[indice]
    return cadena_decifrada


mensaje_cifrado=cifrar(cadena,clave)
print(mensaje_cifrado)
print("-----------------")
print(decifrar(mensaje_cifrado))

