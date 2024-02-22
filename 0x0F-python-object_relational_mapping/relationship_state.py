#!/usr/bin/python3
"""
This module defines the State class and creates the Base instance.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Create the Base instance
Base = declarative_base()


class State(Base):
    """
    Class representing a state.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", back_populates="state")

    def __repr__(self):
        return f"<State(id={self.id}, name={self.name})>"
