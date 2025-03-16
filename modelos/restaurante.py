class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo = False #atributo protegido
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome}   |   {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(20)}  |  {'Categoria'.ljust(20)}  |  {'Status'.ljust(20)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)}  |  {restaurante._categoria.ljust(20)}  |  {restaurante.ativo.ljust(20)}')

    @property #modifica a forma como um atributo de uma classe é acessado
    def ativo(self):
        return '✅' if self._ativo else '❎'

    def alternar_estado(self):  
        self._ativo = not self._ativo

