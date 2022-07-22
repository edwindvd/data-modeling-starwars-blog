import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    favoritos_id = Column(Integer, ForeignKey('favoritos.id'))
    name = Column(String(250), nullable=False)
    address1 = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    passsword = Column(String(10), nullable=False)

class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    # street_name = Column(String(250))
    # street_number = Column(String(250))
    # post_code = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    personajes_id = Column(Integer, ForeignKey('personajes.id'))
    # person = relationship(Person)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    # favoritos_id = Column(Integer, ForeignKey('favoritos.id'))
    personajes_id = Column(Integer, ForeignKey('personajes.id'))
    name = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)

class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    # favoritos_id = Column(Integer, ForeignKey('favoritos.id'))
    # planets_id = Column(Integer, ForeignKey('planets.id'))
    name = Column(String(250), nullable=False)
    clasificacion = Column(String(250), nullable=False)
    lenguaje = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram4.png')