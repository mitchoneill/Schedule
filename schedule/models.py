from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation

Model = declarative_base()


class Event(Model):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    start_time = Column(Integer)
    duration = Column(Integer)
    title = Column(String)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    complete = Column(Boolean, nullable=True)
    tags = Column(ARRAY(String), nullable=True)
    rescheduled = relation('Event', remote_side=[id])
    goal = relation('Goal', back_populates='events')
    result = relation('Result', back_populates='events')


class Result(Model):
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True)
    productivity = Column(Integer, nullable=True)
    focus = Column(Integer, nullable=True)
    energy = Column(Integer, nullable=True)
    enjoyment = Column(Integer, nullable=True)
    notes = Column(String, nullable=True)
    event = relation('Event', back_populates='results')


class Goal(Model):
    __tablename__ = 'goals'
    id = Column(Integer, primary_key=True)
    start_time = Column(Integer)
    duration = Column(Integer)
    complete_time = Column(Integer, nullable=True)
    goal_status = Column(Integer, nullable=True)
    current_status = relation('CurrentStatus', back_populates='goals')
    title = Column(String)
    description = Column(String, nullable=True)
    completed = Column(Boolean, nullable=True)


class CurrentStatus(Model):
    __tablename__ = 'current_status'
    id = Column(Integer, primary_key=True)
    goal = relation('Goal', back_populates='current_status')
    time = Column(Integer)
    status = Column(Integer)
    notes = Column(String, nullable=True)
