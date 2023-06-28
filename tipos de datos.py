# datos de tipo numerico
edad = 18
peso = 96
estatura= 1.71
print(f"mi peso es de {peso}")
# operaciones aritmeticas basicas
imc = peso / (estatura**2)
print("Mi imc es de:",imc," \n")
print(type(imc))
print("Mi imc es de: {:.2f}".format(imc),"\n")
# datos de tipo cadena de caracteres
asignatura = "Programacion"
carrera = "Ingenieria civil en informatica"
print("la asignatura de",asignatura,"corresponde a la carrera de",carrera)
print("la cantidad de caracteres de la palabra", asignatura, "es de",len(asignatura))
#valores booleanos
ampolleta = False
interruptor = True
print(ampolleta,interruptor)
print("la variable ampolleta es de tipo:",type(interruptor),"\n")
#podemos transformar cualquier valor a un booleano
print(bool(0))
print(bool(""))
print(bool(None))
print(bool("True"))
print(bool(1))
#datos de tipo list
#inicializando lista de 2 maneras
nueva_lista = list()
otra_lista = []
print("esta es una lista vacia:",nueva_lista)
print("esta es una lista vacia:",otra_lista)
print(type(otra_lista))
#declarando tres listas diferentes
estudiantes = ["Matias", "Marco", "Cristobal", "Sebastian", "Marco"]
num = [1,2,3,4,5,6]
lenguaje = ["Python"]
#¿ Se puede realizar una lista de datos compuestos?
data = [ 'Osorno', {"UV": 'nivel bajo', 'Temp "C': 15}, (-40.5725, -73,.1353)]
listamixta = ['Jose', 50, True]
print("lista de cadena de caracteres:",estudiantes)
print("lista de numeros:",num)
print("lista de elementos:",lenguaje)
print("esta es una lista mixta:",listamixta)
print("esto igual es una lista:",data)
print(len(listamixta))
print(estudiantes.count("pepe"))
print(num.count(5000))

lenguaje = ["JavaScript"]
print("nuevo valor de arreglo de un elemento",lenguaje)
#¿Como accedo a un especifico de la lista?
print(estudiantes[0])
print(estudiantes[1])
print("posicion -2",estudiantes[-2])
#sumar listas
print("suma de listas",estudiantes + num)
#que hacen estas funciones
print(list("Python"))
print(list(range(1,5)))
print("\n")
#tuplas-(no mutables)
newtupla = tuple()
grupo1 = ("Daniel","Cristian","Felipe",200,100,"Daniel")
print("######## 05-tuplas ########")
print(type(grupo1))
print("indice del elemento:",grupo1.index ("Daniel"))
grupo2 = ("Pedro",100,"Felipe","Diego",2020,"Alejandra")
print("trozo de la tupla",grupo2[0:3])

#sets"conjuntos"
conjunto_vacio = set()
conjunto_vacio1 = {}
print(type(conjunto_vacio1))
conjunto_de_colores = set({"Azul","Rojo","Verde"})
conjunto_animales = {"Gato","Perro","Loro"}

print(type(conjunto_de_colores))
print(type(conjunto_animales))
print("El primer set contiene los colores:",conjunto_de_colores)
print("El segundo set contiene los siguientes animales:",conjunto_animales)
conjunto_de_colores.add("Celeste")
print("el set de colores lo conforman:",conjunto_de_colores)

diccionario1 = dict()
diccionario2 = {}

datos_personales = {
    "Nombre":"Jose",
    "Institucion":"Ulagos",
    "Edad":19,
    "Ciudad":"La Union"
}
print("Diccionario inicial:",datos_personales)
print(datos_personales["Nombre"])
print(datos_personales["Institucion"])
print(datos_personales["Edad"])
print(datos_personales["Ciudad"])

print("Diccionario actualizado:",datos_personales)

datos_personales["Asignatura"] = "Quimica"
print(datos_personales)
print("Diccionario con el nuevo campo:",datos_personales)







