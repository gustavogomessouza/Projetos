
class Funcionario:
    def __init__(self,nome,setor,cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return(f'Olá, meu nome é {self.nome}. Sou do setor {self.setor} e meu cargo é {self.cargo}.')

F1 = Funcionario('Gustavo','Desenvolvimento de sistemas', 'Project Manager')

print(F1.apresentacao())