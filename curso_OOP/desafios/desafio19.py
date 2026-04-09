import rich
from rich import print
from rich.console import Console
console = Console(highlight=False)

class Livro:
    def __init__(self, titulo, n_paginas):
        self.titulo = titulo
        self.n_paginas = n_paginas
        self.pagina_atual = 1
        console.print(f'[blue]Você abriu o livro {self.titulo}, ele possúi {self.n_paginas} páginas e você está na [/][yellow]página {self.pagina_atual}[/]')


    def passar_paginas(self,qtde_de_paginas):
        pagina_final = self.pagina_atual + qtde_de_paginas
        mensagem = ''
        while self.pagina_atual <= pagina_final and self.pagina_atual <= self.n_paginas:
            mensagem = mensagem + ' ' + f'Pág{self.pagina_atual}' + ' >'
            self.pagina_atual += 1
        self.pagina_atual -= 1
        print(mensagem)
        if self.pagina_atual >= self.n_paginas:
            console.print(f'Você chegou ao [red]final[/] do livro {self.titulo} e está na [yellow]página {self.pagina_atual}[/]')
            
        else:
            console.print(f'Você avançou {qtde_de_paginas} páginas agora está na [yellow]página {self.pagina_atual}[/]')

livro1 = Livro('Hobbit', 10)
livro1.passar_paginas(10)
