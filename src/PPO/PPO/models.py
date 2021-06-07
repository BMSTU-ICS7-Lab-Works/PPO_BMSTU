from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date, ForeignKey, create_engine, Table, DATE
from sqlalchemy.ext.declarative import declarative_base

admin_engine = create_engine("postgresql+psycopg2://postgres:1@localhost/Excursions")
Base = declarative_base()

SightsExcursions = Table('SightsExcursions', Base.metadata,
    Column('sightsId', Integer,
      ForeignKey('sights.id', ondelete='cascade')),
    Column('excursionsId', Integer,
        ForeignKey('excursions.id', ondelete='cascade')))

SelectedExcursions = Table('SelectedExcursions', Base.metadata,
    Column('userId', Integer,
      ForeignKey('users.id', ondelete='cascade')),
    Column('scheduleId', Integer,
        ForeignKey('schedule.id', ondelete='cascade')),
    Column('date', Date))


class Excursions(Base):
    __tablename__ = 'excursions'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    guide = Column(Integer, ForeignKey('guides.id'))
    price = Column(Integer)
    sight = relationship('Sights', secondary=SightsExcursions, back_populates='excursion')

    def __init__(self, name, description, guide, price):
        self.name = name
        self.description = description
        self.guide = guide
        self.price = price

    def __repr__(self):
        return "%s, %s, %s, %s" % (self.name, self.description, self.guide, self.price)


class Schedule(Base):
    __tablename__ = 'schedule'
    id = Column(Integer, primary_key=True)
    excursion = Column(Integer, ForeignKey('excursions.id'))
    day = Column(String)
    time = Column(String)

    def __init__(self, excursion, day, time):
        self.excursion = excursion
        self.day = day
        self.time = time

    def __repr__(self):
        return "%s, %s, %s" % (self.excursion, self.day, self.time)


class Guides(Base):
    __tablename__ = 'guides'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    patronymic = Column(String)
    qualification = Column(String)
    biography = Column(String)
    experience = Column(Integer)

    def __init__(self, first_name, last_name, patronymic, qualification, biography, experience):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.qualification = qualification
        self.biography = biography
        self.experience = experience

    def __repr__(self):
        return "<Guide('%s', '%s', '%s', '%s', '%s', '%s')>" % (
        self.first_name, self.last_name, self.patronymic, self.qualification, self.biography, self.experience)


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nickname = Column(String)
    password = Column(String)
    salt = Column(String)
    role = Column(Integer)

    def __init__(self, nickname, password, salt, role):
        self.nickname = nickname
        self.password = password
        self.salt = salt
        self.role = role

    def __repr__(self):
        return "<Users('%s', '%s', '%s', '%s')>" % (self.nickname, self.password, self.salt, self.role)

class Sights(Base):
    __tablename__ = 'sights'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    build_date = Column(DATE)
    type = Column(String)
    author = Column(String)
    description = Column(String)
    excursion = relationship('Excursions', secondary=SightsExcursions, back_populates='sight')

    def __init__(self, name, build_date, type, author, description):
        self.name = name
        self.build_date = build_date
        self.type = type
        self.author = author
        self.description = description

    def __repr__(self):
        return "<Sights('%s', '%s', '%s', '%s', '%s')>" % (self.name, self.build_date, self.type,
                                                          self.author, self.description)


if __name__ == '__main__':
    Base.metadata.create_all(admin_engine)
