from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

McDonalds = Restaurante('McDonalds', 'Fast Food')
suco_melancia = Bebida('Suco de melancia', 5.0, 'Grande')
carpaccio_salmao = Prato('Carpaccio', 20, 'Carpaccio de salmão')

McDonalds.adicionar_no_cardapio(suco_melancia)
McDonalds.adicionar_no_cardapio(carpaccio_salmao)


def main():
    McDonalds.exibir_cardapio

if __name__ == '__main__':
    main()
