<img width="1128" height="240" alt="resultado_testes_pytest_recortado" src="https://github.com/user-attachments/assets/f5b0117d-3a4b-47dd-acb8-7cb1ccf978ea" />

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-green?style=flat&logo=pytest&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP-orange?style=flat&logo=requests&logoColor=white)

# Sobre o projeto: Automação de Testes de API REST

Este projeto tem como objetivo praticar a automação de testes de APIs REST utilizando Python. Os testes verificam diferentes operações de uma API de reservas, validando códigos de resposta, dados retornados e o comportamento dos principais endpoints.

## Objetivo

Validar o funcionamento de uma API de reservas, verificando códigos de resposta HTTP, estrutura dos dados retornados e identificadores das reservas.

## Tecnologias utilizadas

- **Python** — linguagem utilizada para desenvolver os testes.
- **Pytest** — execução e organização dos testes automatizados.
- **Requests** — envio de requisições HTTP para a API.
- **Git e GitHub** — versionamento e hospedagem do projeto.

## Cenários automatizados

- Consulta de reservas.
- Validação dos identificadores das reservas.
- Consulta de uma reserva inexistente.
- Criação de uma reserva.
- Atualização de uma reserva.
- Exclusão de uma reserva.

## Execução dos testes: Pytest

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
