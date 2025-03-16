from modelos.restaurante import Restaurante

McDonalds = Restaurante('McDonalds', 'Fast Food')
Kaishi = Restaurante('Kaishi', 'Japonesa')
DivinoFogao = Restaurante('DivinoFogao', 'Brasileira')

McDonalds.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()