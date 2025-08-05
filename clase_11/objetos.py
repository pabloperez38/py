class Animal:
    """
    Clase base (padre) que define comportamientos comunes.
    """
    
    def __init__(self, nombre, especie):
        """
        Constructor de la clase Animal.
        """
        self.nombre = nombre
        self.especie = especie
    
    def hacer_sonido(self):
        """
        Método que será sobrescrito por las subclases.
        """
        return "Algún sonido"
    
    def obtener_info(self):
        """
        Método que retorna información del animal.
        """
        return f"{self.nombre} es un {self.especie}"

class Perro(Animal):
    """
    Clase Perro que hereda de Animal.
    """
    
    def __init__(self, nombre, raza):
        """
        Constructor que llama al constructor de la clase padre.
        """
        super().__init__(nombre, "Perro")  # Llamar al constructor padre
        self.raza = raza
    
    def hacer_sonido(self):
        """
        Sobrescribe el método de la clase padre.
        """
        return "¡Guau!"
    
    def pasear(self):
        """
        Método específico de la clase Perro.
        """
        return f"{self.nombre} está paseando"

class Gato(Animal):
    """
    Clase Gato que hereda de Animal.
    """
    
    def __init__(self, nombre, color):
        """
        Constructor de la clase Gato.
        """
        super().__init__(nombre, "Gato")
        self.color = color
    
    def hacer_sonido(self):
        """
        Sobrescribe el método de la clase padre.
        """
        return "¡Miau!"
    
    def trepar(self):
        """
        Método específico de la clase Gato.
        """
        return f"{self.nombre} está trepando"

print("=== EJEMPLO 4: HERENCIA ===")
perro = Perro("Rex", "Labrador")
gato = Gato("Mittens", "Naranja")

print(perro.obtener_info())
print(perro.hacer_sonido())
print(perro.pasear())

print(gato.obtener_info())
print(gato.hacer_sonido())
print(gato.trepar())
print()