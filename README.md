<img width="720" height="663" alt="videoframe_19009" src="https://github.com/user-attachments/assets/3e9da5f3-eec1-4a61-a231-9ebf0898a340" />

# Automação de Testes de API REST

Projeto de portfólio voltado à automação de testes de API REST, utilizando Python, Pytest e Requests.

## Objetivo

Validar o funcionamento de uma API de reservas, verificando códigos de resposta HTTP, estrutura dos dados retornados e identificadores das reservas.

## Tecnologias utilizadas

- **Python** — linguagem utilizada para desenvolver os testes.
- **Pytest** — execução e organização dos testes automatizados.
- **Requests** — envio de requisições HTTP para a API.
- **Git e GitHub** — versionamento e hospedagem do projeto.

## Cenários de teste

- Consulta de reservas.
- Validação do código HTTP 200.
- Verificação do formato da resposta JSON.
- Validação dos identificadores das reservas.

## Como executar o projeto

### 1. Criar e ativar o ambiente virtual

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 3. Executar os testes

```bash
python -m pytest
```

## API utilizada

[Restful Booker](https://restful-booker.herokuapp.com/booking)

A API é pública e compartilhada. Sua disponibilidade e seus dados podem variar durante a execução dos testes.

## Próximas melhorias

- Testes de criação, atualização e exclusão de reservas.
- Validação de cenários negativos.
- Integração contínua com GitHub Actions.
