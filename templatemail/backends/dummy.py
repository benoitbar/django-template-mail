from django.core.mail.backends import dummy
from base import BaseEmailBackend


class EmailBackend(dummy.EmailBackend, BaseEmailBackend):
    def send_messages(self, email_messages):
        email_messages = self.render_messages(email_messages)
        super(EmailBackend, self).send_messages(email_messages)
