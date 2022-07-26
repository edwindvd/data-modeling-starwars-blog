import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    address1 = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    passsword = Column(String(10), nullable=False)
    favoritos = relationship('Favoritos')

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    personaje_id = Column(Integer, ForeignKey('personajes.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=True)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    favoritos = relationship('Favoritos')
    name = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    favoritos = relationship('Favoritos')
    name = Column(String(250), nullable=False)
    clasificacion = Column(String(250), nullable=False)
    lenguaje = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')