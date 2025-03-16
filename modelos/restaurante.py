class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False #atributo protegido
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome}   |   {self.categoria}'
    
    def listar_restaurantes():
        print(f'{'Nome do Restaurante'.ljust(20)}  |  {'Categoria'.ljust(20)}  |  {'Status'.ljust(20)}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(20)}  |  {restaurante.categoria.ljust(20)}  |  {restaurante.ativo.ljust(20)}')

    @property
    def ativo(self):
        return '❎' if self._ativo else '✅'


PizzaPrime = Restaurante('PizzaPrime', 'Pizzaria')
restaurante_praca = Restaurante('Praca', 'Italiana')

Restaurante.listar_restaurantes()

