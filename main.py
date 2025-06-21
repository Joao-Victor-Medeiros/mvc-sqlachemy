from models.database import Base, engine
from controllers.agricultor_controller import (
    criar_agricultor,
    listar_agricultores,
    buscar_agricultor_por_id,
    atualizar_agricultor,
    deletar_agricultor
)
from datetime import datetime

# Criar tabelas no banco
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    # Teste do CRUD de Agricultor
    try:
        # Criar agricultor
        print("\n=== Criando agricultor ===")
        novo_agricultor = criar_agricultor(
            nome="João Silva",
            contato="(11) 98765-4321",
            associacao_cooperativa="seagri",
            data_cadastro=datetime.now()
        )
        print(f"Agricultor criado: {novo_agricultor}")

        # Listar agricultores
        print("\n=== Listando agricultores ===")
        agricultores = listar_agricultores()
        for agricultor in agricultores:
            print(f"Agricultor: {agricultor}")

        # Buscar agricultor específico
        print("\n=== Buscando agricultor por ID ===")
        agricultor = buscar_agricultor_por_id(1)
        if agricultor:
            print(f"Agricultor encontrado: {agricultor}")

        # Atualizar agricultor
        print("\n=== Atualizando agricultor ===")
        agricultor_atualizado = atualizar_agricultor(
            agricultor_id=1,
            telefone="(11) 99999-9999"
        )
        print(f"Agricultor atualizado: {agricultor_atualizado}")

        # Deletar agricultor
        print("\n=== Deletando agricultor ===")
        resultado = deletar_agricultor(1)
        print(f"Agricultor deletado: {resultado}")

    except Exception as e:
        print(f"Erro: {str(e)}")
