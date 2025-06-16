from models.item import Item
from models.database import SessionLocal

def criar_item(nome, descricao):
    session = SessionLocal()
    novo_item = Item(nome=nome, descricao=descricao)
    session.add(novo_item)
    session.commit()
    session.refresh(novo_item)
    session.close()
    return novo_item

def listar_itens():
    session = SessionLocal()
    itens = session.query(Item).all()
    session.close()
    return itens
