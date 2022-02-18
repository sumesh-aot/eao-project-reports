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
"""Service to manage Fee Calculation."""

from flask import current_app,jsonify

from reports_api.models import db, CodeTable
from reports_api.models.phase_code import PhaseCode


class CodeService:
    """Service to manage Fee related operations."""

    @classmethod
    def find_code_values_by_type(
            cls,
            code_type: str
    ):
        """Find code values by code type."""
        current_app.logger.debug(f'<find_code_values_by_type : {code_type}')
        model: CodeTable = cls._find_model_from_type(code_type)
        response = {'codes':[]}
        for row in model.find_all():
            response['codes'].append(row.as_dict())

        current_app.logger.debug('>find_code_values_by_type')
        return response

    @classmethod
    def _find_model_from_type(cls, code_type):
        for model_class in db.Model._decl_class_registry.values():  # pylint:disable=protected-access
            if hasattr(model_class, '__tablename__') and model_class.__tablename__ == code_type:
                return model_class

    @classmethod
    def find_code_value_by_type_and_code(
            cls,
            code_type: str,
            code: str
    ):
        """Find code values by code type and code."""
        current_app.logger.debug(f'<find_code_value_by_type_and_code : {code_type} - {code}')
        model: CodeTable = cls._find_model_from_type(code_type)
        current_app.logger.debug('>find_code_value_by_type_and_code')
        return model.find_by_id(code).as_dict()
    
    @classmethod
    def find_phase_codes_by_ea_act_and_work_type(
        cls,
        _ea_act_id: str,
        _work_type_id: str
    ):
        """Find phase codes by ea_act and work_type"""
        current_app.logger.debug(f'<find_phase_codes_by_ea_act_and_work_type : {_ea_act_id} - {_work_type_id}')
        code_table = db.session.query(PhaseCode).filter_by(work_type_id=_work_type_id, ea_act_id=_ea_act_id).all();  # pylint: disable=no-member
        return jsonify([item.as_dict() for item in code_table])
