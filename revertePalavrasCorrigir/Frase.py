class Frase:
    def __init__(self, frase: str) -> None:
        self.__frase = frase

    @property
    def frase(self):
        return self.__frase
    
    @frase.setter
    def frase(self, frase: str):
        self.__frase = frase
