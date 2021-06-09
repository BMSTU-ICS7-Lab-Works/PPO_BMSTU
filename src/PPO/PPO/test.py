import unittest
from schedule.ScheduleRepository import ScheduleRepository
from excursions.ExcursionsRepository import ExcursionsRepository
from guides.GuidesRepository import GuidesRepository
from PPO.models import Schedule, Excursions, Users, Sights, Guides
class TestScheduleRepository(unittest.TestCase):

    def test_insert(self):
        # Rep = ScheduleRepository(3)
        # self.assertEqual(Rep.selectAll(), [])
        # self.assertEqual(Rep.select(100), None)
        # sch = Schedule(12, 1, 'Пн', '13.30')
        # self.assertEqual(Rep.insert(12), -1)
        # self.assertEqual(Rep.insert(sch), 0)
        # getsch = Rep.select(7)
        # self.assertEqual(getsch, sch)
        # sch.time = '14.30'
        # Rep.update(7, sch)
        # self.assertEqual(Rep.select(7), sch)
        # Rep.delete(7)
        # self.assertEqual(Rep.select(7), None)
        2

    def test_update(self):
        2

    def test_delete(self):
        2

    def test_select(self):
        Rep = ScheduleRepository(3)
        self.assertEqual(Rep.select(100), None)
        sch = Schedule(100, 1, 'Пн', '13.30')
        self.assertEqual(Rep.insert(12), -1)
        self.assertEqual(Rep.insert(sch), 0)
        getsch = Rep.select(7)
        self.assertEqual(getsch, sch)

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
    TestScheduleRepository.main()