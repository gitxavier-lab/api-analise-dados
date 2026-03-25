# API de Análise de Dados e Automação

API REST desenvolvida em Python com FastAPI para simulação de processamento de dados, aplicação de regras de negócio e geração de insights.

## 💡 Sobre o projeto

Este projeto simula um sistema backend capaz de processar dados de produtos, aplicar regras de negócio (como cálculo de impostos) e gerar análises para apoio à decisão.

## 🚀 Funcionalidades

- Cadastro de produtos via API REST
- Cálculo automático de imposto (10%)
- Cálculo de preço final
- Análise de dados:
  - Quantidade de produtos
  - Soma total dos valores
  - Média de preços

## 🧠 Conceitos aplicados

- Desenvolvimento de APIs REST
- Estruturação de lógica de negócio
- Manipulação e análise de dados
- Organização de backend com Python

## 🛠 Tecnologias

- Python
- FastAPI
- Uvicorn

## ▶️ Como executar

```bash
pip install fastapi uvicorn
python -m uvicorn main:app --reload
