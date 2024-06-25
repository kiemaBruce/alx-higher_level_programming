#!/usr/bin/python3
"""Changes the name of a State object from the database hbtn_0e_6_usa"""


if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import collate, create_engine, update
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
        stmt = update(State).where(State.id == 2).values(name='New Mexico')
        session.execute(stmt)
        session.commit()
