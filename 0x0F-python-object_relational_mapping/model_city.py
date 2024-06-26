#!/usr/bin/python3
"""Contains the class definition of a City"""


from model_state import State
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, String

Base = declarative_base()


class City(Base):
    """
    Definition of City which defines the cities table.

    Attributes:
        __tablename__ (str): the name of the table defined by the class.
        id (int): primary key of the cities table. It auto-increments, is
                  unique and cannot be null.
        name (str): the name of the city. It cannot be NULL and has a maximum
                    length of 128 characters.
        state_id: the id of the State in which the city is found. This is a
        foreign key to states.id
        state: relationship between cities table and states table.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
    """state = relationship("State", backref="cities")"""


"""
State.city = relationship("City", backref="states")
"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    import sys

    user = sys.argv[1]
    password = sys.argv[2]
    host = "localhost"
    port = 3306
    database = sys.argv[3]
    engine = create_engine(
            (
                f'mysql+mysqlconnector://{user}:{password}@{host}'
                f':{port}/{database}'
                ),
            pool_pre_ping=True
            )
    Base.metadata.create_all(engine)
