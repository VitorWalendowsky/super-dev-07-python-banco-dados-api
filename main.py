from fastapi import FastAPI

app = FastAPI()

@app.get("/greetings")
def saudacoes():
    return {"mensagem: Hello World"}

#tudo depois da ? se chama query param
#/calculadora?numero1=9&numero2=1

@app.ger("/calculadora")
def calculadora(numero1: int, numero2: int):
    soma = numero1 + numero2
    return {"resultado": soma}


#fastapi dev main.py
# 127.0.0.1:8000\greetings
# 127.0.0.1:8000\docs