from PPO.models import Schedule
from schedule.ScheduleRepository import ScheduleRepository

class ScheduleService:
    def __init__(self,  role):
        self.role = role
        self.scheduleRep = ScheduleRepository(role)

    def addSchedule(self, excursion_id, date, time, id=None):
        return self.scheduleRep.insert(Schedule(excursion_id, date, time, id))

    def getAllSchedules(self):
        return self.scheduleRep.selectAll()

    def getScheduleById(self, id):
        return self.scheduleRep.select(id)

    def delScheduleById(self, id):
        return self.scheduleRep.delete(id)

    def updScheduleById(self, id, exc):
        return self.scheduleRep.update(id, exc)

    def getScheduleByExcursion(self, excursion_id):
        scheduleRep = ScheduleRepository(self.role)
        allsch = scheduleRep.selectAll()
        scheduleOfExc = []
        for el in allsch:
            if el.excursion == excursion_id:
                scheduleOfExc.append(el)
        return scheduleOfExc

if __name__ == '__main__':
    schRep = ScheduleRepository(3)
    #schRep.insert(Schedule(1, "2012-03-23", "15:30"))
    print(schRep.update(5, Schedule(1, "2012-03-23", "17:30")))