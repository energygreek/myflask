from setuptools import setup,find_packages
import pathlib
import pkg_resources
#import os
#import sys

#sys.path.insert(0, os.path.join(
#    os.path.dirname(os.path.abspath(__file__)), 'src'))

# 解析文本文件
#with pathlib.Path('requirements.txt').open() as requirements_txt:
#    install_requires = [str(requirement) for requirement in pkg_resources.parse_requirements(requirements_txt) ]

setup(name='myflask',
      version='1.3',
      install_requires=[
            'Bootstrap-Flask==1.4',
            'Flask==1.1.2',
            'Flask-Login==0.5.0',
            'Jinja2==3.0.0a1',
            'SQLAlchemy==1.3.18',
            'Werkzeug==1.0.1',
            'WTForms==2.3.1'
          ],
      packages=['myflask'],
      zip_safe=False,
      include_package_data=True,
      )
