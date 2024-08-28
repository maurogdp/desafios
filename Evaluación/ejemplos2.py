import limpiardatos as lp

lista=lp.crear_lista_diccionarios('Oferta académica.csv')
#print(list(lista[0].keys()))
# for l in lista:
#     print(l['NOMBRE_UNIVERSIDAD'])

universidades=[]
clave='NOMBRE_CARRERA'
for e in lista:
    if e[clave] not in universidades:
        universidades.append(e[clave])

for u in universidades:
    print(u)    