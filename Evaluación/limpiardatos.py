def obtener_lista_de_lineas(nombre_archivo)->list:
    with open(nombre_archivo, 'r',encoding='utf-8') as ofer:
        lineas=ofer.readlines()

    lineas_limpias=[]
    for l in lineas:
        lineas_limpias.append(l.strip('\n'))
    return lineas_limpias

def split_m(cadena: str,delimitador: str=',')->list:
    import csv
    return list(csv.reader([cadena], delimiter=delimitador))[0]

def crear_lista_diccionarios(nombre_archivo_con_extension:str):
    lista_diccionarios_oferta_academica=[]
    lineas=obtener_lista_de_lineas(nombre_archivo_con_extension)
    lista_lineas_como_lista=[]
    for linea in lineas:
        lista_lineas_como_lista.append(split_m(linea))
    keys=lista_lineas_como_lista[0]
    for datos_carrera in  lista_lineas_como_lista[1:]:
        dicci={}
        for i,dato in enumerate(datos_carrera):
            dicci[keys[i]]=dato
        lista_diccionarios_oferta_academica.append(dicci)
    return lista_diccionarios_oferta_academica

# lineas=obtener_lista_de_lineas('Oferta académica.csv')
# char=""
# char.split
# for linea in lineas[0:6]:
#     print(split_m(linea))

# nombre_archivo='Oferta académica.csv'

# def obtener_todos_valores_desde_clave(lista_diccionarios:list)->list:
#     claves=list(lista_diccionarios[0].keys())
#     print('Elige una de las siguientes claves:')
#     for i,c in enumerate(claves):
#         print(f'{i+1}. {c}')
#     indice=int(input("->" ))
#     clave=claves[indice-1]
#     print(clave)
#     lista_final=[]
#     for l in lista_diccionarios:
#         if l[clave] not in lista_final:
#             lista_final.append(l[clave])
#     return lista_final




# d=crear_lista_diccionarios(nombre_archivo)
# # for a in d:
# #     print(a["NOMBRE_UNIVERSIDAD"])
# print(type(d))
# lista=obtener_todos_valores_desde_clave(d)
# for l in lista:
#     print(l)
