# -*- coding: utf-8 -*-

import hashlib
from handlers.base import BaseHandler

import logging

logger = logging.getLogger(__name__)


class AccountLoginHandler(BaseHandler):
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        if not username or not password:
            self.raise_error_page(400)

        db = self.application.database
        user = db.user.find_one({'username': username})
        if not user:
            return self.response_json(content={'message': 'invalid username'}, status_code=400)
        encrypted_password = hashlib.sha1(password).hexdigest()
        if user.get('password') != encrypted_password:
            return self.response_json(content={'message': 'wrong password'}, status_code=400)

        self.session['username'] = username
        return self.response_json(content={
            'username': username,
        })


class AccountRegisterHandlker(BaseHandler):
    def post(self):
        self.render('account/register.html')

