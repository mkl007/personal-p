from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, inspect


Base = declarative_base()


class Usuarios(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    
    @property
    def serialize(self):

        return {
            'email': self.email,
            'name': self.name,
            'id': self.id
        }


class Tareas(Base):
    __tablename__ = 'tarea'

    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    description = Column(String(250), nullable=False)
    usuario_id = Column(Integer,ForeignKey('usuario.id'))
    usuario = relationship(Usuarios)

# We added this serialize function to be able to send JSON objects in a serializable format
    @property
    def serialize(self):

        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }


# comment this becouse it creates a new restaurantmenu.db, and we already have done it

# engine = create_engine('sqlite:///myDatabasepq.db', echo=True)
engine = create_engine('sqlite:///myDatabasepq.db')

inspector = inspect(engine)
table_exists = 'usuario' in inspector.get_table_names()

if table_exists:
    print("The database and tables exist.")
else:
    print("The database and tables do not exist.")
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
# #
