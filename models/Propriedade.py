from sqlalchemy import Column, Integer, String
from models.database import Base

class Propriedade(Base):
    __tablename__ = 'propriedade'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=True)

    def __repr__(self):
        return f"<Item(nome={self.nome}, descricao={self.descricao})>"
