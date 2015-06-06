# -*- coding: utf-8 -*-

from handlers.account.views import AccountLoginView, AccountRegisterView, AccountLogoutView
from handlers.account.api import AccountLoginHandler, AccountRegisterHandlker

from handlers.editor.views import EditorView

from handlers.client.api import ClientLoginHandler

url_patterns = [
    (r'/', AccountLoginView),
    (r'/account/login/?', AccountLoginView),
    (r'/account/register/?', AccountRegisterView),
    (r'/account/logout/?', AccountLogoutView),

    (r'/editor/?', EditorView),

    (r'/api/account/login/?', AccountLoginHandler),
    (r'/api/account/register/?', AccountRegisterHandlker),

    (r'/client/login/?', ClientLoginHandler),
]
