from logit3 import logit3


class logit_email(logit3):
    def __init__(self, email="admin@domain.com", *args, **kwargs):
        print(*args, **kwargs)
        self.email = email
        super(logit_email, self).__init__(*args, **kwargs)

    def notify(self):
        # Send an email to self.email
        pass
