class Elevador:

    def __init__(self, total_andares, capacidade):
        self.__total_andares = total_andares
        self.__andar_atual = 0
        self.__capacidade = capacidade
        self.__pessoas = 0

    def Inicializar(self):
        print('O elevador está inicializando...')
        
    def Entrar(self):
        if self.__pessoas < self.__capacidade:
            self.__pessoas += 1
            print('\nentrou {} pessoas no elevador '.format(self.__pessoas))
        else:
            print('Capacidade máxima atingida : {} pessoas'.format(self.__capacidade))
    
    def Sair(self):
        if self.__pessoas > 0:
            self.__pessoas -= 1
            print('\nQuantidade de pessoas {}'.format(self.__pessoas))
        else:
            print('Não há pessoas no elevador')
    
    def Subir(self):
        if self.__andar_atual < self.__total_andares:
            self.__andar_atual += 1
            print('O elevador está subindo para o: {} andar'.format(self.__andar_atual + 1))
        else:
            print('Você está no último andar')

    def Descer(self):
        if self.__andar_atual > 0 and self.__andar_atual <= self.__total_andares:
            print("Você esta descendo para o andar {}".format(self.__andar_atual))
            self.__andar_atual -= 1
            print("O elevador chegou ao {}° andar".format(self.__andar_atual))
        else:
            print('Você está no térreo')

    def get_total_andares(self):
        return self.__total_andares

    def set_total_andares(self, total_andares):
        self.__total_andares = total_andares

    def get_andar_atual(self):
        return self.__andar_atual

    def set_andar_atual(self, andar_atual):
        self.__andar_atual = andar_atual

    def get_capacidade(self):
        return self.__capacidade

    def set_capacidade(self, capacidade):
        self.__capacidade = capacidade

    def get_pessoas(self, pessoas):
        self.__pessoas  = pessoas

elevador = Elevador(5, 5)
elevador.Inicializar()
elevador.Entrar()
elevador.Entrar()
elevador.Subir()
elevador.Sair()
elevador.Subir()
elevador.Descer()
