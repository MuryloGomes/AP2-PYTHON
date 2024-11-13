from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime

from modelos.base import Base

from sqlalchemy.orm import relationship

class Empregado(Base.Base, Base):
    __tablename__ = "empregado"
    nss = Column(Integer, primary_key=True, unique=True)
    pnome = Column(String(50), nullable=False)
    mnome = Column(String(50), unique=True,nullable=False)
    snome = Column(String(50), unique=True,nullable=False) 
    sexo = Column(String(15),nullable=False)
    dataNasc = Column(DateTime, nullable=False)
    salario = Column(Float, nullable=False)
    endereco = Column(String(50))
    #numeroDepartamento = Column(Integer, ForeignKey("Departamento.numero_depart"),unique=True)
    nssSupervisor = Column(Integer, ForeignKey(nss))
    # Relacionamento: Um empregado pertence a um departamento
    #departamento = relationship("Departamento", back_populates="empregados")