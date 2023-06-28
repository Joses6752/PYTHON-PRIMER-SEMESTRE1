nota_lab1 = float(input("¿Cual es la nota del primer lab"))
nota_lab2 = float(input("¿Cual es la nota del segundo lab"))
promedio_final = (nota_lab1*0.3) + (nota_lab2*0.7)
diccionario1 = dict()
diccionario2 = {}

datos_del_estudiante ={
 "Nombre":"Roberto Gandolfini",
 "Nombre de la asignatura":"Historia",
 nota_lab1:5.5,
 nota_lab2:4.3,
 "promedio": promedio_final
}
print("Diccionario inicial:",datos_del_estudiante)
print(datos_del_estudiante["Nombre"])
print(datos_del_estudiante["Nombre de la asignatura"])
print(datos_del_estudiante[nota_lab1])
print(datos_del_estudiante[nota_lab2 ])



