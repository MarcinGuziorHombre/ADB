from sqlalchemy import create_engine, Column, Integer, DateTime, Float, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

import datetime

class Room(Base):
    __tablename__ = 'room'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    host_id = Column(Integer, ForeignKey('hosts.id'))
    location_id = Column(Integer, ForeignKey('location.id'))
    details_id = Column(Integer, ForeignKey('room_details.id'))

    def __repr__(self):
        return "<room(id={0}, name={1}, host_id={2}, location_id={3}, details_id={4})>".format(
            self.id, self.name, self.host_id, self.location_id, self.details_id
        )


class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __repr__(self):
        return "<host(id={0}, host_name={1})>".format(
            self.id, self.name)


class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    latitude = Column(Float(precision=7, decimal_return_scale=None))
    longitude = Column(Float(precision=7, decimal_return_scale=None))
    neighbourhood = Column(Integer, ForeignKey('neighbourhood.id'))

    def __repr__(self):
        return "<location(id={0}, latitude={1}, longitude={2}, neighbourhood={3})>".format(
            self.id, self.latitude, self.longitude,  self.neighbourhood
        )


class Neighbourhood(Base):
    __tablename__ = 'neighbourhood'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    neighbourhood_group = Column(Integer, ForeignKey('neighbourhood_group.id'))

    def __repr__(self):
        return "<neighbourhood(id={0}, name={1}, neighbourhood_group={2})>".format(
            self.id, self.name,  self.neighbourhood_group
        )


class NeighbourhoodGroup(Base):
    __tablename__ = 'neighbourhood_group'
    id = Column(Integer, primary_key=True)
    neighbourhood_group = Column(String(50))

    def __repr__(self):
        return "<neighbourhood_group(id={1}, neighbourhood_group={2})>".format(
            self.id, self.neighbourhood_group
        )


class RoomDetails(Base):
    __tablename__ = 'room_details'
    id = Column(Integer, primary_key=True)
    room_type = Column(Integer, ForeignKey('room_type.id'))
    price = Column(Integer(unsigned=True))
    min_nigths = Column(Integer(unsigned=True))
    availability_days_per_year = Column(Integer(unsigned=True))

    def __repr__(self):
        return "<room_details(id={0}, room_type={1}, price={2}, min_nigths={3}, availability_days_per_year={4})>".format(
            self.id, self.room_type, self.price, self.min_nigths, self.availability_days_per_year
        )


class RoomType(Base):
    __tablename__ = 'room_type'
    id = Column(Integer, primary_key=True)
    description = Column(String(50))

    def __repr__(self):
        return "<room_type(id={0}, description={1})>".format(
            self.id, self.description
        )


class Review(Base):
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True)
    content = Column(String)
    room_id = Column(ForeignKey("room.id"))
    date = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<review(id={0}, content={1}, room={2}, date={3})>".format(
            self.id, self.content, self.room_id, self.date
        )
