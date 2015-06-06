# -*- coding: utf-8 -*-

from handlers.base import BaseHandler

import logging

logger = logging.getLogger(__name__)


class AccountLoginHandler(BaseHandler):
    def get(self):
        self.render('account/login.html')


class AccountRegisterHandlker(BaseHandler):
    def get(self):
        self.render('account/register.html')
