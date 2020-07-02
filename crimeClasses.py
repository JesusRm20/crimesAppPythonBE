from sqlalchemy import  Column
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import Integer
from sqlalchemy import Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class streetLevelCrimes(Base):
    __tablename__ = "streetLevelCrimes"
    id = Column(Integer, primary_key=True)
    category_id = Column(String)
    location_type = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    street_id = Column(String)
    street_name = Column(String)
    context = Column(String)
    outcome_status = Column(String)
    persistent_id = Column(String)
    location_subtype = Column(String)
    month = Column(String)

    def __repr__(self):
        return "<streetLevelCrimes(id='%i',category_id='%s',location_type='%s',latitude='%s',longitude='%s',street_id='%s',street_name='%s',context='%s',outcome_status='%s',persistent_id='%s',location_subtype='%s',month='%s')>" % (
                                self.id, self.category_id, self.location_type, self.latitude, self.longitude, self.street_id, 
                                self.street_name, self.context, self.outcome_status, self.persistent_id, self.location_subtype, self.month)

class crimeCategories(Base):
    __tablename__ = "crimeCategories"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<User(name='%s')>" % (self.name)

class outcomesCount(Base):
    __tablename__ = "outcomesCount"
    id = Column(Integer, primary_key=True)
    persistent_id = Column(String)

    def __repr__(self):
        return "<User(persistent_id='%s')>" % (self.persistent_id)

class outcomesCrimes(Base):
    __tablename__ = "outcomesCrimes"
    id = Column(Integer, primary_key=True)
    persistent_id = Column(String)
    category = Column(String)
    date_1 = Column(String)
    person_id = Column(String)

    def __repr__(self):
        return "<User(persistent_id='%s',category='%s',date_1='%s',person_id='%s')>" % (self.persistent_id,self.category,self.date_1,self.person_id)
