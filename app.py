# tornado imports
from tornado.ioloop import IOLoop
from tornado.queues import Queue
from tornado import gen
from tornado.options import define, parse_command_line, options

# local imports
from clients.infrastructure_bots import telegram_bot, slack_bot
from clients.controllers import mirror_controller

# define ports input to be set by command line argument
define('port', default=6003, help='port to launch process')


# @gen.coroutine
def main():
    #get port from commandline
    parse_command_line()
    # create service components
    q = {
    'dispatch_telegram': Queue(),
    'dispatch_slack': Queue(),
    'income': Queue()
    }
    controller = mirror_controller(q=q)
    telegram_ai = telegram_bot(q=q)
    slack_ai = slack_bot(q=q)
    # Start workers without waiting (since it never finishes).
    IOLoop.current().spawn_callback(controller.main_loop)
    IOLoop.current().spawn_callback(telegram_ai.dispatcher)
    IOLoop.current().spawn_callback(slack_ai.dispatcher)
    #create listener instance
    # configuration
    port = options.port
    # server
    telegram_ai.service_listener.listen(port)
    slack_ai.service_listener.listen(port + 1)
    #launch listener server
    IOLoop.instance().start()


if __name__ == '__main__':
    main()
