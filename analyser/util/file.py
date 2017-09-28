import os
import security
import variables

from unicodedata import normalize

def file_save(music_file):
    if music_file:
        raw_file_name_uft8 = normalize('NFKD', music_file.filename).encode('utf-8', 'strict').decode('utf-8')
        filename = security.secure_filename(raw_file_name_uft8)
        path_name = os.path.join(variables.UPLOAD_FOLDER, filename)
        music_file.save(path_name)
        return path_name
    return "hoops, there may be some error"