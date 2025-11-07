# 🎓 Workshop: GitHub: Contruindo sua Presença Profissional

Bem-vindo ao workshop sobre como usar GitHub para construir sua presença profissional! Este é um projeto prático onde você vai aprender a fazer seu primeiro Pull Request.

## 📋 Sobre o Projeto

Este é um programa simples em Python que exibe uma lista de presença dos participantes do workshop. Você vai adicionar seu nome à lista praticando o fluxo de trabalho do GitHub!

### 🤖 Automação com GitHub Actions

Este projeto usa GitHub Actions para automatizar algumas tarefas:

- **Validação de PRs**: Quando você abre um Pull Request, a action automaticamente valida seu JSON, testa se o programa funciona e verifica se todos os campos obrigatórios foram preenchidos.
- **Atualização automática**: Quando seu PR é aceito, uma action gera automaticamente um arquivo `presenca.md` com a lista formatada de todos os participantes.

## 🚀 Como Executar

```bash
# 1. Clone o repositório (ou seu fork)
git clone https://github.com/SEU-USUARIO/presenca-profissional.git
cd presenca-profissional

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Execute o programa
python presenca.py
```

## 🤝 Como Contribuir (Seu Primeiro Pull Request!)

### Passo 1: Faça um Fork

Clique no botão "Fork" no canto superior direito desta página para criar uma cópia do repositório na sua conta.

### Passo 2: Clone seu Fork

```bash
git clone https://github.com/SEU-USUARIO/presenca-profissional.git
cd presenca-profissional
```

### Passo 3: Crie um Branch

**🎯 IMPORTANTE:** Sempre crie um branch novo para suas mudanças. Nunca trabalhe direto na branch `main`!

```bash
git checkout -b adicionar-meu-nome
```

Dica: Use nomes descritivos para seus branches, como:
- `adicionar-joao-silva`
- `feat/adicionar-maria-santos`
- `add-pedro-oliveira`

### Passo 4: Adicione seu Nome

Abra o arquivo `participantes.json` e adicione suas informações:

```json
{
  "nome": "Seu Nome Completo",
  "github": "seu-usuario-github",
  "curso": "Engenharia de Computação",
  "instituicao": "Sua Universidade"
}
```

**⚠️ Atenção:**
- Adicione sua entrada **no final** da lista, antes do `]`
- Não esqueça da vírgula após a entrada anterior
- Mantenha a formatação (indentação)

### Passo 5: Teste Localmente

Antes de enviar, teste se funciona:

```bash
python presenca.py
```

Você deve ver seu nome na lista! 🎉

### Passo 6: Commit suas Mudanças

```bash
git add participantes.json
git commit -m "Adiciona [Seu Nome] à lista de presença"
```

**💡 Boas Práticas para Commits:**
- Use mensagens claras e descritivas
- Comece com um verbo no imperativo: "Adiciona", "Corrige", "Atualiza"
- Seja específico sobre o que mudou

### Passo 7: Push para seu Fork

```bash
git push origin adicionar-meu-nome
```

### Passo 8: Abra um Pull Request

1. Vá para a página do seu fork no GitHub
2. Clique no botão "Compare & pull request"
3. Escreva um título claro: `Adiciona [Seu Nome] à lista de presença`
4. Na descrição, explique brevemente sua mudança
5. Clique em "Create pull request"
6. Aguarde os testes automáticos passarem (GitHub Actions) ✅

**Dica:** O GitHub vai automaticamente testar seu PR verificando:
- Se o JSON é válido
- Se o programa executa sem erros
- Se todos os campos obrigatórios estão preenchidos

## ✅ Checklist para Pull Requests

Antes de enviar seu PR, confira:

- [ ] Criei um branch novo (não estou na `main`)
- [ ] Adicionei apenas minhas informações (não alterei dados de outros)
- [ ] Testei o programa localmente com `python presenca.py`
- [ ] Meu JSON está formatado corretamente (sem erros de sintaxe)
- [ ] Todos os campos obrigatórios estão preenchidos (nome, github, curso, instituicao)
- [ ] Minha mensagem de commit é clara
- [ ] Meu PR tem um título descritivo

## 📚 Regras de Boa Convivência

1. **Um PR por pessoa**: Adicione apenas suas informações
2. **Respeite o trabalho dos outros**: Não altere ou remova informações de outros participantes
3. **Mantenha a formatação**: Siga o padrão do arquivo JSON
4. **Seja educado**: Use linguagem profissional em commits e PRs
5. **Peça ajuda**: Se tiver dúvidas, pergunte! Estamos aqui para aprender

## 🎯 Objetivos de Aprendizado

Completando este exercício, você vai praticar:

- ✅ Fazer fork de um repositório
- ✅ Clonar um repositório
- ✅ Criar e trabalhar em branches
- ✅ Fazer commits com boas mensagens
- ✅ Enviar código para o GitHub
- ✅ Abrir e gerenciar Pull Requests
- ✅ Colaborar em projetos open source

## 🤔 Problemas Comuns

### Erro de JSON inválido
Se o programa não funcionar, provavelmente há um erro de sintaxe no JSON. Verifique:
- Vírgulas entre as entradas
- Aspas em todos os textos
- Colchetes e chaves fechados corretamente

### Conflitos no Pull Request
Se houver conflitos, significa que o arquivo foi alterado desde que você fez o fork. Para resolver:
```bash
git pull upstream main
```

## 📞 Precisa de Ajuda?

- Abra uma issue descrevendo seu problema
- Pergunte durante o workshop
- Consulte a [documentação do GitHub](https://docs.github.com)

## 🎉 Parabéns!

Ao completar este exercício, você deu seu primeiro passo para construir sua presença profissional no GitHub! Continue contribuindo para projetos open source e construindo seu portfólio.

---

**Feito com ❤️ para o Workshop de GitHub**
