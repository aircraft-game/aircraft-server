# -*- coding: utf-8 -*-

from handlers.base import BaseHandler

import logging

logger = logging.getLogger(__name__)


class AccountLoginView(BaseHandler):
    def get(self):
        self.render('account/login.html')


class AccountRegisterView(BaseHandler):
    def get(self):
        self.render('account/register.html')
