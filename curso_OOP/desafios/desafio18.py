from rich import print
from rich.panel import Panel


class Churrasco:
    def __init__(self,n_pessoas):
        self.n_pessoas = int(n_pessoas)
    
    def quanta_carne(self):
        return f'[red]{(400 * self.n_pessoas)/1000:.3f}Kg[/] de carne devem ser comprados'

    def custo_total(self):
        return f'Ce vai pagar caro. Vai custar [red]R${(82.4*0.4*(self.n_pessoas)):.2f}[/]'
    
    def preço_pessoa(self):
        return f'O custo por pessoa será de [red]R${(82.4*0.4):.2f}[/]'


churras1 = Churrasco(15)
print(Panel(f'{churras1.quanta_carne()}\n{churras1.custo_total()}\n{churras1.preço_pessoa()}', title='Churras dos amigos'))
