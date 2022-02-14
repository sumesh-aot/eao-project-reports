# Copyright © 2019 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Model to handle all operations related to Payment Disbursement status code."""

from marshmallow import fields
from sqlalchemy import Column, ForeignKey, Integer, Boolean, String
from sqlalchemy.orm import relationship

from .code_table import CodeTable
from .db import db, ma


class PhaseCode(db.Model, CodeTable):
    """Model class for Phase."""

    __tablename__ = 'phase_codes'

    id = Column(Integer, primary_key=True, autoincrement=True)  # TODO check how it can be inherited from parent

    work_type_id = Column(ForeignKey('work_types.id'), nullable=False)
    start_event = Column(String())
    end_event = Column(String)
    duration = Column(Integer())
    legislated = Column(Boolean())

    work_type = relationship('WorkType', foreign_keys=[work_type_id], lazy='select')

    def as_dict(self):
        """Return Json representation."""
        return {
            'id': self.id,
            'name': self.name,
            'sortOrder': self.sort_order,
            'startEvent': self.start_event,
            'endEvent': self.end_event,
            'duration': self.duration,
            'legislated': self.legislated,
            'workType': self.work_type.as_dict()
        }
