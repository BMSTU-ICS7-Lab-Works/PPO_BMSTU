from PPO.SessionManager import SessionManager
from PPO.models import Excursions
from PPO.BaseRepository import BaseRepository


class ExcursionsRepository(BaseRepository):
    def __init__(self, role):
        self.role = role
        session_manager = SessionManager()
        session_manager.setRole(role)
        self.session = session_manager.getSession()

    def __del__(self):
        self.session.close()

    def select(self, id):
        return self.session.query(Excursions).filter(Excursions.id == id).first()

    def selectAll(self):
        return self.session.query(Excursions).all()

    def insert(self, excursion):
        self.session.add(excursion)
        self.session.commit()

    def delete(self, id):
        self.session.query(Excursions).filter(Excursions.id == id).delete()
        self.session.commit()

    def update(self, id, excursion):
        self.session.query(Excursions).filter(Excursions.id == id).update({Excursions.id: excursion.id, Excursions.name: excursion.name,
                                                                   Excursions.description: excursion.description, Excursions.guide: excursion.guide,
                                                                   Excursions.price: excursion.price})
        self.session.commit()