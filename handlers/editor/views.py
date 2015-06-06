# -*- coding: utf-8 -*-

from handlers.base import BaseHandler

import logging

logger = logging.getLogger(__name__)


class EditorView(BaseHandler):
    def get(self):
        if not self.session.get('username'):
            self.redirect('/account/login/')

        self.render('editor/editor.html', username=self.session.get('username'))