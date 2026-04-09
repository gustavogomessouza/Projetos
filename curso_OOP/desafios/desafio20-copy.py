import rich
from rich import print
from rich.console import Console
from rich.panel import Panel


class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.fav_games = []

    def add_favoritos(self, nome_do_game):
        self.fav_games.append(nome_do_game)

    def ficha(self):
        jogos_fav_str = ""
        for i in self.fav_games:
            jogos_fav_str = jogos_fav_str + ":space_invader:" + i + "\n"
        print(
            Panel(
                f"Nome real: [white on blue]{self.nome}[/]\nJogos favoritos:\n{jogos_fav_str}",
                title=f"Jogador <{self.nick}>",
            )
        )


guga = Gamer("Gustavo Gomes", "gustavogomdesou")
guga.add_favoritos("Minecraft")
guga.add_favoritos("Outer Wilds")
guga.add_favoritos("Obra Dinn")
guga.ficha()
