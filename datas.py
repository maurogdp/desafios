import csv
import random

# Listas de nombres y apellidos
nombres = ["Juan", "Ana", "Luis", "Maria", "Carlos", "Elena", "Fernando", "Lucia", "Miguel", "Sofia",
           "Jose", "Laura", "Javier", "Andrea", "Pablo", "Carmen", "Diego", "Paula", "Alberto", "Marta",
           "Rafael", "Sara", "Pedro", "Nuria", "Alfonso", "Isabel", "Jorge", "Patricia", "Manuel", "Victoria",
           "Antonio", "Cristina", "Francisco", "Olga", "Raul", "Silvia", "Hugo", "Eva", "Enrique", "Alicia",
           "Sergio", "Beatriz", "Emilio", "Irene", "Jaime", "Miriam", "Gonzalo", "Teresa", "Ricardo", "Clara"]

apellidos = ["González", "Muñoz", "Rojas", "Díaz", "Pérez", "Soto", "Silva", "Contreras", "López", "Rodríguez",
             "Morales", "Martínez", "Fuentes", "Valenzuela", "Araya", "Sepúlveda", "Espinoza", "Torres", "Castillo",
             "Ramírez", "Reyes", "Gutiérrez", "Castro", "Vásquez", "Fernández", "Tapia", "Pizarro", "Sandoval",
             "Peña", "Sánchez", "Carrasco", "Martín", "Herrera", "Núñez", "Jara", "Vergara", "Rivera", "Figueroa",
             "Riquelme", "Gómez", "Campos", "Mejías", "Escobar", "Bravo", "Vera", "Molina", "Vega", "Méndez", "Vidal"]

# Función para generar datos de estudiantes
def generar_datos_estudiantes(n):
    datos = []
    nombres_usados = set()
    
    while len(datos) < n:
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        nombre_completo = f"{nombre} {apellido}"
        
        if nombre_completo not in nombres_usados:
            nombres_usados.add(nombre_completo)
            matematicas = round(random.uniform(1.0, 7.0), 1)
            fisica = round(random.uniform(1.0, 7.0), 1)
            quimica = round(random.uniform(1.0, 7.0), 1)
            datos.append({'nombre': nombre_completo, 'matematicas': matematicas, 'fisica': fisica, 'quimica': quimica})
    
    return datos

# Generar 500 datos de estudiantes
datos_estudiantes = generar_datos_estudiantes(500)

# Guardar los datos en un archivo CSV
with open('estudiantes.csv', 'w', newline='',encoding='utf-8') as archivo_csv:
    campos = ['nombre', 'matematicas', 'fisica', 'quimica']
    escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
    
    escritor.writeheader()
    escritor.writerows(datos_estudiantes)

print("Datos de estudiantes generados y guardados en 'estudiantes.csv'")
