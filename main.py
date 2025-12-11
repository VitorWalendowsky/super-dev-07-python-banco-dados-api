from fastapi import FastAPI, HTTPException
from datetime import datetime

from classes import AlunoCalcularFrequencia, AlunoCalcularMedia, CarroAutonomia, CategoriaCriar, CategoriaEditar, PedidoTotal, ProdutoDesconto
from src.repositorios import mercado_categoria_repositorio

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
    



@app.post("/aluno/calcular-media")
def calcular_media(aluno_dados: AlunoCalcularMedia):
    nota1 = aluno_dados.nota1
    nota2 = aluno_dados.nota2
    nota3 = aluno_dados.nota3
    media = (nota1 + nota2 + nota3) / 3
    return {
        "media": media,
        "nome_completo": aluno_dados.nome_completo
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
def calcular_ano_nascimento(idade: int, ano_atual: int):
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



# exemplo1 Criar um endpoint do tipo POST aluno/calcular-frequencia
# Payload:
#  nome do caluno
#  quantidade letivos
#  quantidade presenças
# 
# qtd letivos 100
# qtd presencas 
# (qtd presencas * 100) / qtd letivos


@app.post("/aluno/calcular-frequencia")
def calcular_frequencia(aluno_dados: AlunoCalcularFrequencia):
    qtd_letivos = aluno_dados.qtd_letivos
    qtd_presencas = aluno_dados.qtd_presencas
    frequencia = (qtd_presencas * 100) / qtd_letivos
    return{
        "frequencia": frequencia,
        "nome_completo": aluno_dados.nome_completo
    }

# Ex.2 Criar um endpoint do tipo POST /produto/calcular-desconto
# Criar uma classe ProdutoDesconto
#   nome
#   preco_original
#   percentual_desconto
# Payload:
#   nome do produto
#   preço original
#   percentual de desconto (0 a 100)
#
# Fórmulas:
#   valor_desconto = (preco_original * percentual_desconto) / 100
#   preco_final = preco_original - valor_desconto

@app.post("/produto/calcular-desconto")
def calcular_desconto(produto_dados: ProdutoDesconto):
    valor_desconto = (produto_dados.preco_original * produto_dados.percentual_desconto) / 100
    preco_final = produto_dados.preco_original - valor_desconto
    return{
        "nome": produto_dados.nome,
        "preco_original": produto_dados.preco_original,
        "percentual_desconto": produto_dados.percentual_desconto,
        "valor_desconto": valor_desconto,
        "preco_final": preco_final
    }


# Ex.3 Criar um endpoint do tipo POST /carro/calcular-autonomia
# Criar uma classe CarroAutonomia
#   modelo
#   consumo_por_litro
#   quantidade_combustivel
# Payload:
#   modelo do carro
#   consumo por litro (km/l)
#   quantidade de combustível no tanque (litros)
#
# Fórmula:
#   autonomia = consumo_por_litro * quantidade_combustivel

@app.post("/carro/calcular-autonomia")
def calcular_autonomia(carro_dados: CarroAutonomia):
    autonomia = carro_dados.consumo_por_litro * carro_dados.quantidade_combustivel0
    return{
        "modelo": carro_dados.modelo,
        "consumo_por_litro": carro_dados.consumo_por_litro,
        "quantidade_combustivel": carro_dados.quantidade_combustivel,
        "autonomia": autonomia
    }


# Ex.4 Criar um endpoint do tipo POST /pedido/calcular-total
# Criar uma classe PedidoTotal
#   descricao
#   quantidade
#   valor_unitario
# Payload:
#   descrição do pedido
#   quantidade de itens
#   valor unitário
#
# Fórmulas:
#   subtotal = quantidade * valor_unitario
#   taxa = subtotal * 0.05  (5% de taxa de serviço)
#   total = subtotal + taxa

@app.post("/pedido/calcular-total")
def calcular_total(pedido_dados: PedidoTotal):
    subtotal = pedido_dados.quantidade * pedido_dados.preco_unitario
    taxa = subtotal * 0.05
    total = subtotal + taxa
    return{
        "descricao": pedido_dados.descricao,
        "quanttidade": pedido_dados.quantidade,
        "preco_unitario": pedido_dados.preco_unitario,
        "subtotal": subtotal,
        "taxa": taxa,
        "total": total
    }




#Carregar todas as categorias

@app.get("/api/v1/categorias", tags=["Categorias"])
def listar_categorias():
    categorias = mercado_categoria_repositorio.obter_todos()
    return categorias


@app.post("/api/v1/categorias", tags=["Categorias"])
def cadastrar_categoria(categoria: CategoriaCriar):
    mercado_categoria_repositorio.cadastrar(categoria.nome)
    return {"mensagem": "Categoria cadastrada com sucesso!"}


# Put - /api/v1/categorias/10
# metodo delete

@app.delete("/api/v1/categorias/{id}", tags=["Categorias"])
def apagar_categoria(id: int):
    linhas_afetadas = mercado_categoria_repositorio.apagar(id)
    if linhas_afetadas == 0:
        raise HTTPException(
            status_code=404,
            detail="Categoria não encontrada"
        )
    return {"mensagem": "Categoria apagada com sucesso!"}


@app.put("/api/v1/categorias/{id}", tags=["Categorias"])
def alterar_categoria(id: int, categoria: CategoriaEditar):
    linhas_afetadas = mercado_categoria_repositorio.atualizar(id, categoria.nome)
    if linhas_afetadas == 0:
        raise HTTPException(
            status_code=404,
            detail="Categoria não encontrada"
        )
    return {"mensagem": "Categoria atualizada com sucesso!"}