from datetime import datetime
from typing import List, Optional
from misc.FilePath import FilePath
from misc.FileType import FileType
from PIL import Image


class Photo:
    def __init__(self, paths: List[FilePath]):
        self.paths = paths
        self.isLive = len(paths) > 1
        self.photoPath = next(path for path in paths if path.ty == FileType.PHOT0)
        self.videoPath = next((path.ty == FileType.VIDEO for path in paths), None)
        self._setDateTime()
        self._setNewPath()


    def _setDateTime(self):
            try:
                image = Image.open(self.photoPath.path)
                exif = image.getexif()
                if 306 in exif:
                    self.dateTime = datetime.strptime(exif[306],'%Y:%m:%d %H:%M:%S')
                else:
                    self.dateTime = None
            except Exception as e:
                print(f"Error getting date for {self.photoPath.name}", e)
                self.dateTime = None


    def _setNewPath(self):
        if self.dateTime:
            self.newPath = f"{self.photoPath.root}/{self.dateTime.year}/{self.dateTime.strftime('%m-%B')}"
        else:
            self.newPath = "No dateTime"


    def __str__(self):
        return f"{self.photoPath.name} - {self.dateTime}"

