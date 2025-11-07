#!/usr/bin/env python3
"""
Workshop GitHub - Lista de Presença
Um projeto simples para aprender Git e GitHub!
"""

import json
from datetime import datetime
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

def carregar_participantes():
    """Carrega a lista de participantes do arquivo JSON."""
    arquivo = Path("participantes.json")

    if not arquivo.exists():
        return []

    with open(arquivo, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data.get("participantes", [])

def exibir_lista_presenca():
    """Exibe a lista de presença de forma bonita no terminal."""
    console = Console()

    # Título
    console.print()
    console.print(Panel.fit(
        "[bold cyan]🎓 Workshop: GitHub para Presença Profissional[/bold cyan]\n"
        "[yellow]Engenharia de Computação[/yellow]",
        box=box.DOUBLE,
        border_style="cyan"
    ))
    console.print()

    # Carrega participantes
    participantes = carregar_participantes()

    if not participantes:
        console.print("[yellow]Nenhum participante cadastrado ainda.[/yellow]")
        console.print("[dim]Seja o primeiro a adicionar seu nome! 🚀[/dim]\n")
        return

    # Cria tabela
    tabela = Table(
        title="📋 Lista de Presença",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold magenta",
        title_style="bold green"
    )

    tabela.add_column("#", style="dim", width=6, justify="right")
    tabela.add_column("Nome", style="cyan", min_width=20)
    tabela.add_column("GitHub", style="blue")
    tabela.add_column("Curso", style="green")
    tabela.add_column("Instituição", style="yellow", min_width=25)

    # Adiciona participantes
    for idx, participante in enumerate(participantes, 1):
        nome = participante.get("nome", "")
        github = participante.get("github", "")
        curso = participante.get("curso", "")
        instituicao = participante.get("instituicao", "")

        # Formata o GitHub como @usuario
        github_fmt = f"@{github}" if github else "-"

        tabela.add_row(
            str(idx),
            nome,
            github_fmt,
            curso,
            instituicao
        )

    console.print(tabela)
    console.print()

    # Estatísticas
    total = len(participantes)
    console.print(f"[bold green]✅ Total de participantes: {total}[/bold green]\n")

def main():
    """Função principal."""
    try:
        exibir_lista_presenca()
    except Exception as e:
        console = Console()
        console.print(f"[bold red]Erro:[/bold red] {e}")

if __name__ == "__main__":
    main()
