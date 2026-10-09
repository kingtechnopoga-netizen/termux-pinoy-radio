#!/data/data/com.termux/files/usr/bin/env python
# VECTOR Pinoy Radio - Termux Edition
# Named stations + easy channel switching (press q while playing to go back to menu)

import subprocess
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

STATIONS = [
    ("Love Radio 90.7 Manila",      "https://azura.loveradio.com.ph/listen/love_radio_manila/radio.mp3"),
    ("Yes FM 101.1 Manila",         "https://azura.yesfm.com.ph/listen/yes_fm_manila/radio.mp3"),
    ("MOR / Barangay LS Manila",    "https://playerservices.streamtheworld.com/api/livestream-redirect/MORFM_S01.mp3"),
    ("MYX Philippines",             "http://22283.live.streamtheworld.com:3690/MYXFM_SC"),
    ("DWIZ 882 Manila",             "http://dwizmanila.radioca.st:9079/stream"),
    ("DZMM Radyo Patrol 630",       "http://209.126.124.126:8852/stream"),
    ("Home Radio 97.9 Manila",      "http://142.44.212.114:9071/stream"),
    ("FM Radio Manila (FMR)",       "http://209.126.124.126:8872/stream"),
    ("Bombo Radyo Iloilo",          "https://stream.zenolive.com/gzudz59nz9duv"),
    ("Love Radio Cebu",             "http://loveradiocebu.radioca.st:8033/stream"),
]


def show_menu():
    console.clear()
    console.print(Panel.fit(
        "[bold magenta]VECTOR PINOY RADIO[/bold magenta]\n[cyan]Termux Edition v1.0[/cyan]",
        border_style="magenta",
    ))
    table = Table(title="Mga Station", border_style="cyan", header_style="bold cyan")
    table.add_column("#", justify="right", style="bold yellow")
    table.add_column("Station", style="bold white")
    for i, (name, _) in enumerate(STATIONS, 1):
        table.add_row(str(i), name)
    console.print(table)
    console.print(
        "[green]Controls habang tumutugtog:[/green] "
        "[bold]q[/bold]=stop/balik sa menu  [bold]9/0[/bold]=volume  "
        "[bold]m[/bold]=mute  [bold]space[/bold]=pause"
    )
    console.print("[dim]0 = exit  |  c = custom URL[/dim]")


def play(url, name):
    console.print(Panel.fit(
        f"NOW PLAYING\n[bold cyan]{name}[/bold cyan]",
        border_style="green",
    ))
    try:
        subprocess.run(["mpv", url, "--no-video", "--really-quiet"], check=False)
    except KeyboardInterrupt:
        # Ctrl+C while playing: stop mpv, go back to menu
        pass


def main():
    while True:
        show_menu()
        choice = Prompt.ask("[bold yellow]Piliin ang channel[/bold yellow]", default="0")
        if choice == "0":
            console.print("[cyan]Bye, VECTOR! Ingat.[/cyan]")
            break
        if choice.lower() == "c":
            url = Prompt.ask("Stream URL")
            if url.startswith("http://") or url.startswith("https://"):
                play(url, "Custom Stream")
            else:
                console.print("[red]Invalid URL. Dapat http:// o https:// ang simula.[/red]")
            continue
        if choice.isdigit() and 1 <= int(choice) <= len(STATIONS):
            name, url = STATIONS[int(choice) - 1]
            play(url, name)
        else:
            console.print("[red]Invalid na pinili. Subukan ulit.[/red]")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[cyan]Bye, VECTOR![/cyan]")
