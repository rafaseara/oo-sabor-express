from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

McDonalds = Restaurante('McDonalds', 'Fast Food')
Suco_melancia = Bebida('Suco de melancia', 5, 'Grande')
Carpaccio_salmao = Prato('Carpaccio', 20, 'Carpaccio de salmão')

McDonalds.adicionar_bebida(Suco_melancia)
McDonalds.adicionar_prato(Carpaccio_salmao)


def main():
    pass

if __name__ == '__main__':
    main()
