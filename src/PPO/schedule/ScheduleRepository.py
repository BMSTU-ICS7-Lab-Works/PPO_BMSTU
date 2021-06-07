from PPO.SessionManager import SessionManager
from PPO.models import Schedule
from PPO.BaseRepository import BaseRepository


class ScheduleRepository(BaseRepository):
    def __init__(self, role):
        self.role = role
        session_manager = SessionManager()
        session_manager.setRole(role)
        self.session = session_manager.getSession()

    def __del__(self):
        self.session.close()

    def select(self, id):
        return self.session.query(Schedule).filter(Schedule.id == id).first()

    def selectAll(self):
        return self.session.query(Schedule).all()

    def insert(self, schedule):
        self.session.add(schedule)
        self.session.commit()

    def delete(self, id):
        self.session.query(Schedule).filter(Schedule.id == id).delete()
        self.session.commit()

    def update(self, id, schedule):
        self.session.query(Schedule).filter(Schedule.id == id).update({Schedule.id: Schedule.id,
                                                                   Schedule.day: schedule.day, Schedule.time: schedule.time})
        self.session.commit()