from libro import Libro
import json

JSON_FILENAME = "libros.json"

class Biblioteca:
    def __init__(self):
        self.libros = dict()
        self.cargar(JSON_FILENAME)


    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro
        self.guardar(JSON_FILENAME)
    
    def buscar_por_titulo(self, titulo):
        resultado = []
        for libro in self.libros.values():
            if libro.titulo == titulo:
                resultado.append(libro)
        
        return resultado
    
    def buscar_por_autor(self, autor):
        print(autor)
        resultado = []
        for libro in self.libros.values():
            if libro.autor == autor:
                resultado.append(libro)
        return resultado
    
    def prestar_libro(self, isbn):
        if isbn not in self.libros:
            return False
        
        if self.libros[isbn].ejemplares < 1:
            return False
        
        self.libros[isbn].ejemplares -= 1
        self.guardar(JSON_FILENAME)
        return True
    
    def devolver_libro(self, isbn):
        if isbn not in self.libros:
            return False
        
        self.libros[isbn].ejemplares -= 1
        self.guardar(JSON_FILENAME)
        return True
    
    def listar_libros(self):
        for libro in self.libros.values():
            print(libro)
    
    def guardar(self, filename):
        json_dict = dict()
        for libro in self.libros.values():
            json_dict[libro.isbn] = libro.__dict__
        
        json_text = json.dumps(json_dict, indent=2)

        json_file = open(filename, "w")
        json_file.write(json_text)
        json_file.close()
    
    def cargar(self, filename):
        json_file = open(filename, "r")

        json_text = json_file.read()
        json_dict = json.loads(json_text)
        for libro in json_dict.values():
            self.libros[libro["isbn"]] = Libro(
                libro["titulo"], 
                libro["autor"], 
                libro["isbn"], 
                libro["ejemplares"]
            )

        

