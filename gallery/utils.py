from functools import partial
import os
from datetime import date


def _update_filename(instance, filename, path):
    """Custom upload and rename function for 'upload_to='
         at ImageField of ImageGallery model."""

    path = path

    filename = f'ID:-{instance.id}-{date.today().strftime("%b-%d-%Y")}.jpg'

    return os.path.join(path, filename)


def upload_to(path):
    return partial(_update_filename, path=path)
