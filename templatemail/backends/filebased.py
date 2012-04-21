from django.core.mail.backends import filebased
from base import BaseEmailBackend


class EmailBackend(filebased.EmailBackend, BaseEmailBackend):
    def send_messages(self, email_messages):
        email_messages = self.render_messages(email_messages)
        super(EmailBackend, self).send_messages(email_messages)
