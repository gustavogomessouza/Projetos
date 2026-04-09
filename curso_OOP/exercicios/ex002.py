


# Declarando classe

class AlunoUnicamp:
    ''' 
    # ÁREA PARA DOCUMENTAÇÃO DA CLASSE (Docstring)
    
    Cria o objeto 'aluno' que possui atributos: nome,idade; métodos: aniversario(),mensagem(),é_bonito().
    
    Para criar um novo aluno, use:
    variavel = AlunoUnicamp(nome,idade)
    '''
    # Atributos

    '''
    Os atributos estão definidos na instanciação do objeto, é a forma mais segura de se trabalhar com OOP
    '''

    # Métodos

        # Método construtor
    def __init__(self,nome = "",idade = 0): 
        '''Agora os atributos vêm na instanciação'''
        self.nome = nome
        self.idade = idade

        # Métodos de instância

    def aniversario(self):
        self.idade += 1

    def é_bonito(self):
        if self.nome == 'Gustavo':
            return 'sim'
        else:
            return 'não'
    def __str__(self):
        # __str__ mostra a classe do objeto e o seu lugar na memória quando voce escreve print(objeto)
        return f"{self.nome} é aluno da Unicamp e tem {self.idade} anos"
        # Sobrescrevendo o __str__ , agora ele printará a mensagem acima.



# Declarando objeto

'''
Aluno1 = AlunoUnicamp()
Aluno1.nome = "Gustavo"
Aluno1.idade = 18
'''
Aluno1 = AlunoUnicamp('Gustavo',18)
Aluno1.aniversario()

# print(Aluno1.mensagem()) 'Ficou obsoleto pois Aluno.mensagem() foi substituido pela __str__()
print(Aluno1) 
print(Aluno1.é_bonito())


'''
Aluno2 = AlunoUnicamp()
Aluno2.nome = 'Fred'
Aluno2.idade = 20
'''
Aluno2 = AlunoUnicamp('Fred',20)

# print(Aluno2.mensagem()) 'Ficou obsoleto pois Aluno.mensagem() foi substituido pela __str__()
print(Aluno2)

print(Aluno2.é_bonito())






# print(Aluno1.__dict__)
    '''
    Retorna:

        {'nome': 'Gustavo', 'idade': 19}

    Que é o dicionário que conecta cada atributo de Aluno1 ao seu valor

    É equivalente a Aluno.__getstate__()

    A diferença é que __dict__ é um atributo, ou seja, é o valor em si e __getstate__() é o método que retorna esse atributo
    O __getstate__() pode ser alterado na definição da classe, já o __dict__ não.
    '''

# print(Aluno1.__class__)
    '''
    Retorna:

        <class '__main__.AlunoUnicamp'>
    
    Que é exatamente a classe de Aluno1