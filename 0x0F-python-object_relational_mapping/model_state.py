#!/usr/bin/python3
"""Contains the class definition of a state and an instance Base =
declarative_base()
This script connects to a MySQL database and creates the `states` table if it
does not exist."""


if __name__ == "__main__":
    from sqlalchemy import Column, Integer, String
    from sqlalchemy import create_engine
    from sqlalchemy.orm import declarative_base
    """from sqlalchemy.ext.declarative import declarative_base"""
    from sqlalchemy.orm import sessionmaker
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
    Base = declarative_base()

    class State(Base):
        """
        Definition of the State which defines of the states table

        Attributes:
            __tablename__ (str): the name of the table that this class defines.
            id (int): primary key of the table which auto-increments.
            name (str): the name of the state.

        """
        __tablename__ = 'states'
        id = Column(Integer, primary_key=True)
        name = Column(String(128), nullable=False)

    Base.metadata.create_all(engine)
