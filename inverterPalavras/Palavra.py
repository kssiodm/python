class Palavra(object):

    def __init__(self, palavra: str) -> None:
        self.__palavra = palavra
    
    @property
    def palavra(self):
        return self.__palavra
    
    @palavra.setter
    def palavra(self, palavra: str):
        self.__palavra = palavra

    def invertPalavra(self):
        frase = self.palavra
        print(' Você digitou: {}'.format(frase))
        invertida = ' '.join(palavra[::-1] for palavra in frase.split())
        return '{}'.format(invertida)