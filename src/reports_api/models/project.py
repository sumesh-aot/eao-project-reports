# Copyright © 2019 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Model to manage Project."""

from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .base_model import BaseModel


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
    address = Column(Text, nullable=True, default=None)
    sub_sector_id = Column(ForeignKey('sub_sectors.id'), nullable=False)
    proponent_id = Column(ForeignKey('proponents.id'), nullable=False)
    region_id_env = Column(ForeignKey('regions.id'), nullable=False)
    region_id_flnro = Column(ForeignKey('regions.id'), nullable=False)

    sub_sector = relationship('SubSector', foreign_keys=[sub_sector_id], lazy='select')
    proponent = relationship('Proponent', foreign_keys=[proponent_id], lazy='select')
    region_env = relationship('Region', foreign_keys=[region_id_env], lazy='select')
    region_flnro = relationship('Region', foreign_keys=[region_id_flnro], lazy='select')

    def as_dict(self):  # pylint:disable=arguments-differ
        """Return Json representation."""
        result = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'location': self.location,
            'capital_investment': self.capital_investment,
            'epic_guid': self.epic_guid,
            'is_project_closed': self.is_project_closed,
            'address': self.address,
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
