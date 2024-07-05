import funciones as fn
opcion=0
listaregistrar=[]
while opcion!=4:
    print("""
        1.-registrar puntajes torneo
        2.-listar todos lo puntajes
        3.-imprimir por tipo
        4.-salir del programa
    """)
    opcion = int(input("ingresa una opcion: "))
    if opcion==1:
        fn.registrarapuntes(listaregistrar)
    elif opcion==2:
        fn.listarpuntaje(listaregistrar)
    elif opcion==3:
        archivarlista = "archivo.txt"
        fn.imprimirtipo(listaregistrar,archivarlista)
    elif opcion==4:
        print("saliendo del programa")