class Libro:
    def __init__(self, titulo, autor, isbn, ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ejemplares = ejemplares
    
    def __str__(self):
        return f"{self.titulo} escrito por {self.autor} con ISBN {self.isbn}. Hay {self.ejemplares} disponibles"
