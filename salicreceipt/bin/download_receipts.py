import os
import re
import csv
import requests

from salicreceipt.paths import RECEIPTS_PATH


def get_id_arquivos():
    with open(RECEIPTS_PATH, 'r') as csv_data_file:
        csv_reader = csv.reader(csv_data_file)

        id_arquivos = [row[10] for row in csv_reader]

    return id_arquivos[1:]


def download_receipt_file(id_arquivo, receipt_file_folder):
    DOWNLOAD_LINK = 'http://salic.cultura.gov.br/verprojetos/abrir?id={}'

    url = DOWNLOAD_LINK.format(id_arquivo)

    response = requests.get(url)
    content_disposition = response.headers['content-disposition']

    receipt_content = response.content
    receipt_file_name = re.findall('filename="(.+)"', content_disposition)[0]
    receipt_file_path = os.path.join(receipt_file_folder, receipt_file_name)

    with open(receipt_file_path, 'wb') as receipt_file:
        receipt_file.write(receipt_content)


# id_arquivos = get_id_arquivos()
id_arquivos = ['231633']
download_receipt_file(id_arquivos[0], '.')
