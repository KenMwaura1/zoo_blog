from app.commands import db_config
from manage import app
from app.commands import db
from dotenv import load_dotenv
from dataclasses import dataclass
import os

load_dotenv()

db_config(app)

@dataclass
class Database:
    engine = db.create_engine(os.environ.get('SQLALCHEMY_DATABASE_URI', ))
    model = None

    @staticmethod
    def initialize():
        session = db.session(Database.engine)

    @staticmethod
    def insert(self, data):
        self.session.add(data)
        self.session.commit()

    @staticmethod
    def delete(self, data):
        self.session.delete(data)
        self.session.commit()

    @staticmethod
    def find_one(self, table, query, data):
        self.session.query(table).filter_by(query=data).first()

    @staticmethod
    def find_all(self, table, query, data):
        self.session.query(table).filter_by(query=data).all()
