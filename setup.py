# -*- coding: utf-8 -*-
"""
unicategories
=============

Unicode category database.

More details on project's README and
`github page <https://github.com/ergoithz/unicategories/>`_.

License
-------
MIT (see LICENSE file).
"""

# avoid issues with broken easy_install scripts (hi appveyor!)
import os
import codecs
os.environ['UNICODE_CATEGORIES_CACHE'] = 'off'  # noqa

from setuptools import setup
from cache_setup import Distribution

from unicategories import __meta__ as meta
from unicategories.cache import generate_and_cache

meta_app = meta.__app__
meta_version = meta.__version__
meta_license = meta.__license__

with codecs.open('README.rst', encoding='utf-8') as f:
    meta_doc = f.read()

setup(
    name=meta_app,
    version=meta_version,
    url='https://github.com/ergoithz/unicategories',
    download_url='https://github.com/ergoithz/unicategories/archive/%s.tar.gz'
        % meta_version,
    license=meta_license,
    author='Felipe A. Hernandez',
    author_email='ergoithz@gmail.com',
    description='Unicode category database',
    long_description=meta_doc,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    keywords=['unicode'],
    packages=[
        'unicategories',
        'unicategories.tests',
        ],
    package_content={
        'unicategories': {
            'cache/unicategories.cache': generate_and_cache
        },
    },
    install_requires=['appdirs'],
    test_suite='unicategories.tests',
    distclass=Distribution,
    zip_safe=False,
    platforms='any'
)
