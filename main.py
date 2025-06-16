from models.database import Base, engine
from controllers.item_controller import criar_item, listar_itens

# Criar tabelas no banco
Base.metadata.create_all(bind=engine)

# Criar novo item
criar_item("Teclado", "Teclado mecânico USB")
criar_item("Monitor", "Monitor LED 24 polegadas")

# Listar todos os itens
itens = listar_itens()
for item in itens:
    print(item)
