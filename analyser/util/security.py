from unicodedata import normalize
from werkzeug._compat import text_type, PY2
import re
import os

def secure_filename(filename):
    _filename_gbk_strip_re = re.compile(r'^[\u4e00-\u9fa5_a-zA-Z0-9.]+$')
    _windows_device_files = ('CON', 'AUX', 'COM1', 'COM2', 'COM3', 'COM4', 'LPT1',
                             'LPT2', 'LPT3', 'PRN', 'NUL')

    if isinstance(filename, text_type):
        filename = normalize('NFKD', filename).encode('utf-8', 'ignore')
        if not PY2:
            filename = filename.decode('utf-8')
    for sep in os.path.sep, os.path.altsep:
        if sep:
            filename = filename.replace(sep, ' ')

    filename = str(_filename_gbk_strip_re.sub('', '_'.join(
                   filename.split()))).strip('._')

    # on nt a couple of special files are present in each folder.  We
    # have to ensure that the target file is not such a filename.  In
    # this case we prepend an underline
    if os.name == 'nt' and filename and \
       filename.split('.')[0].upper() in _windows_device_files:
        filename = '_' + filename

    return filename