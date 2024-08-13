with open("estudiantes.csv","r",encoding='utf-8') as estudiantes:
    contenido=estudiantes.readlines()
    # print(contenido[0])
    lista=[]
    for linea in contenido:
        lista_fila=linea.strip('\n').split(',')
        # print(lista_fila)
        lista.append(lista_fila)
    datos=[]
    for l in lista[1:]:
        dic={}
        dic["Nombre"]=l[0]
        dic["Matematica"]=float(l[1])
        dic["Fisica"]=float(l[2])
        dic["Quimica"]=float(l[3])
        datos.append(dic)
    #print(datos)
    #mat=[d["Matematica"] for d in datos if d["Matematica"]==1]
    #print(mat)
    nombres=[d["Nombre"] for d in datos]
    print(nombres)
    n=input("ingresa el nombre: ")
    print(f"Las notas de {n} son las siguintes:\n")
    for d in datos:
        if d["Nombre"]==n:
            mat=d["Matematica"]
            fis=d["Fisica"]
            qui=d["Quimica"]
    print(f"Matemática: {mat}")
    print(f"Fis: {fis}")
    print(f"Qui: {qui}")
            
    
    

    # dic=[{'Nombre':nombre_estudiante,'Matematica':nota_matematica,'fisica':nota_fisica,'quimica},{},{},{},...]