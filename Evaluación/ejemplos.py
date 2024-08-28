import limpiardatos as lp

lista=lp.obtener_lista_de_lineas('Oferta académica.csv')
lista_oferta=[]
for elem in lista:
    l=lp.split_m(elem)
    lista_oferta.append(l)


universidades=[]
for e in lista_oferta[1:]:
    if e[3] not in universidades:
        universidades.append(e[3])

for u in universidades:
    print(u)
