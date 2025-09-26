from enemigos import enemigos
from creador import crear_jugador
from batalla import batalla

print(" Bienvenido al Mini Juego ")
jugador = crear_jugador()

print("\n Tu personaje:")
jugador.mostrar_stats()

print("\n Estos son los enemigos disponibles:")
for i, enemigo in enumerate(enemigos, 1):
    print(f"{i}. {enemigo.nombre} ({enemigo.raza}, {enemigo.tipo_peleador})")

op = int(input("\nElige el número del enemigo contra el que lucharás: ")) - 1
enemigo_seleccionado = enemigos[op]

print(f"\n {jugador.nombre} se enfrenta a {enemigo_seleccionado.nombre} ")
batalla(jugador, enemigo_seleccionado)
