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

"""A helper test.

Test-Suite to ensure that the /reports endpoint is working as expected.
"""

from datetime import datetime
from random import randrange
from typing import Dict, List, Tuple

from faker import Faker


token_header = {
    'alg': 'RS256',
    'typ': 'JWT',
    'kid': 'sbc-auth-web'
}

fake = Faker()


def get_claims(app_request=None, role: str = Role.EDITOR.value, username: str = 'CP0001234', login_source: str = None,
               roles: list = [], product_code: str = 'BUSINESS'):
    """Return the claim with the role param."""
    claim = {
        'jti': 'a50fafa4-c4d6-4a9b-9e51-1e5e0d102878',
        'exp': 31531718745,
        'iat': 1531718745,
        'iss': 'http://localhost:8081/auth/realms/demo',
        'aud': 'sbc-auth-web',
        'sub': '15099883-3c3f-4b4c-a124-a1824d6cba84',
        'typ': 'Bearer',
        'realm_access':
            {
                'roles':
                    [
                        '{}'.format(role),
                        *roles
                    ]
            },
        'preferred_username': username,
        'name': username,
        'username': username,
        'loginSource': login_source,
        'roles':
            [
                '{}'.format(role),
                *roles
            ],
        'product_code': product_code
    }
    return claim
