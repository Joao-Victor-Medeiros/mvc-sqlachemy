from sqlalchemy import Column, Integer, String, DateTime
from models.database import Base

class Agricultor(Base):
    __tablename__ = 'agricultor'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    contato= Column(String, nullable=True)
    associacao_cooperativa= Column(String, nullable=True)
    data_cadastro = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<Agricultor(nome={self.nome}, associacao_cooperativa={self.associacao_cooperativa})>"
