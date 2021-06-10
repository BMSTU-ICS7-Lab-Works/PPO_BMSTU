from .models import Excursions, Schedule
from guides.guides_repositories import GuidesRepository
from .ExcursionsRepository import ExcursionsRepository, SightsExcursionsRepository, ScheduleRepository, SelectedExcursionsRepository

from sights.BL import getSightbyId



class ExcursionsService:
    def __init__(self,  role):
        self.role = role
        self.excursionRep = ExcursionsRepository(role)

    def addExcursion(self, name, description, guide_name, guide_surname, guide_patronymic, price):
        guideRep = GuidesRepository(self.role)
        guide = guideRep.findGuideByFIO(guide_name, guide_surname, guide_patronymic)
        self.excursionRep.insert(Excursions(name, description, guide.id, price))

    def getAllExcursions(self):
        return self.excursionRep.selectAll()

    def getExcursionById(self, id):
        return self.excursionRep.select(id)

    def delExcursionById(self, id):
        return self.excursionRep.delete(id)

    def updExcursionById(self, id, exc):
        return self.excursionRep.update(id, exc)

def addExcursion(name, description, guide_name, guide_surname, guide_patronymic, price, role):
    guideRep = GuidesRepository(role)
    guide = guideRep.findGuideByFIO(guide_name, guide_surname, guide_patronymic)
    del guideRep
    excursionRep = ExcursionsRepository(role)
    excursionRep.addExcursion(Excursions(name, description, guide.id, price))

def addSchedule(excursion_id, date, time, role):
    scheduleRep = ScheduleRepository(role)
    scheduleRep.addSchedule(Schedule(excursion_id, date, time))

def addSelectedExcursionsRel(userId, scheduleId, date, role):
    selectedRep = SelectedExcursionsRepository(role)
    selectedRep.addRel(userId, scheduleId, date)

def addSightExcursionRel(sight_id, exc_id, role):
    SightsExcursionsRep = SightsExcursionsRepository(role)
    SightsExcursionsRep.addRel(sight_id, exc_id)

def getExcursionByName(name, role):
    excursionsRep = ExcursionsRepository(role)
    return excursionsRep.findExcursionByName(name)


def getScheduleByExcursion(excursion_name, role):
    excursion = getExcursionByName(excursion_name, role)
    ScheduleRep = ScheduleRepository(role)
    return ScheduleRep.findScheduleByExcursion(excursion)

def getAllExcursions(role):
    excursionRep = ExcursionsRepository(role)
    return excursionRep.findAllExcursions()

def getSightsbyExcursion(excursion, role):
    SERep = SightsExcursionsRepository(role)
    res = SERep.getSightsbyExcursion(excursion)

    fres = []
    for el in res:
        for id in el:
            fres.append(getSightbyId(id, role))
    return fres

def delPastExcursions(role):
    ScheduleRep = ScheduleRepository(role)
    return ScheduleRep.deletePastExcursions()


def filltime():
    res = {}
    for i in range(0, 24):
        if i < 10:
            res['0' + str(i) +':00'] = '0' + str(i) +':00'
            res['0' + str(i) + ':30'] = '0' + str(i) +':30'
        else:
            res[str(i) +':00'] = str(i) +':00'
            res[str(i) +':30'] = str(i) +':30'
    return res.items()
