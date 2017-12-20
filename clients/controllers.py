from tornado import gen


class BaseController(object):

    def __init__(self):
        pass


class mirror_controller(BaseController):

    def __init__(self, q=None):
        BaseController.__init__(self)
        self.q = q

    @gen.coroutine
    def main_loop(self):
        while True:
            order = yield self.q['income'].get()
            print(order)
