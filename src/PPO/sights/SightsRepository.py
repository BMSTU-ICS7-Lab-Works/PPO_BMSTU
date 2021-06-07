#getid
#update
#deletebyId
#getAll
from PPO.SessionManager import SessionManager
from PPO.models import Sights
from PPO.BaseRepository import BaseRepository


class SightsRepository(BaseRepository):
    def __init__(self, role):
        self.role = role
        session_manager = SessionManager()
        session_manager.setRole(role)
        self.session = session_manager.getSession()

    def __del__(self):
        self.session.close()

    # def findSightByName(self, name):
    #     return self.session.query(Sights).filter(Sights.name == name).first()

    def select(self, id):
        return self.session.query(Sights).filter(Sights.id == id).first()

    def selectAll(self):
        return self.session.query(Sights).all()

    def insert(self, sight):
        self.session.add(sight)
        self.session.commit()

    def delete(self, id):
        self.session.query(Sights).filter(Sights.id == id).delete()
        self.session.commit()

    def update(self, id, sight):
        self.session.query(Sights).filter(Sights.id == id).update({Sights.id: sight.id, Sights.name: sight.name,
                                                                   Sights.build_date: sight.build_date, Sights.type: sight.type,
                                                                   Sights.author: sight.author, Sights.description: sight.description})
        self.session.commit()