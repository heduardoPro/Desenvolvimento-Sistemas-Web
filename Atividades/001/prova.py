class Gabarito:
    def __init__(self, respostas):
        self.respostas = respostas
    
    def resposta_questao(self, numero_questao):
        return self.respostas[numero_questao]

class Prova:

    def __init__(self, gabarito):
        self.gabarito = gabarito
        self.respostas_aluno = []

    def resposta_aluno(self, reposta):
        self.respostas_aluno.append(reposta)

    def acertos(self):
        acertos = 0
        for aluno, gabarito in zip(self.respostas_aluno, self.gabarito.respostas):
            if aluno == gabarito:
                acertos += 1

        return acertos

    def nota(self):
        total_pontos = 0
        for i in range(len(self.respostas_aluno)):
            if i <= 10:
                total_pontos += 0.5 if self.respostas_aluno == self.gabarito.respostas else 0
            else:
                total_pontos += 1 if self.respostas_aluno == self.gabarito.respostas else 0

        return total_pontos        
    def maior_nota(self, outra_prova):
        notas = [self.nota(), outra_prova.nota()]
        return max(notas)
    
gabarito = Gabarito(['A', 'B', 'A', 'D', 'A',])

prova_A1 = Prova(gabarito)
prova_A2 = Prova(gabarito)

prova_A1.resposta_aluno('A')
prova_A1.resposta_aluno('B')
prova_A1.resposta_aluno('A')

prova_A2.resposta_aluno('D')
prova_A2.resposta_aluno('D')
prova_A2.resposta_aluno('D')

print("Aluno 1 - Acertos:", prova_A1.acertos())
print("Aluno 1 - Nota Final:", prova_A1.nota())

print("\nAluno 2 - Acertos:", prova_A2.acertos())
print("Aluno 2 - Nota Final:", prova_A1.nota())

maior_nota = prova_A1.maior_nota(prova_A2)
print('A maior nota foi {}'.format(maior_nota))