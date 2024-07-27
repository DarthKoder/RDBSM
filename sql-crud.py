from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.orm import declarative_base, sessionmaker


# executing the instructions from the "chinook" database 
db = create_engine("postgresql:///chinook")
base = declarative_base()



# create a class-based model for the "programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)
    
    
# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our enging (the db)
Session = sessionmaker(db)
#opens an actual session by calling the Session() subclass defined above
session = Session()

#creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating our Programmer table
ada_lovelace = Programmer(
    first_name = "Ada",
    last_name = "Lovbelace",
    gender = "Female",
    nationality = "British",
    famous_for = "First Programmer"
)

alan_turing = Programmer(
    first_name = "Alan",
    last_name = "Turing",
    gender = "Male",
    nationality = "British",
    famous_for = "Modern Computing"
)

grace_hopper = Programmer(
    first_name = "Grace",
    last_name = "Hopper",
    gender = "Female",
    nationality = "American",
    famous_for = "COBOL language"
)

margaret_hamilton = Programmer(
    first_name = "Margaret",
    last_name = "Hamilton",
    gender = "Female",
    nationality = "American",
    famous_for = "Apollo 11"
)

bill_gates = Programmer(
    first_name = "Bill",
    last_name = "Gates",
    gender = "Male",
    nationality = "American",
    famous_for = "Microsoft"
)

tim_berners_lee = Programmer(
    first_name = "Tim",
    last_name = "Berners-Lee",
    gender = "Male",
    nationality = "British",
    famous_for = "World Wide Web"
)

darth_koder = Programmer(
    first_name = "Darth",
    last_name = "Koder",
    gender = "Male",
    nationality = "British",
    famous_for = "The Sith Lord of Coders"
)

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(darth_koder)

# commit our session to the database
session.commit()

# query the database to find all Programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " +programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
