import openpyxl

estudiantes = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))
    estudiantes[nombre] = nota  

if estudiantes:
    promedio = sum(estudiantes.values()) / len(estudiantes)
else:
    promedio = 0

libro = openpyxl.Workbook()
hoja = libro.active
hoja.title = "Notas"

hoja["A1"] = "Nombres"
hoja["B1"] = "Notas"
hoja["C1"] = "Promedio"

fila = 2
for nombre, nota in estudiantes.items():
    hoja[f"A{fila}"] = nombre
    hoja[f"B{fila}"] = nota
    fila += 1  

hoja[f"C2"] = promedio  

libro.save("ejercicio5.xlsx")
print("¡Ejercicio 5 guardado en ejercicio5.xlsx!")
