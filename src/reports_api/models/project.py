from sqlalchemy import Column, ForeignKey, Integer, Boolean, String, Float
from sqlalchemy.orm import relationship

from .base_model import BaseModel
from .db import db


class Project(BaseModel):
    """Model class for Project."""

    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String())
    description = Column(String())
    location = Column(String())
    capital_investment = Column(Float())
    epic_guid = Column(String(), nullable=True, default=None)
    is_project_closed = Column(Boolean(), default=False)
    sub_sector_id = Column(ForeignKey('sub_sectors.id'), nullable=False)
    proponent_id = Column(ForeignKey('proponents.id'), nullable=False)
    region_id_env = Column(ForeignKey('regions.id'), nullable=False)
    region_id_flnro = Column(ForeignKey('regions.id'), nullable=False)

    sub_sector = relationship('SubSector', foreign_keys=[sub_sector_id], lazy='select')
    proponent = relationship('Proponent', foreign_keys=[proponent_id], lazy='select')
    region_env = relationship('Region', foreign_keys=[region_id_env], lazy='select')
    region_flnro = relationship('Region', foreign_keys=[region_id_flnro], lazy='select')

    def as_dict(self):
        """Return Json representation."""
        result = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'location': self.location,
            'capital_investment': self.capital_investment,
            'epic_guid': self.epic_guid,
            'is_project_closed': self.is_project_closed,
            'sub_sector_id': self.sub_sector_id,
            'proponent_id': self.proponent_id,
            'region_id_env': self.region_id_env,
            'region_id_flnro': self.region_id_flnro,

            'sub_sector': self.sub_sector.as_dict(),
            'proponent': self.proponent.as_dict(),
            'region_env': self.region_env.as_dict(),
            'region_flnro': self.region_flnro.as_dict()
        }
        return result
