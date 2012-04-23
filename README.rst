==========
Django-Template-Mail
==========
:Info: A Django application to send email using django's templating system
:Author: Benoît Bar (http://github.com/benoitbar, http://twitter.com/benoitbar)

Get started
===========

Installing
----------
::

    pip install django-template-mail

Configure your mail backend
---------------------------

django-template-mail ships with same backends as Django (https://docs.djangoproject.com/en/dev/topics/email/#email-backends). Just replace **django.core.mail** by **templatemail** ::

    EMAIL_BACKEND = 'templatemail.backends.smtp.EmailBackend'

Convert HTML into plain text
----------------------------

By default, django-template-backend uses a minimalist process to convert HTML into plain text. I suggest you to use **html2text** (https://github.com/aaronsw/html2text) ::

    EMAIL_HTML2TEXT = 'html2text.html2text'

You can also write your own method and use it ::

    EMAIL_HTML2TEXT = 'your.module.yourhtml2textmethod'

Sending emails
==============

To send email with django-template-mail you simply should use the method described in the Django documentation (https://docs.djangoproject.com/en/dev/topics/email/) and replace the **message** attribute as a tuple **('directory_template/template.html', {'key': 'value'}, context_instance)** ::
    
    from django.core.mail import send_mail
    send_mail( 
        'Welcome', 
        (
            'mail/welcome.html', 
            {
                'username': request.user.username, 
                'full_name': request.user.get_full_name(),
                'signup_date': request.user.date_joined
            }
        ),
        'from@example.com', 
        ['to@example.com'], 
        fail_silently=False
    )

django-template-mail looks into django template directories/loaders ::

    <p>Hi {{full_name}},</p> 
    <p>
        You just signed up using:
        <ul>      
            <li>username: {{username}}</li>
            <li>join date: {{signup_date}}</li>
        </ul>
    </p>
    <p>Thanks!</p>