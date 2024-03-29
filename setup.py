#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    setup,
    find_packages,
)

extras_require={
    'test': [
        "pytest==3.3.2",
        "tox>=2.9.1,<3",
    ],
    'lint': [
        "flake8==3.4.1",
        "isort>=4.2.15,<5",
    ],
    'document': [
        "Sphinx>=1.6.5,<2",
        "sphinx_rtd_theme>=0.1.9",
    ],
    'dev': [
        "bumpversion>=0.5.3,<1",
        "pytest-xdist",
        "wheel",
    ],
}

extras_require['dev'] = (
    extras_require['dev']
    + extras_require['test']
    + extras_require['lint']
    + extras_require['document']
)

setup(
    name='eth-rlp',
    # *IMPORTANT*: Don't manually change the version here. Use `make bump`, as described in readme
    version='0.1.0-alpha.1',
    description="""eth-rlp: RLP definitions for common Ethereum objects in Python""",
    long_description_markdown_filename='README.md',
    author='Jason Carver',
    author_email='ethcalibur+pip@gmail.com',
    url='https://github.com/ethereum/eth-rlp',
    include_package_data=True,
    install_requires=[
        "eth-utils>=0.7.4,<1.0.0",
    ],
    setup_requires=['setuptools-markdown'],
    extras_require=extras_require,
    py_modules=['eth_rlp'],
    license="MIT",
    zip_safe=False,
    keywords='ethereum',
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
