import random

def calcular_defensa(armadura):
    """Valores base de defensa según el tipo de armadura"""
    defensa_base = {
        "sin armadura": 0,
        "de cuero": 2,
        "de madera": 3,
        "de hierro": 5,
        "de diamante": 8,
        "de roca": 6
    }
    return defensa_base.get(armadura, 1)

def turno_ataque(atacante, defensor):
    """Un turno de ataque entre personajes"""
    defensa = calcular_defensa(defensor.armadura)
    danio = atacante.fuerza + random.randint(1, 6) - defensa
    if danio < 0:
        danio = 0  

    defensor.vida -= danio
    print(f" {atacante.nombre} ataca a {defensor.nombre} causando {danio} de daño.")
    print(f" Vida restante de {defensor.nombre}: {defensor.vida}\n")
    return defensor.vida <= 0  

def usar_pocion(jugador):
    """Curar al jugador si tiene pociones disponibles"""
    if jugador.limite_de_stock > 0:
        jugador.vida += 200  
        jugador.limite_de_stock -= 1
        print(f" {jugador.nombre} usa una poción y recupera 200 de vida.")
        print(f" Vida actual: {jugador.vida}")
        print(f" Pociones restantes: {jugador.limite_de_stock}\n")
    else:
        print(" No te quedan pociones.\n")

def batalla(jugador, enemigo):
    """Sistema de batalla por turnos con decisiones del jugador"""
    print("\n ¡La batalla comienza! \n")

    turno = 0
    while jugador.vida > 0 and enemigo.vida > 0:
        if turno % 2 == 0:
            
            print(f" Es tu turno, {jugador.nombre}")
            print("1. Atacar")
            print("2. Usar poción")
            print("3. Escapar")
            accion = input("Elige tu acción: ")

            if accion == "1":
                if turno_ataque(jugador, enemigo):
                    print(f" {jugador.nombre} ha derrotado a {enemigo.nombre} ")
                    return jugador
            elif accion == "2":
                usar_pocion(jugador)
            elif accion == "3":
                print(f" {jugador.nombre} ha escapado de la batalla.")
                return None
            else:
                print("Acción no válida, pierdes el turno.\n")

        else:
            
            print(f" Turno de {enemigo.nombre}")
            if turno_ataque(enemigo, jugador):
                print(f" {jugador.nombre} ha sido derrotado por {enemigo.nombre} ")
                return enemigo

        turno += 1

    
    print(" Ambos han caído en combate... ¡empate!")
    return None
