import os
from setuptools import setup

def read(fname):
  return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="newspaper",
    version="0.1dev",
    author="g. nicholas d'andrea",
    author_email="nick@gnidan.org",
    description=("Typesetter utility to format text files into high-quality, ",
      "human readable documents."),
    keywords="typesetter plaintext",
    packages=['newspaper', 'tests'],
    license='BSD',
    long_description=read('README'),
)

