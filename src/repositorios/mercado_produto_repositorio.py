from src.banco_dados import conectar


def cadastrar(nome: str, id_categoria: int):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "insert into produtos (nome, id_categorias) values (%s, %s)"
    dados = (nome, id_categoria)
    cursor.execute(sql, dados)
    conexao.commit()
    cursor.close()
    conexao.close()

    

def editar(id: int, nome: str):
    pass



def apagar(id: int) -> int:
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "DELETE FROM produtos where ID = %s"
    dados = (id,)
    cursor.execute(sql,dados)
    conexao.commit()
    linhas_afetadas = cursor.rowcount
    cursor.close()
    conexao.close()
    return linhas_afetadas

def obter_todos():
    pass