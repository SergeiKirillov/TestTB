import argparse
from core.application import Application
from ui.terminal_ui import TerminalUI
from ui.rich_ui import RichUI

parser = argparse.ArgumentParser()
parser.add_argument("--ui", choices=["terminal", "rich"], default="terminal")
args = parser.parse_args()

if args.ui == "terminal":
    ui = TerminalUI()
else:
    ui = RichUI()

app = Application(ui)
app.run()


