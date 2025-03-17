from modelos.restaurante import Restaurante

McDonalds = Restaurante('McDonalds', 'Fast Food')

McDonalds.alternar_estado()

McDonalds.receber_avalicao('Rafaella', 10)
McDonalds.receber_avalicao('Roberto', 3)
McDonalds.receber_avalicao('Milena', 5)

def main():
    """O main do programa"""
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()