
def main():
    class Persona():
        def __init__(self): #Para agregar datos por teclado
            self.nombre = input("Ingresar nombre: ")
            self.apellido = input("Ingresar apellido: ")
            self.direccion = input("Ingresar direccion: ")
            self.telefono = input("Ingresar telefono: ")

        def mostrarpersona(self):
            print(f"Nombre : {self.nombre} {self.apellido}")

    # persona1 = Persona()
    # persona1.mostrarpersona()

    # persona2 = Persona()
    # persona2.mostrarpersona()

    class Empleado(Persona):
        def __init__(self):
            super().__init__()
            self.__sueldo = float(input("Ingrese su sueldo: ")) #__ sirve para proteger y que no se pueda modificas el valor
            self.alimentacion = 0
            self.transporte = 0
            self.pension = 0
            self.salud = 0
            
        
        def devengado(self):
            if self.__sueldo<2000000 :
                self.alimentacion = 80000
                self.transporte = 60000

        def deducciones(self):
            self.salud = self.__sueldo * 0.0375 
            self.pension = self.__sueldo * 0.04

        def mostrarempleado(self):
            super().mostrarpersona()
            self.salarioneto = self.__sueldo + self.alimentacion + self.transporte - self.pension - self.salud
            print(f"Sueldo : {self.__sueldo}")
            print(f"Alimentacion : {self.alimentacion}")
            print(f"Transporte : {self.transporte}")
            print(f"Pension : {self.pension}")
            print(f"Salud : {self.salud}")
            print(f"Salario Neto : {self.salarioneto}")

    empleado1 = Empleado()
    empleado1.devengado()
    empleado1.deducciones()
    empleado1.mostrarempleado()

if __name__ == "__main__":
    main()