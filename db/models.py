from .database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Boolean, DateTime, Text
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
    
    #Relación uno a muchos con producto
    item = relationship('Item', back_populates='Productos')


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    serial = Column(String(60))
    fecha_ingreso = Column(Date)
    #Clave foranea 
    productos_id = Column(Integer, ForeignKey('productos.id'))
    

class Usuario(Base):
    __tablename__ = 'usuarios'
    id_usuario = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    correo = Column(String(100))
    contraseña = Column(String(255))
    rol_id = Column(Integer, ForeignKey('roles.id_rol'))
    estado = Column(Boolean)
    fecha_registro = Column(Date)

    rol = relationship('Rol', back_populates='usuarios')


class Rol(Base):
    __tablename__ = 'roles'
    id_rol = Column(Integer, primary_key=True)
    nombre = Column(String(50))

    usuarios = relationship('Usuario', back_populates='rol')


class Inventario(Base):
    __tablename__ = 'inventarios'
    id_inventario = Column(Integer, primary_key=True)
    producto_id = Column(Integer, ForeignKey('productos.id'))
    cantidad_actual = Column(Integer)
    alerta_stock = Column(Integer)

    producto = relationship('Producto')


class Pedido(Base):
    __tablename__ = 'pedidos'
    id_pedido = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('usuarios.id_usuario'))
    fecha_pedido = Column(DateTime)
    estado = Column(String(50))
    total = Column(Float)

    cliente = relationship('Usuario')
    detalles = relationship('DetallePedido', back_populates='pedido')


class DetallePedido(Base):
    __tablename__ = 'detalle_pedido'
    id_detalle = Column(Integer, primary_key=True)
    pedido_id = Column(Integer, ForeignKey('pedidos.id_pedido'))
    producto_id = Column(Integer, ForeignKey('productos.id'))
    cantidad = Column(Integer)
    precio_unitario = Column(Float)

    pedido = relationship('Pedido', back_populates='detalles')
    producto = relationship('Producto')


class Reseña(Base):
    __tablename__ = 'reseñas'
    id_reseña = Column(Integer, primary_key=True)
    producto_id = Column(Integer, ForeignKey('productos.id'))
    cliente_id = Column(Integer, ForeignKey('usuarios.id_usuario'))
    calificación = Column(Integer)
    comentario = Column(Text)
    fecha = Column(DateTime)

    producto = relationship('Producto')
    cliente = relationship('Usuario')
