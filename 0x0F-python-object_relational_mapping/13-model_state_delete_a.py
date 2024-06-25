#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter a from the
database hbtn_0e_6_usa"""


if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import collate, create_engine, delete, update
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
        stmt = delete(State).where(State.name.like('%a%'))
        session.execute(stmt)
        session.commit()
