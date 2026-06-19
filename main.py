import argparse
from core.application import Application
from ui.terminal_ui import TerminalUI
from ui.rich_ui import RichUI

def parse_args():
    parser = argparse.ArgumentParser(
        description="Система проверки знаний"
    )
    parser.add_argument(
        "--ui", 
        choices=["terminal", "rich"], 
        default="terminal",
        help="Тип интерфейса"
    )
    parser.add_argument(
        "--theme",
        default=None,
        help="Тема вопросов"
    )
    return parser.parse_args()


if __name__=="__main__":
    args = parse_args()
   
    app = Application(ui_type = args.ui , theme=args.theme)
    if args.theme is None:
        app.selectDB()
    else:
        app.run("electrical")
    

