cadena="El Monte Everest, la montaña más alta del mundo con una altitud de 8,848 metros, no está completamente inmóvil. Debido a la colisión de las placas tectónicas indoaustraliana y eurasiática, el Everest sigue aumentando de altura a una tasa de aproximadamente 4 milímetros por año. Además, los terremotos pueden afectar su altura, como ocurrió en el terremoto de Nepal de 2015, que redujo su altura en unos pocos centímetros."

clave="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-=_+[]|;:',.<>?/~`"

lista_cadena=[]
caracteres_distintos=[]

for c in cadena:
    if c not in caracteres_distintos:
        caracteres_distintos.append(c)
    lista_cadena.append(c)
print(caracteres_distintos)
print(lista_cadena)
print(len(caracteres_distintos))
import random

clave_reordenada=random.sample(clave,40)
print(len(clave_reordenada))
print(clave)
print(clave_reordenada)