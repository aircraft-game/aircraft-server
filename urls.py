# -*- coding: utf-8 -*-

from handlers.account.views import AccountLoginView, AccountRegisterView

url_patterns = [
    (r'/account/login/?', AccountLoginView),
    (r'/account/register/?', AccountRegisterView),
]
