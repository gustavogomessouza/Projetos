import rich
from rich.console import Console
from rich import print
from rich.panel import Panel
console = Console()

class ControleRemoto:
    def __init__(self):
        self.canal_atual = 0
        self.volume_atual = 0
        self.ligado = False
        self.ui_volume = ''
        self.ui_canais = ''

    def mudar_canal(self, frente_ou_tras):
        self.canal_atual = (self.canal_atual + frente_ou_tras)%5
    
    def mudar_volume(self, frente_ou_tras):
        if self.volume_atual + frente_ou_tras <= 5 and self.volume_atual + frente_ou_tras >= 0:
            self.volume_atual += frente_ou_tras
    
    def botao(self):
        self.ligado = not self.ligado

    def comando(self,comando_atual):
        if comando_atual == '<':
            c1.mudar_canal(-1)
        elif comando_atual == '>':
            c1.mudar_canal(1)
        elif comando_atual == '-':
            c1.mudar_volume(-1)
        elif comando_atual == '+':
            c1.mudar_volume(1)
        elif comando_atual == '@':
            c1.botao()
        elif comando_atual == '0':
            quit()
    
    def gerar_uis(self):
        self.ui_canais = ''
        self.ui_volume = ''
        for i in range(5):
                if self.canal_atual == i:
                    self.ui_canais += f' [black on orange3]{i+1}[/]'
                else:
                    self.ui_canais += (' ' + str(i+1))
        for i in range(5):
            if self.volume_atual >= i+1:
                self.ui_volume += '[on green]  [/]'
            else:
                self.ui_volume += '[on white]  [/]'
        if c1.ligado == False:
            console.print(Panel('[red]A TV está desligada[/]\n',title='[ TV ]',width=33))
        else:
            console.print(Panel(f'Canal = {self.ui_canais}\nVolume = {self.ui_volume}',title='[ TV ]'), width= 33)
                

c1 = ControleRemoto()


while True:
    c1.gerar_uis()
    c1.comando(input())

