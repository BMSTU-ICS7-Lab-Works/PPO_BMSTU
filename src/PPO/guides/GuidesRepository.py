from PPO.SessionManager import SessionManager
from PPO.models import Guides
from PPO.BaseRepository import BaseRepository


class GuidesRepository(BaseRepository):
    def __init__(self, role):
        self.role = role
        session_manager = SessionManager()
        session_manager.setRole(role)
        self.session = session_manager.getSession()

    def __del__(self):
        self.session.close()

    def select(self, id):
        return self.session.query(Guides).filter(Guides.id == id).first()

    def selectAll(self):
        return self.session.query(Guides).all()

    def insert(self, guide):
        self.session.add(guide)
        self.session.commit()

    def delete(self, id):
        self.session.query(Guides).filter(Guides.id == id).delete()
        self.session.commit()

    def update(self, id, guide):
        self.session.query(Guides).filter(Guides.id == id).update({Guides.id: guide.id, Guides.first_name: guide.first_name,
                                                                   Guides.last_name: guide.last_name, Guides.patronymic: guide.patronymic,
                                                                   Guides.qualification: guide.qualification, Guides.biography: guide.biography,
                                                                   Guides.experience: guide.experience})
        self.session.commit()