#!/usr/bin/python3
"""Contains the class definition of a state and an instance Base =
declarative_base()
This script connects to a MySQL database and creates the `states` table if it
does not exist."""


if __name__ == "__main__":
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
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
    Base = automap_base()
    """Base.prepare(engine, autoload_with=engine)"""
    Base.prepare(engine)
    """Base.prepare(engine, reflect=True)"""
    State = Base.classes.states
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).all()
    for state in states:
        print(f'{state.id}: {state.name}')
