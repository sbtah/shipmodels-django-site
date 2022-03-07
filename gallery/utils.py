from functools import partial
import os
from datetime import date
import hashlib


def _update_filename(instance, filename, path):
    path = path

    filename = f'Tytuł-{instance.tytuł}-{date.today().strftime("%b-%d-%Y")}.jpg'

    return os.path.join(path, filename)


def upload_to(path):
    return partial(_update_filename, path=path)
