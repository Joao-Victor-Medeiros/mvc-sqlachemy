from models.Agricultor import Agricultor
from models.database import SessionLocal

def criar_agricultor(nome, contato, associacao_cooperativa, data_cadastro):
    session = SessionLocal()
    try:
        novo_agricultor = Agricultor(
            nome=nome,
            contato=contato,
            associacao_cooperativa=associacao_cooperativa,
            data_cadastro=data_cadastro
        )
        session.add(novo_agricultor)
        session.commit()
        session.refresh(novo_agricultor)
        return novo_agricultor
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def listar_agricultores():
    session = SessionLocal()
    try:
        return session.query(Agricultor).all()
    finally:
        session.close()

def buscar_agricultor_por_id(agricultor_id):
    session = SessionLocal()
    try:
        return session.query(Agricultor).filter(Agricultor.id == agricultor_id).first()
    finally:
        session.close()

def atualizar_agricultor(agricultor_id, nome=None, cpf=None, endereco=None, telefone=None):
    session = SessionLocal()
    try:
        agricultor = session.query(Agricultor).filter(Agricultor.id == agricultor_id).first()
        if agricultor:
            if nome is not None:
                agricultor.nome = nome
            if cpf is not None:
                agricultor.cpf = cpf
            if endereco is not None:
                agricultor.endereco = endereco
            if telefone is not None:
                agricultor.telefone = telefone
            session.commit()
            session.refresh(agricultor)
        return agricultor
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def deletar_agricultor(agricultor_id):
    session = SessionLocal()
    try:
        agricultor = session.query(Agricultor).filter(Agricultor.id == agricultor_id).first()
        if agricultor:
            session.delete(agricultor)
            session.commit()
            return True
        return False
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
