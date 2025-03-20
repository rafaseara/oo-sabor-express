from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    """Classe de um restaurante com suas caracteristicas"""
    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializador das instâncias

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self._nome = nome
        self._categoria = categoria
        self._ativo = False #atributo protegido
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        """Colocando uma string para o restaurante"""
        return f'{self._nome}   |   {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        """Lista dos restaurantes instanciados"""
        print(f'{'Nome do Restaurante'.ljust(20)}  |  {'Categoria'.ljust(20)}  |  {'Avaliações'.ljust(20)}  |  {'Status'.ljust(20)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)}  |  {restaurante._categoria.ljust(20)}  |  {str(restaurante.media_avaliacoes).ljust(20)}  |  {restaurante.ativo.ljust(20)}')

    @property #modifica a forma como um atributo de uma classe é acessado
    def ativo(self):
        """Mostra um emoji para diferentes estados do ativo"""
        return '✅' if self._ativo else '❎'

    def alternar_estado(self):  
        """Altera o estado do ativo daquele restaurante"""
        self._ativo = not self._ativo

    def receber_avalicao(self, cliente, nota):
        """
        Registra cada avaliacao do resturante

        Parâmetros:
        - cliente (str): O cliente que esta avaliando
        - nota (float): A nota dada pelo cliente (1 a 5)
        """
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        else:
            print(f'A nota {nota} não está dentro dos parâmetros permitidos e não foi computada')

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao:
            return 'Sem avaliações (-)'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def adicionar_no_cardapio(self, item):
        if isinstance (item, ItemCardapio):
            self._cardapio.append(item)
    
    @property
    def exibir_cardapio(self):
        print(f'\nCardapio do restaurante {self._nome}: \n')

        for num, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{num}. Nome: {item._nome} | Preço: R${item._preco} | Descricao: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{num}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)


