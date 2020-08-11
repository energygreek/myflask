from setuptools import setup
import pathlib
import pkg_resources

# 解析文本文件
with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [str(requirement) for requirement in pkg_resources.parse_requirements(requirements_txt) ]

NAME = 'myflask'
VERSION = '1.3'
PY_MODULES = ['main']

setup(name=NAME,
      version=VERSION,
      py_modules=PY_MODULES,
      install_requires=install_requires 
      )
