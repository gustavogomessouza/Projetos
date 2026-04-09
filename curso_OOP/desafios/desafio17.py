import rich
from rich import print
from rich.panel import Panel
from rich.align import Align
from rich.text import Text


class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
    
    def etiqueta(self):
        return Panel(f'{self.nome:^20}\n{'':-^20}\n{self.preco:.^20}',title='Produto',width=25)

celular1 = Produto('Iphone',1000000)

produto2 = Produto('Notebook Gamer',8000)

print(celular1.etiqueta())
print(max(len(str(produto2.nome)),len(str(produto2.preco)))+2)
print(produto2.etiqueta())