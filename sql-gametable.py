from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.orm import declarative_base, sessionmaker


# executing the instructions from the "chinook" database 
db = create_engine("postgresql:///chinook")
base = declarative_base()



# create a class-based model for the "Games" table
class BestGames(base):
    __tablename__ = "BestGames"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    release_date = Column(Integer)
    device_on_release = Column(String)
    rating_out_of_10 = Column(Integer)
    
    
# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our enging (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)



# creating our best games table
sonic = BestGames(
    name = "Sonic the Hedghog",
    release_date = 1991,
    device_on_release = "Sega Megadrive",
    rating_out_of_10 = 10
)

super_mario_bros = BestGames(
    name = "Super Mario Bros Deluxe",
    release_date = 1999,
    device_on_release = "Game Boy Colour",
    rating_out_of_10 = 8
)

mario_kart_64 = BestGames(
    name = "Mario Kart 64",
    release_date = 1996,
    device_on_release = "Nintendo 64",
    rating_out_of_10 = 10
)

gta_san_andreas = BestGames(
    name = "Grand Theft Auto: San Andreas",
    release_date = 2004,
    device_on_release = "Playstation2",
    rating_out_of_10 = 10
)

cod_4 = BestGames(
    name = "Call of Duty: Modern Warfare",
    release_date = 2007,
    device_on_release = "PC | Xbox 360 | Playstation 3",
    rating_out_of_10 = 10
)

skyrim = BestGames(
    name = "Elder Scrolls V: Skyrim",
    release_date = 2011,
    device_on_release = "PC | Xbox 360 | Playstation 3",
    rating_out_of_10 = 10
)

elder_scrolls_online = BestGames(
    name = "Elder Scrolls V: Online",
    release_date = 2014,
    device_on_release = "PC | Xbox One | Playstation 4",
    rating_out_of_10 = 10
)

valorant = BestGames(
    name = "Valorant",
    release_date = 2020,
    device_on_release = "PC",
    rating_out_of_10 = 10
)

overwatch = BestGames(
    name = "Overwatch",
    release_date = 2016,
    device_on_release = "PC",
    rating_out_of_10 = 9
)

assassins_creed_2 = BestGames(
    name = "Assassins Creed II",
    release_date = 2009,
    device_on_release = "PC | Xbox 360 | Playstation 3",
    rating_out_of_10 = 10
)


# add each instance of our programmers to our session
session.add(sonic)
session.add(super_mario_bros)
session.add(mario_kart_64)
session.add(gta_san_andreas)
session.add(cod_4)
session.add(skyrim)
session.add(elder_scrolls_online)
session.add(valorant)
session.add(overwatch)
session.add(assassins_creed_2)

# committhe sessions to the database
session.commit()

# query the database to find all Programmers
bestgames = session.query(BestGames)
for game in bestgames:
    print(
        game.id,
        game.name,
        game.release_date,
        game.device_on_release,
        game.rating_out_of_10,
        sep = " | "
    )