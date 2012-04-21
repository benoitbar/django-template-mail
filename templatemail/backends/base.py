import re

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.importlib import import_module


class BaseEmailBackend(object):
    def render_messages(self, email_messages):
        emails = []
        for message in email_messages:
            body = message.body
            assert (type(body) is tuple or type(body) is list), "The message must be a tuple. e.g ('template_directory/template.html',)"
            template_name = body[0]
            dictonnary = len(body) >= 2 and body[1] or None
            context_instance = len(body) >= 3 and body[2] or None
            html_content = render_to_string(template_name, dictonnary, context_instance)

            path = settings.EMAIL_HTML2TEXT
            if path is None:
                html2text = self._html2text
            else:
                try:
                    mod_name, method_name = path.rsplit('.', 1)
                    mod = import_module(mod_name)
                except ImportError, e:
                    raise ImproperlyConfigured(('Error importing email backend module %s: "%s"'
                                                % (mod_name, e)))
                try:
                    html2text = getattr(mod, method_name)
                except AttributeError:
                    raise ImproperlyConfigured(('Module "%s" does not define a '
                                                '"%s" method' % (mod_name, method_name)))

            plain_content = html2text(html_content)

            msg = EmailMultiAlternatives(subject=message.subject, body=plain_content, from_email=message.from_email, to=message.to, bcc=message.bcc,
                 connection=message.connection, attachments=message.attachments, headers=message.extra_headers, cc=message.cc)
            msg.attach_alternative(html_content, "text/html")
            emails.append(msg)
        return emails

    def _html2text(self, html):
        """Convert HTML to plain txt
        - suppress all return
        - <p>, <div>, <tr> to return
        - <td> to tab
        """
        p = re.compile('(<p.*?>)', re.I)
        div = re.compile('(<tr.*?>)|(<div.*?>)', re.I)
        t = re.compile('<td.*?>', re.I)
        comm = re.compile('<!--.*?-->', re.M)
        tags = re.compile('<.*?>', re.M)

        text = html.replace('\n', '')   # remove returns time this compare to split filter join
        text = p.sub('\n\n', text)      # replace p \n\n
        text = div.sub('\n', text)      # replace tr and div by \n
        text = t.sub('\t', text)        # replace td by \t
        text = comm.sub('', text)       # remove comments
        text = tags.sub('', text)       # remove all remaining tags
        text = re.sub(' +', ' ', text)  # remove running spaces this remove the \n and \t
        return text
