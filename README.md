# 🏃‍♂️📊 KudoCli

> **KudoCli** é uma ferramenta de linha de comando (CLI) desenvolvida em **Python** para análise de performance esportiva e interação segura com a API oficial do Strava.

---

# 💡 A História e a Inspiração por Trás do Nome

Mais do que uma simples escolha técnica, o coração do **KudoCli** carrega uma identidade afetiva muito forte.

O nome e a identidade visual do projeto são uma homenagem à **Kekeo**, a cachorrinha mais velha da desenvolvedora.

Essa escolha demonstra que desenvolvimento de software e engenharia não precisam ser frios ou puramente utilitários. É possível criar ferramentas tecnicamente robustas sem abrir mão da personalidade.

Com uma identidade visual baseada na cor **Hot Pink (`#FF69B4`)**, combinada a uma interface elegante no terminal utilizando a biblioteca **Rich**, o projeto une:

- 💻 Engenharia de Software
- 🎨 Design de Interface (TUI)
- ❤️ Identidade Visual
- 🐶 Significado Pessoal

---

# 🛠️ Tecnologias Utilizadas

- Python 3.10+
- stravalib
- rich (Interface CLI e Banner)
- argparse
- python-dotenv
- pyproject.toml (Empacotamento Multiplataforma)

---

# 🚀 Guia de Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/KudoCli.git
cd KudoCli
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Ou instale o projeto como pacote Python:

```bash
pip install --editable .
```

---

# 🌍 Execução Global

O projeto foi empacotado seguindo os padrões modernos do ecossistema Python.

Após instalar em modo editável, o comando passa a funcionar como um aplicativo nativo do sistema operacional.

Basta executar:

```bash
kudo
```

Sem precisar utilizar:

```bash
python main.py
```

Compatível com:

- ✅ Linux
- ✅ Windows
- ✅ macOS

---

# 💻 Comandos Disponíveis

| Comando | Descrição |
|----------|-----------|
| `kudo -h` | Exibe o menu principal com banner e ajuda |
| `kudo --help` | Exibe todos os comandos disponíveis |
| `kudo status` | Verifica autenticação e exibe os dados do perfil autorizado |
| `kudo search --id ID` | Busca um atleta pelo ID |
| `kudo search --username NOME` | Busca um atleta pelo nome de usuário |
| `kudo analyze --table` | Gera uma tabela de performance com Índice de Variabilidade de Esforço |
| `kudo analyze --geo` | Gera uma tabela de performance contendo links diretos para o Google Maps |

---

# 🏛️ Arquitetura, Ética e Privacidade

## A Descoberta sobre a API do Strava

Durante o desenvolvimento do projeto, surgiu uma importante descoberta arquitetural relacionada ao modelo de segurança da API oficial do Strava.

Embora o projeto tenha nascido inspirado em conceitos de **OSINT (Open Source Intelligence)**, ficou evidente que a API oficial segue rigorosamente o padrão **OAuth2**, exigindo autorização explícita do proprietário da conta para qualquer acesso aos dados de atividades.

Na prática, isso significa que a aplicação possui acesso legítimo apenas às contas que concederam autorização diretamente.

Essa característica torna a plataforma aderente aos princípios modernos de segurança e privacidade.

---

# 🔐 Lições Aprendidas

## Privacy by Design

A API do Strava demonstra uma implementação consistente dos princípios de **Privacy by Design**, garantindo que somente usuários autorizados possam compartilhar seus dados.

---

## Compliance

Ferramentas de auditoria e inteligência precisam respeitar rigorosamente:

- Termos de Serviço
- Consentimento do usuário
- Escopos OAuth2
- Limites de acesso definidos pela plataforma

Forçar qualquer tentativa de coleta não autorizada seria incompatível com boas práticas de Cibersegurança.

---

## Saber Pivotar Também é Engenharia

Um dos maiores aprendizados deste projeto foi compreender que maturidade técnica também envolve reconhecer limitações arquiteturais.

Quando uma abordagem deixa de fazer sentido diante das restrições técnicas e éticas, a melhor decisão é reavaliar, adaptar ou redirecionar o projeto.

Essa capacidade faz parte da evolução profissional em Engenharia de Software.

---

## Nenhum Conhecimento é Perdido

Embora parte da proposta inicial tenha sido reformulada, todo o conhecimento desenvolvido permanece extremamente valioso.

Durante o projeto foram consolidadas habilidades como:

- gerenciamento de tokens OAuth2;
- estruturação de uma CLI profissional;
- empacotamento multiplataforma;
- tratamento de exceções;
- boas práticas de arquitetura Python;
- construção de interfaces modernas em terminal utilizando **Rich**.

Todo esse aprendizado servirá como base para futuros projetos voltados à automação, auditoria e ferramentas OSINT baseadas exclusivamente em fontes públicas.

---

# 📋 Roadmap de Competências Desenvolvidas

## Arquitetura da Aplicação

- [x] CLI profissional utilizando `argparse`
- [x] Organização modular do projeto
- [x] Subcomandos independentes
- [x] Estrutura escalável

---

## Empacotamento

- [x] Configuração moderna com `pyproject.toml`
- [x] Instalação via `pip`
- [x] Execução como comando global
- [x] Compatibilidade multiplataforma

---

## Segurança

- [x] Uso de `.env`
- [x] Isolamento de credenciais
- [x] OAuth2
- [x] Controle de escopos de acesso

---

## Interface

- [x] Banner personalizado
- [x] Tabelas estilizadas
- [x] Painéis com Rich
- [x] Identidade visual em Hot Pink (`#FF69B4`)

---

## Cibersegurança

- [x] Estudo aprofundado do fluxo OAuth2
- [x] Compliance em APIs
- [x] Privacy by Design
- [x] Limitações arquiteturais da API do Strava

---

# 🔮 Roadmap Futuro

- [ ] Evoluir o KudoCli como ferramenta de auditoria de performance autorizada.
- [ ] Expandir os recursos de análise estatística esportiva.
- [ ] Melhorar relatórios e visualizações em terminal.
- [ ] Desenvolver uma nova ferramenta de OSINT baseada exclusivamente em fontes públicas e abertas.
- [ ] Aplicar toda a experiência adquirida neste projeto em novas soluções voltadas para Segurança da Informação e Engenharia de Software.

---

# 📚 Principais Aprendizados

O KudoCli representa muito mais do que uma ferramenta de linha de comando.

Ele demonstra a evolução prática em:

- Engenharia de Software
- Arquitetura de Aplicações
- Empacotamento Python
- Segurança da Informação
- OAuth2
- APIs REST
- Interfaces de Terminal (TUI)
- Compliance
- Design de Software

Acima de tudo, o projeto reforça que escrever código também pode ser uma forma de expressar criatividade, identidade e significado pessoal.

---

## ❤️ Homenagem

> "Todo projeto conta uma história. O KudoCli foi construído para aprender tecnologia, mas também para eternizar a companhia da Keko em cada comando executado."

---

## 📄 Licença

Este projeto é disponibilizado para fins educacionais e de aprendizado.

Sinta-se à vontade para estudar o código, contribuir com melhorias e utilizá-lo como referência para projetos próprios, sempre respeitando as políticas e os Termos de Serviço das APIs utilizadas.
