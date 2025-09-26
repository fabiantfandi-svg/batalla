from personaje import Persona


razas = {
    "humano": {"velocidad": 20, "vida": 2200, "fuerza": 10},
    "elfo": {"velocidad": 25, "vida": 2000, "fuerza": 8},
    "gigante": {"velocidad": 12, "vida": 3000, "fuerza": 15},
    "ogro": {"velocidad": 14, "vida": 2800, "fuerza": 14},
    "duende": {"velocidad": 22, "vida": 1800, "fuerza": 12},
    "minotauro": {"velocidad": 16, "vida": 2500, "fuerza": 13}
}

armas = {
    "espada": {"tipo_peleador": "guerrero"},
    "arco": {"tipo_peleador": "arquero"},
    "mazo": {"tipo_peleador": "tanque"},
    "cuchillo": {"tipo_peleador": "asesino"},
    "mangual": {"tipo_peleador": "bruto"},
    "alabarda": {"tipo_peleador": "berserker"}
}

def crear_jugador():
    nombre = input("Elige el nombre de tu personaje: ")

    print("\nEscoge una raza:")
    for r in razas.keys():
        print("-", r)
    raza = input("- ").lower()

    print("\nEscoge un arma:")
    for a in armas.keys():
        print("-", a)
    arma = input("- ").lower()

    stats_raza = razas[raza]
    stats_arma = armas[arma]

    jugador = Persona(
        nombre=nombre,
        raza=raza,
        velocidad=stats_raza["velocidad"],
        armadura="sin armadura",
        arma=arma,
        pociones="curación",
        limite_de_stock=2,   
        vida=stats_raza["vida"],
        tipo_peleador=stats_arma["tipo_peleador"],
        fuerza=stats_raza["fuerza"]
    )

    return jugador

