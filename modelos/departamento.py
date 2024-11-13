from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from modelos.base import Base

from sqlalchemy.orm import relationship

class Departamento(Base.Base, Base):
    __tablename__ = "departamento"
    numeroDepart = Column(Integer,primary_key=True, unique=True)
    nome = Column(String(50),unique=True, nullable=False)
    numeroEmpregado = Column(Integer,nullable=False, unique=True)
    #nssEmpregrado = Column(Integer,ForeignKey("Empregado.nss"))
    dataInicio = Column(DateTime)
    # Relacionamento: Um departamento pode ter muitos empregados
    #empregados = relationship("Empregado", back_populates="departamento")
