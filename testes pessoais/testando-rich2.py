from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

text = Text("This is a Text object.\n", style="italic")
text.append("You can append ", style="bold blue")
text.append("different styles.", style="underline red")

# Pass the Text object to the Panel
console.print(Panel(text, title="Using Text Class"))