from cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, descricao, tipo, tamanho):
        super().__init__(nome, preco)
        self.descricao = descricao
        self.tipo = tipo
        self.tamanho = tamanho
    
    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        valor_desconto = 0.15
        self._preco -= (self._preco * valor_desconto)