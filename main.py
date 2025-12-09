from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/greetings")
def saudacoes():
    return {"mensagem":  "Hello World"}

# /calculadora?numero1=9&numero2=1
@app.get("/calculadora")
def calculadora(numero1: int, numero2: int):
    soma = numero1 + numero2
    return {"resultado": soma}

# (query) vai depois da ? ex.: /calculadora/expert?operacao=soma&n1=100&n2=200
@app.get("/calculadora/expert")
def calculadora_expert(operacao: str, n1: int, n2: int):
    if operacao not in ["somar", "subtrair"]:
        return HTTPException(
            status_code=400,
            detail="Operação inválida. Opções disponíveis [somar/subtrair]"
        )

    if operacao == "somar":
        resultado = n1 + n2
        return {
            "n1": n1,
            "n2": n2,
            "operacao": operacao,
            "resultado": resultado,
        }
    elif operacao == "subtrair":
        resultado = n1 - n2
        return {
            "n1": n1,
            "n2": n2,
            "operacao": operacao,
            "resultado": resultado,
        }
    
# Criar um endpoint 'pessoa/nome-completo' para concatenar o nome da pessoa
#   Receber dois query params: nome e sobrenome
#   Retornar no seguinte formato {"nomeCompleto": "John Doe"}
# Criar um endpoint 'pessoa/calcular-ano-nascimento' para calcular o ano de nascimento
#   Query param: idade
#   Calcular o ano de nascimento
#   Retornar {"anoNascimento": 1991}
# Criar um endpoint 'pessoa/imc' para calcular o imc da pessoa
#   Query param: altura, peso
#   Calcular o imc
#   Retornar {"imc": 20.29}
# Alterar o endpoint 'pessoa/imc' para retornar o status do imc
#   Descobrir o status do IMC
#   Retornar {"imc"': 20.29, "Obesidade III"}




# fastapi dev main.py

# 127.0.0.1:8000/docs
# 127.0.0.1:8000/greetings

@app.get("/nome/completo")
def nome_completo(nome: str, sobrenome: str):
    nome_completo = f"{nome} {sobrenome}"
    return {"nomeCompleto": nome_completo}

@app.get("/calcular/ano-nascimento")
def calcular_ano_nascimento(idade: int):
    from datetime import datetime
    ano_atual = datetime.now().year
    ano_nascimento = ano_atual - idade
    return {"anoNascimento": ano_nascimento}

@app.get("/imc")
def calcular_imc(altura: float, peso: float):
    imc = peso / (altura ** 2)
    status = ""
    
    if imc < 18.5:
        status = "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        status = "Peso normal"
    elif 25 <= imc < 29.9:
        status = "Sobrepeso"
    elif 30 <= imc < 34.9:
        status = "Obesidade I"
    elif 35 <= imc < 39.9:
        status = "Obesidade II"
    else:
        status = "Obesidade III"
    
    return {"imc": round(imc, 2), "status": status}