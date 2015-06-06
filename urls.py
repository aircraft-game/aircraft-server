# -*- coding: utf-8 -*-

from handlers.account.views import AccountLoginView, AccountRegisterView
from handlers.account.api import AccountLoginHandler, AccountRegisterHandlker

url_patterns = [
    (r'/account/login/?', AccountLoginView),
    (r'/account/register/?', AccountRegisterView),

    (r'/api/account/login/?', AccountLoginHandler),
    (r'/api/account/register/?', AccountRegisterHandlker),
]
