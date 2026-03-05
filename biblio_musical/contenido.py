# Clase para agrupar todo el contenido musical

class Contenido: 
    def __init__(self, titulo): 
        self.titulo = titulo 

    def mostrar_titulo(self): 
        return self.titulo 
    
    def descripcion(self): 
        return f"Contenido: {self.titulo}"