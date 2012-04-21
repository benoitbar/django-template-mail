# -*- coding: utf-8 -*-

from distutils.core import setup
from setuptools import find_packages


DESCRIPTION = "A Django application to send email using django's templating system"

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    pass

CLASSIFIERS = [
    'Development Status :: 1 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Framework :: Django',
]

setup(
    name='django-template-mail',
    version='0.1',
    packages=find_packages(),
    author='Benoît Bar',
    author_email='bar.benoit@gmail.com',
    url='http://github.com/benoitbar/django-template-mail/',
    license='MIT',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    platforms=['any'],
    classifiers=CLASSIFIERS,
)
