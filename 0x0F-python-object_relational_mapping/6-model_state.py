#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa"""


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
        __tablename__ = 'states'
        id = Column(Integer, primary_key=True)
        name = Column(String(128), nullable=False)

    Base.metadata.create_all(engine)
