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
        logging.info("session closed")

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
        try:
            self.session.commit()
        except:
            logging.error('Commit failure in insert schedule')
            return -1
        logging.info('Succesfully commited insert schedule')
        self.session.refresh(schedule)
        return schedule.id

    def delete(self, id):
        num_del = self.session.query(Schedule).filter(Schedule.id == id).delete()
        if num_del == 1:
            logging.info('deleted schedule with id = ', id)
        else:
            logging.info('nothing deleted, id does not exist')
        self.session.commit()
        #logging.info('deleted schedule with id = ', id)
        return num_del

    def update(self, id, schedule):
        num_upd = self.session.query(Schedule).filter(Schedule.id == id).update({Schedule.id: Schedule.id,
                                                                   Schedule.day: schedule.day,
                                                                           Schedule.time: schedule.time})
        if num_upd == 0:
            logging.info('does not update schedule with id = ', id, ', such id does not exists')
        else:
            logging.info('succesfully updated schedule with id = ', id)
        self.session.commit()
        return num_upd