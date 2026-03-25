# API de Análise de Dados e Automação

API REST desenvolvida em Python com FastAPI para simulação de processamento de dados, aplicação de regras de negócio e geração de insights.

---

## 💡 Sobre o projeto

Este projeto simula um sistema backend capaz de processar dados de produtos, aplicar regras de negócio (como cálculo de impostos) e gerar análises para apoio à decisão.

---

## 🚀 Funcionalidades

- Cadastro de produtos via API REST  
- Cálculo automático de imposto (10%)  
- Cálculo de preço final  
- Análise de dados:
  - Quantidade de produtos
  - Soma total dos valores
  - Média de preços  

---

## 🧠 Arquitetura

```
api-analise-dados/
│
├── main.py            # Rotas da API
├── services/
│   └── calculo.py     # Regras de negócio
```

---

## 🛠 Tecnologias

- Python  
- FastAPI  
- Uvicorn  

---

## ▶️ Como executar

```bash
pip install fastapi uvicorn
python -m uvicorn main:app --reload
```

Acesse no navegador:

http://127.0.0.1:8000/docs

---

## 📌 Endpoints

- GET /produtos → Lista produtos  
- POST /produtos → Adiciona produto com cálculo automático  
- GET /analise → Retorna métricas (total, média, quantidade)  

---

## 🎯 Objetivo

Simular um sistema backend com foco em automação, análise de dados e aplicação de regras de negócio, utilizando boas práticas de organização e desenvolvimento de APIs.

---

## 📎 Observação

Projeto desenvolvido com foco em aprendizado prático e construção de portfólio para atuação em desenvolvimento backend com Python.
