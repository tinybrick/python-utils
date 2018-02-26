"""
Setuptool for building
"""

import os
from setuptools import setup, find_packages, Command

class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

from utils.__init__ import __version__

setup(
    author='Jeff Wang',
    author_email='jeffwji@test.com',

    version_command='git describe --always --long --dirty=-dev',

    name = "utils",
    packages = find_packages(
      exclude=['tests', '*.tests', '*.tests.*']
    ),

    package_data = {
        '':[ 'config/*.properties', '*.md' ],
    },

    install_requires=requirements,
)
