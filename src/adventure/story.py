from adventure.utils import read_events_from_file
import random
from rich import print
from rich.console import Console

default_message = "[yellow]You stand still, unsure what to do. The forest swallows you.[/yellow]"

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return default_message

def left_path(event):
    return "[red][bright_red italic bold]You walk left. [/bright_red italic bold]" + event + "[/red]"

def right_path(event):
    return "[green][bright_green italic bold]You walk right. [/bright_green italic bold]" + event + "[/green]"

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    print("[orange3]You wake up in a dark forest. You can go left or right.[/orange3]")
    while True:
        console = Console()
        choice = console.input("[purple][bold]Which direction do you choose?[/bold] ([red]left[/red]/[green]right[/green]/[blue]exit[/blue]): [/purple]")
        choice = choice.strip().lower()
        if choice == 'exit':
            break
        
        print(step(choice, events))
