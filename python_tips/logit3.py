class logit3(object):
    _logfile = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        log_string = self.func.__name__ + " was called"
        print(log_string)

        with open(self._logfile, 'a') as opened_file:
            opened_file.write(log_string + '\n')

        self.notify()

        # return base func
        return self.func(*args)

    def notify(self):
        # logit only logs, no more
        pass
