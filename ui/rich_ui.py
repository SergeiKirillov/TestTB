from ui.base_ui import BaseUI
from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align

class RichUI(BaseUI):
    def __init__(self):
        self.console = Console()

    def clear(self):
        self.console.clear()

    def show_menu1(self, title, options):
        self.clear()
        self.console.print(title)
        for i, opt in enumerate(options, 0):
            self.console.print(i, opt)
        return int(self.console.input(">"))
    
    def show_menu(self,title,options):
        """
        Отображает красивое меню и возвращает выбранный пункт.
        """
        self.clear()

        table = Table(
            show_header=True,
            header_style="bold cyan",
            border_style="green"
        )

        table.add_column("№", justify="center", width=5)
        table.add_column("Действие")

        for i, option in enumerate(options, 0):
            table.add_row(str(i), option)

        panel = Panel(
            Align.center(table),
            title=f"[bold yellow]{title}[/bold yellow]",
            border_style="blue",
            padding=(1, 2)
        )

        self.console.print(panel)

        while True:
            try:
                choice = int(
                    self.console.input(
                        "\n[bold green]Выберите пункт:[/bold green] "
                    )
                )

                if 1 <= choice <= len(options):
                    return choice

                self.console.print(
                    "[red]Неверный номер пункта![/red]"
                )

            except ValueError:
                self.console.print(
                    "[red]Введите число![/red]"
                )

    def show_message(self, text):
        self.console.print(text)

    def ask_input(self, text):
        self.console.clear()
        return self.console.input(text)

    def show_question(self, question):
        self.console.print(question)

    def success(self, text):
        self.console.print(f"[green]✓ {text}[/green]")
    
    def error(self, text):
        self.console.print(f"[bold red]✗ {text}[/bold red]")