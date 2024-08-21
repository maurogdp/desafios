
def leer(nombre_archivo:str)->list:
    nombre=f"{nombre_archivo}.csv"
    arch=[]
    with open(nombre,"r",encoding='utf-8') as archivo:
        arch=archivo.readlines()
    return arch

datos=leer("datos2")
# fila1=datos[1].spli(",")
print(datos[0].split(",")[3:50])