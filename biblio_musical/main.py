from pista import Pista
from playlist import Playlist
from biblioteca import Biblioteca
from reproductor import Reproductor
from estadistica import Estadistica

if __name__ == "__main__":

    p1 = Pista("Numb", "Linkin Park", "rock", 185)
    p2 = Pista("Viva la Vida", "Coldplay", "pop", 240)

    lista = Playlist("Viaje", "feliz")
    lista.agregar_pista(p1)
    lista.agregar_pista(p2)

    lista.mostrar()

    print("Total pistas:", Pista.cantidad_pistas())

    repro = Reproductor()
    repro.reproducir(p1)

    mas_larga = Estadistica.pista_mas_larga(lista.pistas)
    print("Pista más larga:", mas_larga.info())