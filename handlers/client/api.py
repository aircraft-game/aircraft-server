# -*- coding: utf-8 -*-

import hashlib
import binascii
import os
from handlers.base import BaseHandler

import logging

logger = logging.getLogger(__name__)


class ClientLoginHandler(BaseHandler):
    def post(self):
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)

        if not username or not password:
            return self.response_json(content={'message': 'invalid username'}, status_code=400)

        db = self.application.database
        user = db.user.find_one({'username': username})
        if not user:
            return self.response_json(content={'message': 'invalid username'}, status_code=400)
        encrypted_password = hashlib.sha1(password).hexdigest()
        if user.get('password') != encrypted_password:
            return self.response_json(content={'message': 'wrong password'}, status_code=400)

        db.token.delete_many({'username': username})
        token = binascii.hexlify(os.urandom(20)).decode()
        db.token.insert({
            'username': username,
            'token': token,
        })
        return self.response_json(content={'username': username, 'token': token})
