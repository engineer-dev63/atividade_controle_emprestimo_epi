db = {
    "colaboradores": []
}

# CREATE
def inserir_colaborador(nome, cargo, matricula):
    novo = {
        "id": len(db["colaboradores"]) + 1,
        "nome_completo": nome,
        "cargo": cargo,
        "matricula": matricula
    }
    db["colaboradores"].append(novo)


# READ
def listar_colaboradores():
    return db["colaboradores"]


# DELETE
def deletar_colaborador(id):
    for c in db["colaboradores"]:
        if c["id"] == id:
            db["colaboradores"].remove(c)
            return True
    return False


# UPDATE
def editar_colaborador(id, nome, cargo, matricula):
    for c in db["colaboradores"]:
        if c["id"] == id:
            c["nome_completo"] = nome
            c["cargo"] = cargo
            c["matricula"] = matricula
            return True
    return False


# SEARCH
def pesquisar_colaborador(nome):
    return [
        c for c in db["colaboradores"]
        if nome.lower() in c["nome_completo"].lower()
    ]