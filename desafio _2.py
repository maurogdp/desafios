# Dado un registro de estudiantes y sus calificaciones en varias asignaturas, el objetivo es implementar
# funciones para gestionar y analizar las calificaciones.

def obtener_diccionario_de_datos():
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
print(datos)


# El problema consiste en lo siguiente:
# 1. Crea una función agregar_estudiante(datos, estudiante): que agregue un nuevo estudiante al registro.
# 2. Crea una función eliminar_estudiante(datos, nombre): que elimine un estudiante del registro por su nombre.
# 3. Crea una función actualizar_calificacion(datos, nombre, asignatura, nueva_calificacion): que actualice la calificación de un estudiante en una asignatura específica.
# 4. Crea una función promedio_estudiante(datos, nombre): que calcule y devuelva el promedio de calificaciones de un estudiante.
# 5. Crea una función promedio_asignatura(datos, asignatura): que calcule y devuelva el promedio de calificaciones en una asignatura específica para todos los estudiantes.
# 6. Implementa un menú interactivo que permita al usuario elegir qué acción realizar (agregar, eliminar, actualizar, calcular promedio del estudiante, calcular promedio de la asignatura) y ejecute la función correspondiente.
