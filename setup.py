from setuptools import setup, find_packages

setup(
    name = 'salic-receipt',
    version = '0.0.1',
    description = 'Download Salic receipt files',
    license = 'GPL v3.0',
    packages = find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires = [
    ],
    data_files = [
        ('data/csv', ['data/csv/comprovantes_pagamento.csv'])
    ],
    python_requires = '>=3',
)
