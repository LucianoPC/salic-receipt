import os
import sys

PROJECT_ROOT = sys.prefix
DATA_PATH = os.path.join(PROJECT_ROOT, 'data')
DATA_CSV_PATH = os.path.join(DATA_PATH, 'csv')
DATA_PICKLE_PATH = os.path.join(DATA_PATH, 'pickle')
RECEIPTS_CSV_PATH = os.path.join(DATA_CSV_PATH, 'comprovantes_pagamento.csv')
RECEIPTS_PICKLE_PATH = os.path.join(DATA_PICKLE_PATH,
                                    'id_arquivos.pickle')
