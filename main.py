import openpyxl

# PARTE 1: Crear diccionario y entrada de datos
estudiantes = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))
    estudiantes[nombre] = nota  

# PARTE 2: Calcular promedio
if estudiantes:  # Verificar que hay datos antes de calcular
    promedio = sum(estudiantes.values()) / len(estudiantes)
else:
    promedio = 0  # En caso de que no haya estudiantes

# PARTE 3: Crear archivo Excel
libro = openpyxl.Workbook()
hoja = libro.active
hoja.title = "Notas"

# PARTE 4: Escribir datos en Excel
hoja["A1"] = "Nombres"
hoja["B1"] = "Notas"
hoja["C1"] = "Promedio"

# Escribir los nombres y notas en las columnas A y B
fila = 2
for nombre, nota in estudiantes.items():
    hoja[f"A{fila}"] = nombre  # Escribir nombre en A
    hoja[f"B{fila}"] = nota    # Escribir nota en B
    fila += 1  

# Escribir el promedio en la columna C, justo debajo del último estudiante
hoja[f"C2"] = promedio  

# PARTE 5: Guardar archivo
libro.save("ejercicio5.xlsx")
print("¡Ejercicio 5 guardado en ejercicio5.xlsx!")
