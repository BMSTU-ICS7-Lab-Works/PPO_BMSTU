import unittest
from unittest import mock
from schedule.ScheduleRepository import ScheduleRepository
from PPO.SessionManager import SessionManager
from excursions.ExcursionsRepository import ExcursionsRepository
from guides.GuidesRepository import GuidesRepository
from PPO.models import Schedule, Excursions, Users, Sights, Guides


class TestBase:
    def __init__(self):
        session_manager = SessionManager()
        try:
            session_manager.setRole(3)
        except:
            raise ValueError('Wrong Role')
        self.session = session_manager.getSession()

    def truncDb(self):
        self.session.execute('''TRUNCATE TABLE schedule CASCADE''')
        self.session.commit()

    def __del__(self):
        self.session.close()

class TestScheduleRepository(unittest.TestCase):

    def test_insert(self):
        Rep = ScheduleRepository(3)
        sch = Schedule(1, 'Пн', '13.30')
        self.assertEqual(Rep.insert(12), -1)
        id = Rep.insert(sch)
        self.assertNotEqual(id, -1)

        Rep.delete(id)

    def test_update(self):
        Rep = ScheduleRepository(3)
        id = Rep.insert(Schedule(1, 'Пн', '16.30'))
        # esli est
        self.assertEqual(Rep.update(id, Schedule(1, 'Пн', '13.30')), 1)
        # esli net
        self.assertEqual(Rep.update(-1, Schedule(1, 'Пн', '13.30')), 0)

        Rep.delete(id)

    def test_delete(self):
        Rep = ScheduleRepository(3)

        id = Rep.insert(Schedule(1, 'Пн', '15.30'))


        #esli est
        self.assertEqual(Rep.delete(id), 1)

        self.assertEqual(Rep.select(id), None)
        #esli net
        self.assertEqual(Rep.delete(-1), 0)

    def test_select(self):
        Rep = ScheduleRepository(3)
        self.assertEqual(Rep.select(-1), None)

        id = Rep.insert(Schedule(1, 'Пн', '15.30'))


        sch = Schedule(1, 'Пн', '15.30')
        getsch = Rep.select(id)
        self.assertEqual(getsch, sch)

        Rep.delete(id)

    def test_selectAll(self):

        Rep = ScheduleRepository(3)

        self.assertEqual(Rep.selectAll(), [])


if __name__ == '__main__':
    # guideRep = GuidesRepository(3)
    # guide = Guides('Дмитрий', 'Куликов', 'Алексеевич', 'Саранский', 'Австралопитек', 100)
    # guideRep.insert(guide)
    # Rep = ExcursionsRepository(3)
    # exc = Excursions('Гонка', 'форсаж', 1, 3000)
    # Rep.insert(exc)
    tb = TestBase()

    #tb.fillDb()

    TestScheduleRepository.main()
    tb.truncDb()
