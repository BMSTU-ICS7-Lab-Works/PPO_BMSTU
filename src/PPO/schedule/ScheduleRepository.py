from PPO.SessionManager import SessionManager
from PPO.models import Schedule
from PPO.BaseRepository import BaseRepository
import logging


class ScheduleRepository(BaseRepository):
    def __init__(self, role):
        self.role = role
        session_manager = SessionManager()
        try:
            session_manager.setRole(role)
        except:
            logging.error('Wrong Role')
            raise ValueError('Wrong Role')
        self.session = session_manager.getSession()
        logging.info('Get session with role ', role)

    def __del__(self):
        self.session.close()

    def select(self, id):
        logging.info('select query with id = ', id)
        return self.session.query(Schedule).filter(Schedule.id == id).first()

    def selectAll(self):
        logging.info('selectAll query worked successfully')
        return self.session.query(Schedule).all()

    def insert(self, schedule):
        try:
            self.session.add(schedule)
        except:
            logging.warning('insertion failed!')
            return -1
        logging.info('successfully insert schedule')
        self.session.commit()
        return 0

    def delete(self, id):
        self.session.query(Schedule).filter(Schedule.id == id).delete()
        self.session.commit()
        logging.info('deleted schedule with id = ', id)

    def update(self, id, schedule):
        self.session.query(Schedule).filter(Schedule.id == id).update({Schedule.id: Schedule.id,
                                                                   Schedule.day: schedule.day,
                                                                           Schedule.time: schedule.time})
        self.session.commit()
        logging.info('updated schedule with id = ', id)