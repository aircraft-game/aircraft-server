# -*- coding: utf-8 -*-

import logging
import json
import tornado.web

from torndsession.sessionhandler import SessionBaseHandler

logger = logging.getLogger(__name__)


class BaseHandler(SessionBaseHandler):
    """A class to collect common handler methods - all other handlers should
    subclass this one.
    """

    def load_json(self):
        """Load JSON from the request body and store them in
        self.request.arguments, like Tornado does by default for POSTed form
        parameters.

        If JSON cannot be decoded, raises an HTTPError with status 400.
        """
        try:
            self.request.arguments = json.loads(self.request.body)
        except ValueError:
            msg = "Could not decode JSON: %s" % self.request.body
            logger.debug(msg)
            raise tornado.web.HTTPError(400, msg)

    def get_json_argument(self, name, default=None):
        """Find and return the argument with key 'name' from JSON request data.
        Similar to Tornado's get_argument() method.
        """
        if default is None:
            default = self._ARG_DEFAULT
        if not self.request.arguments:
            self.load_json()
        if name not in self.request.arguments:
            if default is self._ARG_DEFAULT:
                msg = "Missing argument '%s'" % name
                logger.debug(msg)
                raise tornado.web.HTTPError(400, msg)
            logger.debug("Returning default argument %s, as we couldn't find "
                    "'%s' in %s" % (default, name, self.request.arguments))
            return default
        arg = self.request.arguments[name]
        logger.debug("Found '%s': %s in JSON arguments" % (name, arg))
        return arg

    def raise_error_page(self, error_code):
        if error_code == 400:
            self.set_status(status_code=400)
            self.render('400.html')
        else:
            self.set_status(status_code=500)
            self.render('500.html')

    def response_json(self, content, status_code=200):
        self.set_status(status_code=status_code)
        self.set_header('Content-Type', 'application/json')
        if isinstance(content, dict) or isinstance(content, list):
            self.write(json.dumps(content))
        else:
            self.write(content)
