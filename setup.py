from setuptools import setup, find_packages
from src.CHP_api.__init__ import __version__

import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(name='CHP_api',
      version=__version__,
      description='Simple python adaptor for CHP_REST',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/talestorm-com/CHP_api',
      author='talestorm',
      author_email='dr.krimsn@gmail.com',
      package_dir={'': 'src'},
      packages=find_packages(where='src'),
      python_requires='>=3.5, <4',
      install_requires=['requests==2.24.0'],
     )