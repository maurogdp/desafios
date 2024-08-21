# Dado un registro de estudiantes y sus calificaciones en varias asignaturas, el objetivo es implementar
# funciones para gestionar y analizar las calificaciones.

def obtener_diccionario_de_datos() -> list:
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
    return datos

datos=obtener_diccionario_de_datos()
#print(datos)

# El problema consiste en lo siguiente:
# 1. Crea una función agregar_estudiante(datos, estudiante): que agregue un nuevo estudiante al registro.
# 2. Crea una función eliminar_estudiante(datos, nombre): que elimine un estudiante del registro por su nombre.
# 3. Crea una función actualizar_calificacion(datos, nombre, asignatura, nueva_calificacion): que actualice la calificación de un estudiante en una asignatura específica.
# 4. Crea una función promedio_estudiante(datos, nombre): que calcule y devuelva el promedio de calificaciones de un estudiante.
# 5. Crea una función promedio_asignatura(datos, asignatura): que calcule y devuelva el promedio de calificaciones en una asignatura específica para todos los estudiantes.
# 6. Implementa un menú interactivo que permita al usuario elegir qué acción realizar (agregar, eliminar, actualizar, calcular promedio del estudiante, calcular promedio de la asignatura) y ejecute la función correspondiente.

def agregar_estudiante(datos:list,estudiante:dict) -> None:
    datos.append(estudiante)
    print('\n¡Estudiante registrado exitosamente!\n')

def eliminar_estudiante(datos:list,nombre:str) -> None:
    nom=nombre

    detener_while=False
    while not detener_while:
        for d in datos:
            if d['Nombre']==nom:
                datos.remove(d)
                detener_while=True
                break
        print("No se ha encontrado el estudiante ingresado.\n")
        resp=input('¿Deseas intentar con otro nombre?(s/n): ')
        if resp.lower()=="s":
            nom=input("Ingresa el nombre del estudiante que deseas eliminar de la lista: ")
            continue
        else:
            detener_while=True

def actualizar_calificacion(datos:list,nombre:str,asignatura:str,nueva_calificacion:float) -> None:
    actualizacion=False
    for d in datos:
            if d['Nombre']==nombre:
                d[asignatura]=nueva_calificacion
                actualizacion=True
                print('Actualizacion realizada correctamente.')
                break
    if not actualizacion:
        print("No se ha encontrado el estudiante ingresado.\n")

def promedio_estudiante(datos:list, nombre:str) -> None:
    for d in datos:
        if d['Nombre']==nombre:
            claves=list(d.keys())
            suma=sum([d[c] for c in claves[1:]])
            promedio=round(suma/len(claves[1:]),1)
            print(f"El estudiante {d[claves[0]]} tiene un promedio de {promedio}")

def promedio_asignatura(datos:list, asignatura:str) -> None:
    suma=sum([d[asignatura] for d in datos])
    promedio=round(suma/len(datos),1)
    print(f"El promedio de la asignatura {asignatura} es un {promedio}")

def principal() -> None:
    print("Bienvenido\n")

    while True:
        print("Elige una de  las siguientes accioes:\n")
        print('1. Agregar un estudiante')
        print('2. Eliminar un estudiante')
        print('3. Actualizar calificación de un estudante')
        print('4. Obtener el promedio de notas de un estudiante')
        print('5. Obtener el promedio de una asignatura')
        print('0. Salir')

        r=input("Elige la acción: ")
        if r.isnumeric():
            if r=='1':
                print('Registro de estudiantes\n')
                nom=input("Nombre: ")
                print("\nCalificaciones...")
                mat=round(float(input("\nMatemática: ")),1)
                fis=round(float(input('Física: ')),1)
                qui=round(float(input('Quimica: ')),1)
                claves=list(datos[0].keys())
                estudiante={claves[0]:nom,claves[1]:mat,claves[2]:fis,claves[3]:qui}
                
                agregar_estudiante(datos,estudiante)
            elif r=='2':
                print('Ingresa el nombre del estudiante que deseas eliminiar.\n')

                nombres=[d["Nombre"] for d in datos]
                print(f'Nombres\n {nombres}')
                nombre=input("\nNombre: ")
                eliminar_estudiante(datos,nombre)
            elif r=='3':
                nombres=[d["Nombre"] for d in datos]
                print(f'Nombres\n {nombres}')

                asignaturas=list(datos[0].keys())
                print(f'Asignaturas: {asignaturas[1:]}')
                print('Ingresa los siguientes datos\n')
                nom=input('Nombre del estudiante: ')
                asignatura=input('Asignatura: ')
                nota=input('Nueva nota: ')
                actualizar_calificacion(datos,nom,asignatura,nota)
            elif r=='4':
                nombres=[d["Nombre"] for d in datos]
                print(f'Nombres\n {nombres}')
                print('Indica el nombre del estudiante al que deseas calcular el promedio de notas')
                nombre=input('Nombre: ')
                promedio_estudiante(datos,nombre)
            elif r=='5':
                asignaturas=list(datos[0].keys())
                print(f'Asignaturas: {asignaturas[1:]}')
                print('Indica la asignatura para calcular el promedio de notas')
                claves=list(datos[0].keys())
                for i,c in enumerate(claves[1:]):
                    print(f"{i}. {c}")

                asignatura=input('Asignatura: ')
                promedio_asignatura(datos,asignatura)
            elif r=='0':
                print('Hasta pronto!')
                break

# principal()

print(list(datos[0].keys()))
