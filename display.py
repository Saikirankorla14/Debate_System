from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.rule import Rule

console = Console()

def print_intro(topic):
    console.print(Panel(f"[bold]Topic:[/] {topic}", title="Debate Start"))

def print_round(n):
    console.print(Rule(f"Round {n}"))

def print_argument(agent, text, color):
    console.print(Panel(text, title=f"[{color}]{agent}[/]", border_style=color))

def print_scores(reasoning, sa, sb):
    console.print(f"[dim]Judge: {reasoning}[/]")
    console.print(f"  Round scores → A: {sa}  B: {sb}\n")

def print_verdict(verdict, score_a, score_b):
    console.print(Panel(verdict, title="[bold yellow]Final Verdict[/]"))
    table = Table(title="Final Scores")
    table.add_column("Agent")
    table.add_column("Total Score")
    table.add_row("Agent A", str(score_a))
    table.add_row("Agent B", str(score_b))
    console.print(table)