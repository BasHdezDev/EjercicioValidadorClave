from abc import ABC, abstractmethod


class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada: int):
        self.longitud_esperada: int = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        if self.longitud_esperada >= len(clave):
            return True
        else:
            return False

    def _contiene_mayuscula(self, clave: str):

        if not any(letra.isupper() for letra in clave):
            return False
        else:
            return True

    def _contiene_minuscula(self, clave: str) -> bool:
        if not any(letra.islower() for letra in clave):
            return False
        else:
            return True

    def _contiene_numero(self, clave: str):
        if not any(letra.isdigit() for letra in clave):
            return False
        else:
            return True

    @abstractmethod
    def es_valida(self, clave: str):
        pass


class ReglaValidacionGanimedes(ReglaValidacion):

    def __init__(self):
        super().__init__(_longitud_esperada=8)

    def contiene_caracter_especial(self, clave: str) -> bool:
        for char in clave:
            if char == "@" or char == "_" or char == "#" or char == "$" or char == "%":
                return True
            else:
                return False

    def es_valida(self, clave: str) -> bool:
        pass

class ReglaValidacionCalisto(ReglaValidacion):

    def __init__(self):
        super().__init__(_longitud_esperada=6)

    def contiene_calisto(self, clave: str) -> bool:
        clave_lower = clave.lower()
        indice = clave_lower.find('calisto')
        while indice != -1:
            calisto = clave[indice: indice + 7]
            num_mayusculas = sum(1 for letra in calisto if letra.isupper())
            if 2 <= num_mayusculas < len(calisto):
                return True
            indice = clave_lower.find('calisto', indice + 1)
        return False


    def es_valida(self, clave: str) -> bool:
        pass


# ----------------------------------------------------------------------------------------------------

class Validador:
    def __init__(self, regla: ReglaValidacion):
        pass

    def es_valida(self, clave: str) -> bool:
        pass




