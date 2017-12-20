from tornado import web


class base_web_app(web.Application):

    def __init__(self, q=None):
        self.q = q
        handlers = []
        web.Application.__init__(self, handlers)


class tornado_web_app(base_web_app):
    pass

class slack_web_app(base_web_app):
    pass
