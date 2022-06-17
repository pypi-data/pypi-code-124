# Copyright (c) 2021, VRAI Labs and/or its affiliates. All rights reserved.
#
# This software is licensed under the Apache License, Version 2.0 (the
# "License") as published by the Apache Software Foundation.
#
# You may not use this file except in compliance with the License. You may
# obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


from typing import Union

from supertokens_python.ingredients.emaildelivery import \
    EmailDeliveryIngredient
from supertokens_python.recipe.emailverification.interfaces import \
    TypeEmailVerificationEmailDeliveryInput


class User:
    def __init__(self, user_id: str, email: str):
        self.user_id = user_id
        self.email = email


class EmailVerificationIngredients:
    def __init__(self, email_delivery: Union[EmailDeliveryIngredient[TypeEmailVerificationEmailDeliveryInput], None] = None):
        self.email_delivery = email_delivery
