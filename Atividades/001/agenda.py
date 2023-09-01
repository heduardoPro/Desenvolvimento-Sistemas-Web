class Agenda:
    
    def __init__(self) -> None:
        self.contatos = {}

    def adicionar_contato(self, nome, telefone, email):
        self.contatos[nome] = {'telefone': telefone, 'email': email}
        print(f"Contato {nome} adicionado com sucesso.")

    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print(f"\nContato {nome} removido com sucesso.")
        else:
            print(f"\nContato {nome} não encontrado na agenda.")

    def buscar_pessoa(self, nome):
        posicoes = [index for index, contato_nome in enumerate(self.contatos) if nome == contato_nome]
        if posicoes:
            print(f"{nome} encontrado na posiçÃP: {posicoes}")
        else:
            print(f"{nome} não encontrado na agenda.")
    
    def __str__(self) -> str:
        return f'{self.contatos}'
    
# Exemplo de uso
agenda = Agenda()
print(agenda)

agenda.adicionar_contato("João", "123456789", 'email1@gmail.com')
agenda.adicionar_contato("Maria", "987654321", "email1@gmail.com")
agenda.adicionar_contato("<NAME>", "(00) 0000-0000", "<EMAIL>")

print('-'*80)
print(agenda)
print('-'*80)

agenda.remover_contato("João")
agenda.remover_contato("Henrique")

agenda.buscar_pessoa('Maria')
print('-'*80)
print(agenda)
print('-'*80)



