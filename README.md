<img width="1128" height="240" alt="resultado_testes_pytest_recortado" src="https://github.com/user-attachments/assets/f5b0117d-3a4b-47dd-acb8-7cb1ccf978ea" />

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-green?style=flat&logo=pytest&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP-orange?style=flat&logo=requests&logoColor=white)

# 	📌 Sobre o projeto: Automação de Testes de API REST

Este projeto consiste na automação de testes de uma API REST de reservas, verificando o comportamento dos endpoints, os códigos de resposta HTTP e a estrutura dos dados retornados.

##	🎯 Objetivo

Verificar se as operações de consulta, criação, atualização e exclusão de reservas funcionam conforme esperado, incluindo a validação dos identificadores e das respostas da API.

## Tecnologias utilizadas

- **Python** — linguagem utilizada para desenvolver os testes.
- **Pytest** — execução e organização dos testes automatizados.
- **Requests** — envio de requisições HTTP para a API.
- **Git e GitHub** — versionamento e hospedagem do projeto.
- **GitHub Actions** — execução automática dos testes por integração contínua (CI).

## Cenários de testes

- Consulta de reservas (GET).
- Validação dos identificadores das reservas.
- Consulta de uma reserva inexistente.
- Criação de uma reserva (POST).
- Atualização de uma reserva (PUT).
- Exclusão de uma reserva (DELETE).

## Execução dos testes

Os testes automatizados são executados com **Pytest**.

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

## 🚀 Melhorias futuras

- Ampliar a cobertura dos testes com cenários negativos.
- Adicionar validações mais detalhadas das respostas da API.
- Gerar relatórios HTML com os resultados dos testes.
- Melhorar a organização e a reutilização do código de testes.
