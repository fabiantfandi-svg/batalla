class Persona:
    def __init__(self, nombre, raza, velocidad, armadura, arma, pociones, limite_de_stock, vida, tipo_peleador, fuerza):
        self.nombre = nombre
        self.raza = raza
        self.velocidad = velocidad
        self.armadura = armadura
        self.arma = arma
        self.pociones = pociones
        self.limite_de_stock = limite_de_stock
        self.vida = vida
        self.tipo_peleador = tipo_peleador
        self.fuerza = fuerza

    def saludar(self):
        print(f"Hola soy {self.nombre}, un {self.raza} con {self.arma}")
    
    def mostrar_stats(self):
        print(f"""
        Nombre: {self.nombre}
        Raza: {self.raza}
        Velocidad: {self.velocidad}
        Armadura: {self.armadura}
        Arma: {self.arma}
        Pociones: {self.pociones}
        Límite de stock: {self.limite_de_stock}
        Vida: {self.vida}
        Tipo peleador: {self.tipo_peleador}
        Fuerza: {self.fuerza}
        """)
