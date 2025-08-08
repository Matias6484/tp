# 1 Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área del rectángulo
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura    
mi_rectangulo = Rectangulo(7, 3)
area = mi_rectangulo.calcular_area()
print(f"El área del rectángulo es: {area}")
# 2 Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina.
class Mate:
    def __init__(self, n):
        self.n = n  
        self.cebadas_restantes = n  
        self.estado_lleno = False  

    def cebar(self):
        if self.estado_lleno:
            raise Exception("¡Cuidado! ¡Te quemaste!")
        self.estado_lleno = True

    def beber(self):
        if not self.estado_lleno:
            raise Exception("¡El mate está vacío!")
        
        self.estado_lleno = False  

        if self.cebadas_restantes > 0:
            self.cebadas_restantes -= 1
        else:
            print("Advertencia: el mate está lavado.")


mate = Mate(3)

try:
    mate.cebar()
    mate.beber()  
    mate.cebar()
    mate.beber()  
    mate.cebar()
    mate.beber()  
    mate.cebar()
    mate.beber()  
    mate.cebar()
    mate.beber()  
    mate.cebar()
    mate.cebar()  
except Exception as e:
    print(e)
# 3 Botella y Sacacorchos
class Corcho:
    def __init__(self, bodega):
        self.bodega = bodega

class Botella:
    def __init__(self, corcho):
        self.corcho = corcho

class Sacacorchos:
    def __init__(self):
        self.corcho = None  

    def destapar(self, botella):
        if botella.corcho is None:
            raise Exception("La botella ya está destapada.")
        if self.corcho is not None:
            raise Exception("El sacacorchos ya contiene un corcho.")

        
        self.corcho = botella.corcho
        botella.corcho = None

    def limpiar(self):
        if self.corcho is None:
            raise Exception("El sacacorchos no tiene un corcho.")
        
        self.corcho = None

corcho = Corcho("Bodega pobre")
botella = Botella(corcho)


sacacorchos = Sacacorchos()

try:
    sacacorchos.destapar(botella)
    print(f"Corcho extraído de: {sacacorchos.corcho.bodega}")

    sacacorchos.limpiar()
    
    
    sacacorchos.limpiar()

except Exception as e:
    print(f"Error: {e}")
# 4 Una heladería es un tipo especial de restaurante. Cree una clase Restaurante
class Restaurante:
    def __init__(self, restaurante_nombre, tipo_comida):
        self.restaurante_nombre = restaurante_nombre
        self.tipo_comida = tipo_comida

    def describir_restaurante(self):
        print(f"Nombre del restaurante: {self.restaurante_nombre}")
        print(f"Tipo de comida: {self.tipo_comida}")

    def abrir_restaurante(self):
        print(f"El restaurante {self.restaurante_nombre} está ahora abierto.")


class Heladeria(Restaurante):
    def __init__(self, restaurante_nombre, tipo_comida, sabores):
        super().__init__(restaurante_nombre, tipo_comida)
        self.sabores = sabores

    def mostrar_sabores(self):
        print("Sabores de helado disponibles:")
        for sabor in self.sabores:
            print(f"- {sabor}")

mi_heladeria = Heladeria("Firulais", "Heladería", ["Menta", "Tramontana", "Frutilla", "Mango"])


mi_heladeria.describir_restaurante()
mi_heladeria.abrir_restaurante()
mi_heladeria.mostrar_sabores()

# 5 Escribir una clase Personaje
class Personaje:
    def __init__(self, nombre, vida, posicion, velocidad):
        self.nombre = nombre
        self.vida = vida
        self.posicion = posicion  
        self.velocidad = velocidad

    def recibir_ataque(self, cantidad):
        self.vida -= cantidad
        print(f"{self.nombre} recibió {cantidad} de daño. Vida restante: {self.vida}")
        if self.vida <= 0:
            raise Exception(f"{self.nombre} ha muerto.")

    def mover(self, direccion):
        dx, dy = direccion
        nueva_x = self.posicion[0] + dx * self.velocidad
        nueva_y = self.posicion[1] + dy * self.velocidad
        self.posicion = (nueva_x, nueva_y)
        print(f"{self.nombre} se movió a la posición {self.posicion}")

class Soldado(Personaje):
    def __init__(self, nombre, vida, posicion, velocidad, ataque):
        super().__init__(nombre, vida, posicion, velocidad)
        self.ataque = ataque

    def atacar(self, otro_personaje):
        print(f"{self.nombre} ataca a {otro_personaje.nombre} con {self.ataque} de daño")
        otro_personaje.recibir_ataque(self.ataque)

class Campesino(Personaje):
    def __init__(self, nombre, vida, posicion, velocidad, cosecha):
        super().__init__(nombre, vida, posicion, velocidad)
        self.cosecha = cosecha

    def cosechar(self):
        print(f"{self.nombre} cosechó {self.cosecha} unidades.")
        return self.cosecha


soldado = Soldado(nombre="Soldier", vida=100, posicion=(0, 0), velocidad=2, ataque=25)
campesino = Campesino(nombre="pleb", vida=50, posicion=(5, 5), velocidad=1, cosecha=10)


soldado.mover((1, 0))       
campesino.mover((0, -1))    

campesino.cosechar()

try:
    soldado.atacar(campesino)
    soldado.atacar(campesino)
    soldado.atacar(campesino)  
except Exception as e:
    print(f"{e}")
# 6 Usuarios: Cree una clase Usuario.
class Usuario:
    def __init__(self, nombre, apellido, edad, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ciudad = ciudad

    def describir_usuario(self):
        print("📄 Perfil del usuario:")
        print(f"Nombre completo: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad} años")
        print(f"Ciudad: {self.ciudad}")
        print()

    def saludar_usuario(self):
        print(f"Hola, {self.nombre} {self.apellido}! ¡Bienvenido/a de nuevo!\n")
 

usuario1 = Usuario("Santiago","Mamani", 28, "Catamarca")
usuario2 = Usuario("Matias","Cruz", 24, "Salta")
usuario3 = Usuario("Ariel","Ortega", 30, "Jujuy")


for usuario in [usuario1, usuario2, usuario3]:
    usuario.describir_usuario()
    usuario.saludar_usuario()
 
# 7 Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método.
class Usuario:
    def __init__(self, nombre, apellido, edad, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ciudad = ciudad

    def describir_usuario(self):
        print("📄 Perfil del usuario:")
        print(f"Nombre completo: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad} años")
        print(f"Ciudad: {self.ciudad}")
        print()

    def saludar_usuario(self):
        print(f"Hola, {self.nombre} {self.apellido}! ¡Bienvenido/a de nuevo!\n")

class Admin(Usuario):
    def __init__(self, nombre, apellido, edad, ciudad, privilegios):
        super().__init__(nombre, apellido, edad, ciudad)
        self.privilegios = privilegios  

    def mostrar_privilegios(self):
        print(f"Privilegios del administrador {self.nombre} {self.apellido}:")
        for privilegio in self.privilegios:
            print(f"{privilegio}")
        print()
 

admin1 = Admin(
    nombre="Matias",
    apellido="Cruz",
    edad=24,
    ciudad="Salta",
    privilegios=[
        "puede postear en el foro",
        "puede borrar un post",
        "puede banear usuario",
        "puede modificar configuraciones"
    ]
)


admin1.describir_usuario()
admin1.saludar_usuario()
admin1.mostrar_privilegios()

# 8 Privilegios: Escriba una clase Privilegios
class Privilegios:
    def __init__(self, privilegios=None):
        if privilegios is None:
            privilegios = []
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        if self.privilegios:
            print("Privilegios del administrador:")
            for privilegio in self.privilegios:
                print(f"{privilegio}")
        else:
            print("Este administrador no tiene privilegios asignados.")
        print()

class Usuario:
    def __init__(self, nombre, apellido, edad, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ciudad = ciudad

    def describir_usuario(self):
        print("📄 Perfil del usuario:")
        print(f"Nombre completo: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad} años")
        print(f"Ciudad: {self.ciudad}")
        print()

    def saludar_usuario(self):
        print(f"👋 Hola, {self.nombre} {self.apellido}! ¡Bienvenido/a de nuevo!\n")

class Admin(Usuario):
    def __init__(self, nombre, apellido, edad, ciudad, lista_privilegios):
        super().__init__(nombre, apellido, edad, ciudad)
        self.privilegios = Privilegios(lista_privilegios)


admin1 = Admin(
    nombre="Matias",
    apellido="Cruz",
    edad=24,
    ciudad="Salta",
    lista_privilegios=[
        "puede agregar usuarios",
        "puede borrar comentarios",
        "puede banear usuarios"
    ]
)


admin1.describir_usuario()
admin1.saludar_usuario()
admin1.privilegios.mostrar_privilegios()
