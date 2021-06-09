from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class SessionManager():
    admin_engine = create_engine("postgresql+psycopg2://postgres:1@localhost/PPO")
    unlogged_engine = create_engine("postgresql+psycopg2://unlogged_user:unlogged_user@localhost/PPO")
    logged_engine = create_engine("postgresql+psycopg2://logged_user:logged_user@localhost/PPO")
    guide_engine = create_engine("postgresql+psycopg2://guide:guide@localhost/PPO")

    def __init__(self, role=0):
        self.role = role
        self.sessionmaker = sessionmaker(bind=self.unlogged_engine)
        self.session = self.sessionmaker()

    def setRole(self, role):
        if 0 <= role <= 3:
            self.role = role
        else:
            raise Exception("Wrong role")

    def getSession(self):
        if self.role == 0:
            self.sessionmaker = sessionmaker(bind=self.unlogged_engine)
            self.session = self.sessionmaker()
            return self.session
        elif self.role == 1:
            self.sessionmaker = sessionmaker(bind=self.logged_engine)
            self.session = self.sessionmaker()
            return self.session
        elif self.role == 2:
            self.sessionmaker = sessionmaker(bind=self.guide_engine)
            self.session = self.sessionmaker()
            return self.session
        elif self.role == 3:
            self.sessionmaker = sessionmaker(bind=self.admin_engine)
            self.session = self.sessionmaker()
            return self.session
        else:
            raise Exception("Wrong role")

