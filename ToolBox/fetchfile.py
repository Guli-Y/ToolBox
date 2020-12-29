
import os

path = os.path.dirname(os.path.abspath(__file__))

def fetch_files(path):
    new_path = os.path.join(path, '..', 'raw_data')
    price_files = []
    for root, direc, files in os.walk(new_path):
        if 'price' in direc:
            price_files.append(files)
    return price_files
