from tornado import gen, httpserver
from clients.servers import tornado_web_app, slack_web_app


class BaseBot(object):
    """
    base bot structure to handle external message services and social networks
    """

    def __init__(self, q=None):
        self.q = q
        self.stop = False

    def encode(self, msg):
        """
        build a valid message to be sent to external service
        """
        pass

    def decode(self, payload):
        """
        normalize a message from external service
        """
        pass

    @gen.coroutine
    def dispatcher(self):
        """
        coroutine that sends messages to external services
        """
        print('start dispatcher')
        while not self.stop:
            order = yield self.q['dispatch_telegram'].get()
            # TODO: implement how to send the message to respective platform


class telegram_bot(BaseBot):

    def __init__(self, q=None):
        BaseBot.__init__(self, q)
        app = tornado_web_app()
        self.service_listener = httpserver.HTTPServer(app)


class slack_bot(BaseBot):

    def __init__(self, q=None):
        BaseBot.__init__(self, q)
        app = slack_web_app()
        self.service_listener = httpserver.HTTPServer(app)
