import limpiardatos as lp

def prob_1():
    lista_de_lineas=lp.obtener_lista_de_lineas('ArchivoD_Adm2024.csv')
    def split_pc(cadena):
        return lp.split_m(cadena,delimitador=';')

    contador_primera_prioridad=0
    contador_segunda_prioridad=0
    contador_tercera_prioridad=0
    contador_cuarta_prioridad=0
    for linea in lista_de_lineas:
        lin=split_pc(linea)
        # print(linea)
        if lin[4]=='REGULAR':
            if lin[2]=='15100' or lin[2]=='15300':
                #print(lin)
                if lin[1]=='1'and lin[3]=='24':
                    contador_primera_prioridad+=1
                elif lin[1]=='2'and lin[3]=='24':
                    contador_segunda_prioridad+=1
                elif lin[1]=='3'and lin[3]=='24':
                    contador_tercera_prioridad+=1
                elif lin[1]=='4'and lin[3]=='24':
                    contador_cuarta_prioridad+=1
    print(f'primera prioridad: {contador_primera_prioridad}')
    print(f'segunda prioridad: {contador_segunda_prioridad}')
    print(f'tercera prioridad: {contador_tercera_prioridad}')
    print(f'tercera prioridad: {contador_cuarta_prioridad}')

def prob_2():
    def selc():
        lista_de_lineas=lp.obtener_lista_de_lineas('ArchivoD_Adm2024.csv')
        def split_pc(cadena):
            return lp.split_m(cadena,delimitador=';')

        contador_seleccionados=0
        for linea in lista_de_lineas:
            lin=split_pc(linea)
            # print(linea)
            tipo_pref=lin[4]
            estado_pref=lin[3]
            carrera_pref=lin[2]
            if tipo_pref=='REGULAR':
                if carrera_pref=='15100' or carrera_pref=='15300':
                    #print(lin)
                    if estado_pref=='24':
                        contador_seleccionados+=1
        return contador_seleccionados
    
    def total_lista_espera():
        lista_de_lineas=lp.obtener_lista_de_lineas('ArchivoD_Adm2024.csv')
        def split_pc(cadena):
            return lp.split_m(cadena,delimitador=';')

        contador_lista_espera=0
        for linea in lista_de_lineas:
            lin=split_pc(linea)
            # print(linea)
            tipo_pref=lin[4]
            estado_pref=lin[3]
            carrera_pref=lin[2]
            if tipo_pref=='REGULAR':
                if carrera_pref=='15100' or carrera_pref=='15300':
                    #print(lin)
                    if estado_pref!='25':
                        contador_lista_espera+=1
        return contador_lista_espera
    
    lista_espera=total_lista_espera()


    seleccionados=selc()
    print(f'Total postulantes: {lista_espera+seleccionados}')
    print(f'Total seleccionados: {seleccionados}')
    print(f'Porcentaje de seleccionados: {round(seleccionados*100/lista_espera,1)}%')

def buscar(objetivo,palabra):
    import regex as re
    patron = r'(?:'+objetivo+r'){e<=1}'
    
    resultados = re.findall(patron, palabra, flags=re.IGNORECASE)
    if len(resultados)>0:
        # print(resultados)
        return True
    else:
        return False

################################################################
oferta_completa = []
oferta=lp.obtener_lista_de_lineas("Oferta académica.csv")
for l in oferta:
    oferta_completa.append(lp.split_m(l))


codigos=[]
for o in oferta_completa:
    if buscar('medicina',o[2]):
        if not buscar('veterinaria',o[2]):
            if not buscar('bachi',o[2]):
                if not buscar('tecno',o[2]):
                    if not buscar('licen',o[2]):
                        print(o[2])
                        codigos.append(o[0])

# print(codigos)

postulaciones=[]
post=lp.obtener_lista_de_lineas('ArchivoD_Adm2024.csv')

for p in post:
    postulaciones.append(lp.split_m(p,delimitador=';'))

cantidad=0
estados=[]
for p in postulaciones:
    if (p[2] in codigos) and p[4] in ["REGULAR"]:#,"PACE","BEA"]:
        if p[3] not in estados:
            estados.append(p[3])
        if (p[3] in ['25','24']):
            cantidad+=1
print(sorted(estados))
print(cantidad)