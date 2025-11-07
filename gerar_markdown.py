#!/usr/bin/env python3
"""
Gera arquivo Markdown com a lista de presença
"""

import json
from datetime import datetime
from pathlib import Path

def carregar_participantes():
    """Carrega a lista de participantes do arquivo JSON."""
    arquivo = Path("participantes.json")

    if not arquivo.exists():
        return []

    with open(arquivo, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data.get("participantes", [])

def gerar_markdown():
    """Gera arquivo Markdown com a lista de presença."""
    participantes = carregar_participantes()

    # Inicia o conteúdo do markdown
    md_content = []
    md_content.append("# 🎓 Lista de Presença - Workshop GitHub")
    md_content.append("")
    md_content.append("**Workshop:** GitHub para Presença Profissional")
    md_content.append(f"**Atualizado em:** {datetime.now().strftime('%d/%m/%Y às %H:%M')}")
    md_content.append("")

    if not participantes:
        md_content.append("*Nenhum participante cadastrado ainda.*")
        md_content.append("")
    else:
        md_content.append(f"**Total de participantes:** {len(participantes)}")
        md_content.append("")
        md_content.append("## 📋 Participantes")
        md_content.append("")

        # Cabeçalho da tabela
        md_content.append("| # | Nome | GitHub | Curso | Instituição |")
        md_content.append("|---|------|--------|-------|-------------|")

        # Linhas de participantes
        for idx, participante in enumerate(participantes, 1):
            nome = participante.get("nome", "-")
            github = participante.get("github", "-")
            curso = participante.get("curso", "-")
            instituicao = participante.get("instituicao", "-")

            # Formata o GitHub como link se existir
            if github and github != "-":
                github_link = f"[@{github}](https://github.com/{github})"
            else:
                github_link = "-"

            md_content.append(
                f"| {idx} | {nome} | {github_link} | {curso} | {instituicao} |"
            )

        md_content.append("")

    md_content.append("---")
    md_content.append("")
    md_content.append("*Lista gerada automaticamente pelo GitHub Actions*")

    # Escreve o arquivo
    with open("presenca.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md_content))

    print("✅ Arquivo presenca.md gerado com sucesso!")

if __name__ == "__main__":
    gerar_markdown()
