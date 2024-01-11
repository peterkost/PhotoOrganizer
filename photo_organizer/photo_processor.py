from pillow_heif import register_heif_opener
from datetime import datetime
from misc.Photo import Photo

def addMetaDataToPhotos(filePaths: list[Photo]):
    print('photo count', len(filePaths))
