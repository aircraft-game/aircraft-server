# -*- coding: utf-8 -*-

from handlers.base import BaseHandler

import logging

logger = logging.getLogger(__name__)


class AccountLoginView(BaseHandler):
    def get(self):
        if self.session.get('username'):
            self.redirect('editor/')

        self.render('account/login.html')


class AccountRegisterView(BaseHandler):
    def get(self):
        if self.session.get('username'):
            self.redirect('editor/')

        self.render('account/register.html')


class AccountLogoutView(BaseHandler):
    def get(self):
        self.session.delete('username')
        self.redirect('/account/login/')
