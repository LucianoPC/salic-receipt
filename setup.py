from setuptools import setup, find_packages

setup(
    name = 'salic-receipt',
    version = '0.0.1',
    description = 'Download Salic receipt files',
    url = 'https://github.com/LucianoPC/salic-receipt',
    author = 'Luciano Prestes Cavalcanti',
    author_email = 'lucianopcbr@gmail.com',
    license = 'MIT',
    packages = find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires = [
        'click', 'pickle' 'requests',
    ],
    data_files = [
        ('data/csv', ['data/csv/comprovantes_pagamento.csv']),
        ('data/pickle', ['data/pickle/id_arquivos.pickle'])
    ],
    python_requires = '>=3',
)
