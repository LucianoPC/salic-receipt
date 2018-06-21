import os

FILE_PATH = os.path.realpath(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(FILE_PATH, os.pardir, os.pardir))
DATA_PATH = os.path.join(PROJECT_ROOT, 'data')
DATA_CSV_PATH = os.path.join(DATA_PATH, 'csv')
RECEIPTS_PATH = os.path.join(DATA_CSV_PATH, 'comprovantes_pagamento.csv')
