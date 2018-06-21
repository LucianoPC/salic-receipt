from setuptools import setup, find_packages

setup(
    name = 'salic-receipt',
    version = '0.0.4',
    description = 'Download Salic receipt files',
    url = 'https://github.com/LucianoPC/salic-receipt',
    author = 'Luciano Prestes Cavalcanti',
    author_email = 'lucianopcbr@gmail.com',
    license = 'MIT',
    install_requires = [
        'click', 'requests',
    ],
    packages = find_packages(),
    # package_data = {
    #     'salicreceipt/data/pickle': ['data/pickle/id_arquivos.pickle'],
    # },
    # data_files = [
    #     ('./data/pickle', ['data/pickle/id_arquivos.pickle']),
    # ],
    entry_points={
        'console_scripts': [
            'salic-receipt = salicreceipt.bin.download_receipts:main',
        ]
    },
    python_requires = '>=3',
    include_package_data = True
)

