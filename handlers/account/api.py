# -*- coding: utf-8 -*-

import hashlib
from handlers.base import BaseHandler

import logging

logger = logging.getLogger(__name__)


class AccountLoginHandler(BaseHandler):
    def post(self):
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)
        if not username or not password:
            return self.raise_error_page(400)

        db = self.application.database
        user = db.user.find_one({'username': username})
        if not user:
            return self.response_json(content={'message': 'invalid username'}, status_code=400)
        encrypted_password = hashlib.sha1(password).hexdigest()
        if user.get('password') != encrypted_password:
            return self.response_json(content={'message': 'wrong password'}, status_code=400)

        self.session['username'] = username
        return self.response_json(content={'username': username})


class AccountRegisterHandlker(BaseHandler):
    def post(self):
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)
        repeat_password = self.get_argument('repeat-password')

        if not username or not password or not repeat_password:
            return self.raise_error_page(400)
        if password != repeat_password:
            return self.response_json(content={'message': 'repeat password wrong'}, status_code=400)

        db = self.application.database
        user = db.user.find_one({'username': username})
        if user:
            return self.response_json(content={'message': 'repeat username'}, status_code=400)

        encrypted_password = hashlib.sha1(password).hexdigest()
        db.user.insert({
            'username': username,
            'password': encrypted_password,
        })

        self.session['username'] = username
        return self.response_json(content={'username': username})
