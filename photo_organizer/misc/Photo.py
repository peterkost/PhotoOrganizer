from PIL import Image
from typing import override
from datetime import datetime

from misc.File import File
from misc.FilePath import FilePath


class Photo(File):
    def __init__(self, path: FilePath):
        File.__init__(self, path)
        

    @override
    def _setDateTime(self):
            try:
                image = Image.open(self.path.getFullPath())
                exif = image.getexif()
                if 306 in exif:
                    self.dateTime = datetime.strptime(exif[306],'%Y:%m:%d %H:%M:%S')
            except Exception as e:
                print(f"Error setting date for {self.path.name}", e)
                self.dateTime = None
