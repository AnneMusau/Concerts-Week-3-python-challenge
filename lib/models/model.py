from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String)

    concerts = relationship("Concert", back_populates="band")

class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    city = Column(String)

    concerts = relationship("Concert", back_populates="venue")

class Concert(Base):
    __tablename__ = 'concerts'

    id = Column(Integer, primary_key=True)
    band_id = Column(Integer, ForeignKey('bands.id'), nullable=False)
    venue_id = Column(Integer, ForeignKey('venues.id'), nullable=False)
    date = Column(Date)

    band = relationship("Band", back_populates="concerts")
    venue = relationship("Venue", back_populates="concerts")
