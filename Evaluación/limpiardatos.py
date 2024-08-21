def obtener_lista_de_lineas(nombre_archivo):
    with open(nombre_archivo, 'r',encoding='utf-8') as ofer:
        lineas=ofer.readlines()

    lineas_limpias=[]
    for l in lineas:
        lineas_limpias.append(l.strip('\n'))
    return lineas_limpias

def split_m(cadena: str,delimitador: str=','):
    import csv
    return list(csv.reader([cadena], delimiter=delimitador))[0]

def crear_diccionario(lista:list):
    pass

lineas=obtener_lista_de_lineas('Oferta académica.csv')
char=""
char.split
for linea in lineas[0:6]:
    print(split_m(linea))
