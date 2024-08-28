# Utiliza los archivos de la carpeta evaluación para obtener el número de estudiantes que fueron seleccionados para estudiar INGENIERIA CIVIL PLAN COMUN en la Universidad Técnica Federico Santa María, eligiendo a esta en 1ra prioridad, 2da prioridad y 3ra prioridad, según el tipo de preferencia REGULAR

import matplotlib.pyplot as plt

# Datos
etiquetas = ['Manzanas', 'Bananas', 'Cerezas', 'Peras']
tamaños = [15, 30, 45, 10]
colores = ['red', 'yellow', 'pink', 'green']

# Crear el gráfico
plt.pie(tamaños, labels=etiquetas, colors=colores, autopct='%1.1f%%', startangle=90)

# Asegurar que el gráfico se dibuje como un círculo
plt.axis('equal')

# Mostrar el gráfico
plt.show()
