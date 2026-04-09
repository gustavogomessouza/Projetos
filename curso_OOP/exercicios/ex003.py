

class ContaBancaria:
    '''
    Cria uma conta bancaria e permite fazer saques e depositos
    '''
    def __init__(self,numero_conta,nome_titular,saldo = 0):
        self.nome_titular = nome_titular
        self.saldo = saldo
        self.numero_conta = numero_conta
    
    def sacar(self,qtde):
        if self.saldo >= qtde:
            self.saldo -= qtde
            print(f"{qtde:.2f} reais sacados")
        else:
            print(f"Saldo insuficiente para sacar {qtde:.2f} reais")
    
    def depositar(self,qtde):
        self.saldo += qtde
        print(f"{qtde:.2f} reais depositados")

    def __str__(self):
        return (f"A conta {self.numero_conta} de {self.nome_titular} possui {self.saldo:.2f} reais")

minha_conta = ContaBancaria('1234','Gustavo',1000)

print(minha_conta)
minha_conta.sacar(500)
print(minha_conta)
minha_conta.sacar(700)
print(minha_conta)
minha_conta.depositar(10000000)
print(minha_conta)




# Não é legal usar print() dentro dos métodos de uma classe