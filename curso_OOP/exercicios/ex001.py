

# Declarando classe

class AlunoUnicamp:
    
    # Atributos



    # Métodos

        # Método construtor
    def __init__(self): 
        self.nome = ""
        self.idade = 0

        # Métodos de instância

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é aluno da Unicamp e tem {self.idade} anos"
    
    def é_bonito(self):
        if self.nome == 'Gustavo':
            return 'sim'
        else:
            return 'não'


# Declarando objeto

Aluno1 = AlunoUnicamp()

Aluno1.nome = "Gustavo"
Aluno1.idade = 18

Aluno1.aniversario()

print(Aluno1.mensagem())
print(Aluno1.é_bonito())


Aluno2 = AlunoUnicamp()
Aluno2.nome = 'Fred'
Aluno2.idade = 20

print(Aluno2.mensagem())
print(Aluno2.é_bonito())

