import services.database as db
from models.Cliente import Cliente

def Incluir(cliente):
    if cliente.nome and cliente.idade >= 0:
        sql = "INSERT INTO Cliente (cliNome, cliIdade, cliProfissao) VALUES (?, ?, ?)"
        values = (cliente.nome, cliente.idade, cliente.profissao)
        try:
            db.cursor.execute(sql, values)
            db.cnxn.commit()
            return True  # Inclusão bem-sucedida
        except Exception as e:
            db.cnxn.rollback()
            return False  # Inclusão falhou
    return False  # Valores inválidos
    
      
      
    
def selecionarById(id):
    db.cursor.execute("SELECT * FROM CLIENTE WHERE CLIID = ?", id)
    row = db.cursor.fetchone()
    if row:
        return Cliente(row[0], row[1], row[2], row[3])
    return None  # Cliente não encontrado

def Alterar(cliente):
    sql = "UPDATE Cliente SET cliNome = ?, cliIdade = ?, cliProfissao = ? WHERE cliId = ?"
    values = (cliente.nome, cliente.idade, cliente.profissao, cliente.id)
    count = db.cursor.execute(sql, values).rowcount
    db.cnxn.commit()

def Excluir(cliente_id):
    sql = "DELETE FROM Cliente WHERE cliId = ?"  # Alterado para corresponder ao nome da coluna na tabela
    values = (cliente_id,)
    db.cursor.execute(sql, values)
    db.cnxn.commit()
    
def selecionarTodos():
    db.cursor.execute("SELECT * FROM CLIENTE")
    customerList = [Cliente(*row) for row in db.cursor.fetchall()]
    return customerList

