import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)


class Character(Base):
    __tablename__ = "character"
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(250), nullable=True)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=True)


class FavoriteCharacter(Base):
    __tablename__ = "favoritecharacter"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    character = relationship(Character)
    user = relationship(User)

class Planet(Base):
    __tablename__ = "planet"
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    population = Column(String(250), nullable=True)
    climate = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)



class FavoritePlanet(Base):
    __tablename__ = "favoriteplanet"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planet = relationship(Planet)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')