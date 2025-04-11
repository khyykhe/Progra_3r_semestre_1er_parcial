class Vehiculo:
    """"
    Clase usadaa para crear objetos de tipo vehiculo
    """
    def __init__(self, marca, modelo, color, placa, anio, cilindraje, kilometraje, combustible, seguro, caja_de_cambio,
                 gama, chasis, pais_de_origen, tipo_de_puertas, numero_de_puertas, valor, llanta_de_emergencia):

        self._marca = marca
        self._modelo = modelo
        self._color = color
        self._placa = placa
        self._anio = anio
        self._cilindraje = cilindraje
        self._kilometraje = kilometraje
        self._combustible = combustible
        self._seguro = seguro
        self._caja_de_cambio = caja_de_cambio
        self._gama = gama
        self._chasis = chasis
        self._pais_de_origen = pais_de_origen
        self._tipo_de_puertas = tipo_de_puertas
        self._numero_de_puertas = numero_de_puertas
        self._valor = valor
        self._llanta_de_emergencia = llanta_de_emergencia


    def __str__(self):
        #return f"Vehiculo:{self.__dict__.__str__()}"
        return (f"Marca: {self._marca}\nModelo: {self._modelo}\nColor: {self._color}\nPlaca: {self._placa}\nAnio: {self._anio}\nCilindraje: {self._cilindraje}\nKilometraje: {self._kilometraje}\nCombustible: {self._combustible}"
                f"\nSeguro: {self._seguro}\nCaja de cambio: {self._caja_de_cambio}\nGama: {self._gama}\nChasis: {self._chasis}\nPais de origen: {self._pais_de_origen}\nTipo de puertas:{self._tipo_de_puertas}"
                f"\nNumero de puertas: {self._numero_de_puertas}\nValor: {self._valor}\nLlanta de emergencia {self._llanta_de_emergencia} ")


if __name__ == "__main__":
    objVehiculo1 = Vehiculo("Ford", "F150", "Negro", "ABC1234"
                         , "anio", "cilindraje", "kilometraje", "combustible", "seguro",
                            "caja de cambio", "gama", "chasis", "pais de origen", "tipo de puertas",
                            "numero de puertas", "valor", "llanta de emergencia")
    print("1ER METODO DE PRESENTACIÓN POR CONSOLA")
    print(f"Marca:{objVehiculo1._marca}")
    print("2DO METODO DE PRESENTACIÓN POR CONSOLA")
    print(objVehiculo1)