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
"""Service to manage work form sync with database."""

from flask import current_app
from collections import defaultdict

from reports_api.utils.helpers import find_model_from_table_name


class SyncFormDataService:
    """Service to sync form data with models."""

    @classmethod
    def _update_or_create(cls, model_class, data: dict):
        # if application_id is not None and hasattr(model_class, 'application_id'):
        #     obj = model_class.query.filter(model_class.application_id==application_id)\
        #             .filter_by(**data).first()
        if 'id' in data and data['id']:
            obj = model_class.find_by_id(data['id'])
            obj = obj.update(data)
        else:
            obj = model_class(**data)
            obj = obj.save()
        return obj

    @classmethod
    def sync_data(cls, payload: dict):
        result = {}

        # TODO: Look into bulk insert/update for collection of items in payload

        for model_name, dataset in payload.items():
            model_class = find_model_from_table_name(model_name)
            if isinstance(dataset, dict):
                obj = cls._update_or_create(model_class, dataset)
                result[model_name] = obj.as_dict()
            elif isinstance(dataset, list):
                result[model_name] = []
                for data in dataset:
                    obj = cls._update_or_create(model_class, data)
                    result[model_name].append(obj.as_dict())
        return result
