def registrarapuntes(listaregistrar):
    id = input("ingrese su identificador: ").lower()
    nombre= input("ingrese nombre: ").lower()
    print("""
    -VALORANT
    -FORNITE
    -FIFA
""")
    try:
        juego1 = int(input("ingrese su puntuación en VALORANT: "))
        juego2 = int(input("ingrese su puntuación en FORNITE: "))
        juego3 = int(input("ingrese su puntuación en FIFA: "))
    except:
         print(" ingrese solo numeros")
    print("""
    1.-PRINCIPIANTE
    2.-AVANZADO
    3.-EXPERTO
    """)
    tipo =int(input("ingrese su tipo de nivel como jugador: "))
    diccionario= {
        "id"    : id,
        "nombre": nombre,
        "valorant": juego1,
        "fornite": juego2,
        "fifa": juego3


    }
    listaregistrar.append(diccionario)
def listarpuntaje(listaregistrar):
    print("listar todos los puntajes: ")
    for list in listaregistrar:
        print(list)
def imprimirtipo(listaregistrar,archivarlista):

    for lista in listaregistrar:
            print(lista)
            with open (archivarlista, "w") as archivo:
                archivo.write(f" id jugador: {lista["id"]}, nombre: {lista["nombre"]}, JUEGO VALORANT:  {lista["valorant"]}, JUEGO FORNITE: {lista["fornite"]}, JUEGO FIFA: {lista["fifa"]}\n")

