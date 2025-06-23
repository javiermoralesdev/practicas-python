from biblioteca import Biblioteca
from libro import Libro

import re

biblioteca = Biblioteca()
def main():
    opcion = -1
    while opcion != 7:
        print("Bienvenido a la biblioteca")
        print("Opciones: ")
        print("1 Agregar un libro")
        print("2 Buscar por titulo")
        print("3 Buscar por autor")
        print("4 Prestar libro")
        print("5 Devolver libro")
        print("6 Listar todos los libros")
        print("7 Salir")
        try:
            opcion = int(input("Ingresa tu opción: "))
            procesar_opcion(opcion)
        except:
            pass

def procesar_opcion(opcion):
    match opcion:
        case 1:
            try:
                biblioteca.agregar_libro()
            except ValueError as e:
                print(repr(e))
        
        case 2:
            titulo = input("Introduce el titulo que buscar: ")
            resultado = biblioteca.buscar_por_titulo(titulo)
            if len(resultado) == 0:
                print("Ningún libro coincide")
            for libro in resultado:
                print(libro)
        
        case 3:
            autor = input("Introduce el autor que buscar: ")
            resultado = biblioteca.buscar_por_autor(autor)
            if len(resultado) == 0:
                print("Ningún libro coincide")
            for libro in resultado:
                print(libro)
        
        case 4:
            isbn = input("Qué ISBN quieres coger prestado? ")
            if not biblioteca.prestar_libro(isbn):
                print("No tenemos ese libro o está agotado")
        
        case 5:
            isbn = input("Qué ISBN quieres devolver?")
            if not biblioteca.devolver_libro(isbn):
                print("No tenemos ese libro")
        
        case 6:
            biblioteca.listar_libros()
        
    print("Operación completada. Pulse enter para volver al menú")
    input()
        


if __name__ == '__main__':
    main()
