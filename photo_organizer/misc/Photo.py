from datetime import datetime
from typing import List
from misc.FilePath import FilePath
from misc.FileType import FileType
from PIL import Image
import re


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
            year = self._guessYear()
            self.newPath = f"{self.photoPath.root}{'/' + year if year else ''}/Undated"

    def _guessYear(self) -> str:
        dir = self.photoPath.dir
        
        yearRegex = re.compile(r'^(1|2)\d{3}$')
        for s in dir.split('/'):
            if yearRegex.match(s):
                return s
        return ''
    
    
    def setNewFileName(self, name):
        self.newFileName = name

    def __str__(self):
        return f"{self.photoPath.name} - {self.dateTime}"

    
    def __lt__(self, other):
        return self.dateTime < other.dateTime
