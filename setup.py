#!/usr/bin/env python
# http://docs.python.org/distutils/setupscript.html
# http://docs.python.org/2/distutils/examples.html

import sys
from setuptools import setup
import ast

name = '1337walls_roulette'
version = '0.1.5'
with open('{}.py'.format(name), 'rU') as f:
    for node in (n for n in ast.parse(f.read()).body if isinstance(n, ast.Assign)):
        node_name = node.targets[0]
        if isinstance(node_name, ast.Name) and node_name.id.startswith('__version__'):
            version = node.value.s
            break
                                            
if not version:
    raise RuntimeError('Unable to find version number')
    
setup(
    name=name,
    version=version,
    description='downloads random image from 1337walls, blurs it and sets it as desktop wallpaper',
    author='vanita5',
    author_email='mail@vanita5.de',
    url='http://github.com/vanita5/{}'.format(name),
    py_modules=[name],
    license="GPLv3",
    install_requires=['Pillow >= 2.5.1', 'requests >= 2.3.0'],
    classifiers=[ # https://pypi.python.org/pypi?:action=list_classifiers
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: POSIX :: Linux',
        'Topic :: System :: Shells',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points = {
        'console_scripts': ['{} = {}:console'.format(name, name)]
    }
)
