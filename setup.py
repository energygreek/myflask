from setuptools import setup

NAME = 'myflask'
VERSION = '1.2'
PY_MODULES = ['main']

setup(name=NAME,
      version=VERSION,
      py_modules=PY_MODULES,
      install_requires=[
        'flask',
        'flask-login',
        'flup'],
      )