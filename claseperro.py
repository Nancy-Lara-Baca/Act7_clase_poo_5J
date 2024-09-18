print("Programacion POO")
# Definicion de clases
class Perro:
    # Funciones dentro de la clase
    def morder(self):
        print("El perro me mordio")
    def Datos_perro(self, nombre, edad):
        print(f" Nombre : {nombre} edad: {edad}")


# Zona de creacion de objetos
pitbull=Perro()

# Zona de uso de objetos

pitbull.Datos_perro("Bobby", 4)
pitbull.morder