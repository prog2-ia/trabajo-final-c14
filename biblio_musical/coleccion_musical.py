from contenido import Contenido
from estadistica import Estadistica

class ColeccionMusical(Contenido): 
    def __init__(self, titulo): 
        super().__init__(titulo)
        self.pistas = [] 

    def agregar_pista(self, pista): 
        self.pistas.append(pista) 

    def eliminar_pista(self, pista): 
        if pista in self.pistas: 
            self.pistas.remove(pista) 

    def duracion_total(self):
        return Estadistica.duracion_total(self.pistas) 
    
    def total_pistas(self): 
        return len(self.pistas) 
    