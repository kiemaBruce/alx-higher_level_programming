#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""


if __name__ == "__main__":
    from model_city import City
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
        cities = session.query(City).order_by(City.id.asc()).all()
        for city in cities:
            city_state = session.query(
                                  State
                                 ).filter(
                                  State.id == city.state_id
                                 ).first()
            print(f'{city_state.name}: ({city.id}) {city.name}')
