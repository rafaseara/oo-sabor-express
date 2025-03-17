class Avaliacao:
    def __init__(self, cliente, nota):
        """
        Inicializador das instâncias de avalicoes

        Parâmetros:
        - cliente (str): O cliente que esta avaliando
        - nota (float): A nota dada pelo cliente (1 a 5)
        """
        self._cliente = cliente
        self._nota = nota