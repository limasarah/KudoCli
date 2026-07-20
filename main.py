#!/usr/bin/env python3
import argparse
from rich.table import Table
from rich.console import Console
from client import StravaClient
from pathlib import Path  # Para manipulação multiplataforma de caminhos
from analyzer import analyze_heart_effort


from rich.panel import Panel
from rich.console import Console

def show_kudo_banner():
    # Exibe o banner estilizado do KudoCli usando Rich com cor rosa personalizada
    banner = """
     _  __           _        ____ _ _     _ 
    | |/ /___ _   _| | _____/ ___| (_) __| |
    | ' // _ \ | | | |/ / _ \___ \ | |/ _` |
    | . \  __/ |_| |   <  __/___) | | | (_| |
    |_|\_\___|\__,_|_|\_\___|____/|_|_|\__,_|

           [#FF69B4]      ❤️  KudoCli  ❤️[/#FF69B4]
    """
    panel = Panel(banner, title="KudoCli", border_style="#FF69B4", style="#FF69B4")
    console = Console()
    console.print(panel)

def main():
    # Determina o caminho absoluto do .env usando pathlib
    env_path = Path(__file__).parent / '.env'
    # O dotenv será carregado automaticamente pelo StravaClient, mas garantimos multiplataforma
    if env_path.exists():
        from dotenv import load_dotenv
        load_dotenv(dotenv_path=env_path)

    show_kudo_banner()

    # Cria o parser de argumentos para subcomandos
    parser = argparse.ArgumentParser(prog="kudo", description="KudoCli: Análise OSINT de atletas Strava")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcomando: search
    search_parser = subparsers.add_parser("search", help="Busca atividades de um atleta pelo username ou ID.")
    group = search_parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--username", type=str, help="Username/slug do atleta Strava")
    group.add_argument("--id", type=str, help="ID do atleta Strava")
    search_parser.add_argument("--limit", type=int, default=10, help="Quantidade de atividades a buscar (padrão: 10)")

    # Subcomando: analyze
    analyze_parser = subparsers.add_parser("analyze", help="Análise de performance das atividades.")
    analyze_parser.add_argument("--table", action="store_true", help="Exibe tabela de performance.")
    analyze_parser.add_argument("--geo", action="store_true", help="Exibe tabela com links de mapa.")
    analyze_parser.add_argument("--limit", type=int, default=10, help="Quantidade de atividades a analisar (padrão: 10)")

    # Subcomando: status
    status_parser = subparsers.add_parser("status", help="Exibe informações do perfil autenticado.")

    args = parser.parse_args()
    console = Console()
    client = StravaClient()

    try:
        if args.command == "search":
            athlete_id = None
            if args.username:
                athlete_id = client.resolve_athlete_id(args.username)
            elif args.id:
                athlete_id = client.resolve_athlete_id(args.id)
            if athlete_id is None:
                raise ValueError("Não foi possível resolver o atleta.")
            activities = client.get_activities_for_athlete(athlete_id, limit=args.limit)
            console.print(f"[bold #FF69B4]Foram encontradas {len(activities)} atividades para o atleta {athlete_id}.[/bold #FF69B4]")
        elif args.command == "analyze":
            activities = client.get_activities(limit=args.limit)
            results = analyze_heart_effort(activities)
            table = Table(title="Análise de Esforço KudoCli", show_lines=True, border_style="#FF69B4")
            table.add_column("Nome", style="#FF69B4")
            table.add_column("FC Média", style="#FF69B4")
            table.add_column("FC Máxima", style="#FF69B4")
            table.add_column("Variabilidade", style="#FF69B4")
            table.add_column("Classificação", style="#FF69B4")
            if args.geo:
                table.add_column("Link GPS", style="#FF69B4")
            for r in results:
                row = [
                    str(r['name']),
                    str(r['average_heartrate']),
                    str(r['max_heartrate']),
                    str(r['variabilidade']),
                    str(r['classificacao'])
                ]
                if args.geo:
                    row.append(r['maps_url'] if r['maps_url'] else '-')
                table.add_row(*row)
            console.print(table)
        elif args.command == "status":
            athlete = client.client.get_athlete()
            panel = Panel(f"Nome: {athlete.firstname} {athlete.lastname}\nID: {athlete.id}\nCidade: {athlete.city}", title="Perfil Autenticado", border_style="#FF69B4", style="#FF69B4")
            console.print(panel)
    except Exception as e:
        # Captura e exibe erros de execução para o usuário
        console.print(f"[bold red]Erro durante a execução: {e}[/bold red]")

# Protege a execução direta do script
if __name__ == "__main__":
    main()


