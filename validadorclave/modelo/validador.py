from abc import ABC, abstractmethod

from validadorclave.modelo.errores import NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, \
    NoTieneLetraMinusculaError, NoTieneNumeroError, NoTieneCaracterEspecialError, NoTienePalabraSecretaError


class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada: int):
        self._longitud_esperada: int = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave: str) -> bool:
        for letra in clave:
            if letra.isupper():
                return True
        return False

    def _contiene_minuscula(self, clave: str) -> bool:
        for letra in clave:
            if letra.islower():
                return True
        return False

    def _contiene_numero(self, clave: str):
        for letra in clave:
            if letra.isdigit():
                return True
        return False

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionGanimedes(ReglaValidacion):

    def __init__(self):
        super().__init__(longitud_esperada=8)

    def contiene_caracter_especial(self, clave: str) -> bool:
        for char in clave:
            if char in "@_#$%":
                return True
        return False

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError()

        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError()

        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError()

        if not self._contiene_numero(clave):
            raise NoTieneNumeroError()

        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError()

        else:
            return True


class ReglaValidacionCalisto(ReglaValidacion):

    def __init__(self):
        super().__init__(longitud_esperada=6)

    def contiene_calisto(self, clave: str) -> bool:

        palabra = "calisto"
        clave_lower = clave.lower()
        index = 0

        while index < len(clave):
            index = clave_lower.find(palabra, index)
            if index > -1:
                inicio_palabra = index
                final_palabra = index + len(palabra)
                calisto_str = clave[inicio_palabra:final_palabra]
                count = 0
                for letra in calisto_str:
                    if letra.isupper():
                        count +=1

                if 2 <= count < len(palabra):
                    return True
                else:
                    index += len(palabra)
            else:
                return False
        return False



    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError()

        if not self._contiene_numero(clave):
            raise NoTieneNumeroError()

        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError()

        else:
            return True


class Validador:
    def __init__(self, regla: ReglaValidacion):
        self.regla: ReglaValidacion = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)




