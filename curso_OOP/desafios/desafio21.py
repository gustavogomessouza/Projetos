from rich import print
from rich.console import Console
console = Console()

class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.tampa = True

    def destampar(self):
        self.tampa = False
    
    def escrever(self,string):
            if self.cor == 'azul':
                if self.tampa == False:
                    console.print(f'[blue]{string}[/]', end=' ')
                else:
                    console.print('A [blue]caneta[/] está tampada')
            if self.cor == 'vermelho':
                if self.tampa == False:
                    console.print(f'[red]{string}[/]', end=' ')
                else:
                    console.print('A [red]caneta[/] está tampada')
            if self.cor == 'verde':
                if self.tampa == False:    
                    console.print(f'[green]{string}[/]', end=' ')
                else:
                    console.print('A [green]caneta[/] está tampada')

    def quebrar_linha(self):
        console.print('\n')

    def tampar(self):
        self.tampa = True



caneta1 = Caneta('azul')
caneta2 = Caneta('vermelho')
caneta3 = Caneta('verde')

caneta1.destampar()
caneta2.destampar()
caneta3.destampar()

caneta1.escrever('OLA, tudo bem?')
caneta1.quebrar_linha()
caneta2.escrever('Falaí seu feio')
caneta3.escrever('Vamo pro RU?')


console.print(' ')