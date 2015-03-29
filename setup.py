try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'fixed-width newspaper formatting for documents',
    'author': 'g. nicholas d\'andrea',
    'url': 'https://github.com/gnidan/newspaper',
    'author_email': 'nick@gnidan.org',
    'version': '0.2',
    'install_requires': ['nose'],
    'packages': ['newspaper'],
    'scripts': [],
    'name': 'newspaper',
}

setup(**config)
