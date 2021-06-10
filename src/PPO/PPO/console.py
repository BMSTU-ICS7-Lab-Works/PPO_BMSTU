from PPO.models import Schedule
from schedule.ScheduleService import ScheduleService

class Interface():
    def choice(self):
        print('Меню: ')
        print('1. Добавить расписание')
        print('2. Получить расписание по Id')
        print('3. Получить все расписания')
        print('4. Удалить расписание по Id')
        print('5. Обновить расписание по Id')
        print('6. Получить расписание экскурсии по его Id')
        print('0. Завершить работу')
        choice = int(input('Введите значение: '))
        if choice == 1:
            self.addSchedule()
        elif choice == 2:
            self.getScheduleById()
        elif choice == 3:
            self.getAllSchedules()
        elif choice == 4:
            self.delScheduleById()
        elif choice == 5:
            self.updScheduleById()
        elif choice == 6:
            self.getScheduleByExcursion()
        elif choice == 0:
            return 0
        else:
            print('Некорректный ввод!')
        self.choice()


    def addSchedule(self):
        service = ScheduleService(3)
        print('Хотите указать Id')
        print('0. Нет')
        print('1. Да')
        id_choice = int(input())
        id = None
        if id_choice == 1:
            id = int(input('Введите Id: '))
        elif id_choice != 0:
            print('Введено неверное значение!')
            self.addSchedule()

        id_exc = int(input('Укажите Id экскурсии, к которому вы хотите привязать расписание: '))

        date = input('Введите дату в формате YYYY-mm-dd: ')
        time = input('Введите время в формате HH:MM : ')
        id = service.addSchedule(id_exc, date, time, id)
        print('Запись была добавлена с Id ', id)
        return id

    def getScheduleById(self):
        service = ScheduleService(3)
        id = int(input('Введите Id расписания: '))
        print(service.getScheduleById(id))

    def getAllSchedules(self):
        service = ScheduleService(3)
        print(service.getAllSchedules())

    def delScheduleById(self):
        service = ScheduleService(3)
        id = int(input('Введите Id расписания: '))
        return service.delScheduleById(id)

    def updScheduleById(self):
        service = ScheduleService(3)
        id = int(input('Введите Id расписания: '))

        id_exc = int(input('Укажите новое Id экскурсии, к которому вы хотите привязать расписание: '))

        date = input('Введите новую дату в формате YYYY-mm-dd: ')
        time = input('Введите новое время в формате HH:MM : ')
        return service.updScheduleById(id, Schedule(id_exc, date, time))

    def getScheduleByExcursion(self):
        service = ScheduleService(3)
        id = int(input('Введите Id экскурсии: '))
        print(service.getScheduleByExcursion(id))


if __name__ == '__main__':
    interface = Interface()
    interface.choice()
