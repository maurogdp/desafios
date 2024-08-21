
def leer_csv(nombre:str)->list:
    with open(nombre,"r", encoding="utf-8") as archivo:
        return archivo.readlines()

def corregir_ia(lineas:list)->list:
    lineas_corregidas=[]
    for l in lineas:
        
        #l.encode('latin1').decode('utf-8')
        #print(l)
        ll=l.replace("Ã","Í").replace("Ã‘","Ñ").replace("Ã“","Ó").replace("Ãœ","Ü").replace("Ã‰","É").replace("Ã","Á").replace("HN","Ñ").replace("Áš","Ú")
        lineas_corregidas.append(ll)
    return lineas_corregidas

def guardar_csv(nombre,lista):
    with open(nombre,'w',encoding='utf-8') as archivo:
        for l in lista:
            archivo.write(l)


lineas=leer_csv("PostulaciónySelección_Admisión2024/Libro_CódigosADM2024_ArchivoD_Anexo -  Oferta académica.csv")
lineas_corregidas=corregir_ia(lineas)

guardar_csv("PostulaciónySelección_Admisión2024/Oferta académica.csv",lineas_corregidas)

# for l in lineas_corregidas[0:100]:
#     print(l)