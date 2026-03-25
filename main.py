from fastapi import FastAPI

app = FastAPI()

produtos = [
    {"id": 1, "nome": "Produto A", "preco": 100},
    {"id": 2, "nome": "Produto B", "preco": 200}
]

@app.get("/")
def home():
    return {"mensagem": "API de Análise de Dados rodando"}

@app.get("/produtos")
def listar_produtos():
    return produtos

@app.post("/produtos")
def adicionar_produto(produto: dict):
    imposto = produto["preco"] * 0.1
    produto["imposto"] = imposto
    produto["preco_final"] = produto["preco"] + imposto

    produtos.append(produto)
    return {
        "mensagem": "Produto adicionado com cálculo",
        "produto": produto
    }

@app.get("/analise")
def analisar_produtos():
    total = sum(p["preco"] for p in produtos)
    media = total / len(produtos)

    return {
        "total_produtos": len(produtos),
        "valor_total": total,
        "media_preco": media
    }