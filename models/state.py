#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os

class State(BaseModel, Base):
    """
    ssssss
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete", back_populates="state")
    else:
        @property
        def cities(self):
            from models import storage
            from models.city import City
            data = []
            for obj in storage.all(City).values():
                if obj.state_id == self.id:
                    data.append(obj)
            print(data)
            return data

