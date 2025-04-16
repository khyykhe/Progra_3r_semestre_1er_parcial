class Persona:
    """"
    Creación de un objeto tipo Persona
    """

    def __init__ (self, salario:float, rol=""):
        self._salario = salario
        self._rol = rol

    def __str__(self):
        return f"Persona: {self.__dict__.__str__()}"


    def calcular_iess(self, rol:"privado"):
    #privado= 0.0945
    #publico= 0.1145
        return self._salario*0.0945

if __name__ == "__main__":
    oPersona1 = Persona(salario=1000.00, rol="privado")
    print(oPersona1)