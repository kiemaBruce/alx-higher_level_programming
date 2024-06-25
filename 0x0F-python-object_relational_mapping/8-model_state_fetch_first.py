#!/usr/bin/python3
"""Contains the class definition of a state and an instance Base =
declarative_base()
This script connects to a MySQL database and creates the `states` table if it
does not exist."""


if __name__ == "__main__":
    from model_state import Base, State
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
    Session = sessionmaker(bind=engine)
    with Session() as session:
        first_state = session.query(State).first()
        if first_state is None:
            print('Nothing')
        else:
            print(f'{first_state.id}: {first_state.name}')
