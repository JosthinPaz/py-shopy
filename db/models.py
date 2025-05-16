from .database import Base
from sqlalchemy import Column, Integer, String,Float,ForeignKey, Date,Boolean
from sqlalchemy.orm import relationship

class Categoria(Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(60))
    estado = Column(Boolean)
    fecha_creacion = Column(Date)

    #Relación uno a muchos con producto
    productos = relationship('Producto', back_populates='categoria')


class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(60))
    descripcion = Column(String(200))

    #Clave foranea 
    categoria_id = Column(Integer, ForeignKey('categorias.id'))
