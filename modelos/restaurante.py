from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo = False #atributo protegido
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome}   |   {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(20)}  |  {'Categoria'.ljust(20)}  |  {'Avaliações'.ljust(20)}  |  {'Status'.ljust(20)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)}  |  {restaurante._categoria.ljust(20)}  |  {str(restaurante.media_avaliacoes).ljust(20)}  |  {restaurante.ativo.ljust(20)}')

    @property #modifica a forma como um atributo de uma classe é acessado
    def ativo(self):
        return '✅' if self._ativo else '❎'

    def alternar_estado(self):  
        self._ativo = not self._ativo

    def receber_avalicao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        else:
            print(f'A nota {nota} não está dentro dos parâmetros permitidos e não foi computada')

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Sem avaliações (-)'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

