def calcular_imposto(preco):
    imposto = preco * 0.1
    preco_final = preco + imposto
    return imposto, preco_final