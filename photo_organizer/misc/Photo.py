from datetime import datetime
from misc.FilePath import FilePath
from PIL import Image
from misc.File import File


class Photo(File):
    def __init__(self, path: FilePath):
        File.__init__(self, path)
        self._tryToSetDateTime()
        self._setNewPath()
        

    def _tryToSetDateTime(self):
            try:
                image = Image.open(self.path.getFullPath())
                exif = image.getexif()
                if 306 in exif:
                    self.dateTime = datetime.strptime(exif[306],'%Y:%m:%d %H:%M:%S')
                else:
                    self.dateTime = None
            except Exception as e:
                print(f"Error setting date for {self.path.name}", e)
                self.dateTime = None


    def _setNewPath(self):
        if self.dateTime:
            self.newPath = f"{self.path.dir}/{self.dateTime.year}/{self.dateTime.strftime('%m-%B')}"
        else:
            year = self._guessYear()
            self.newPath = f"{self.path.dir}{'/' + year if year else ''}/Undated"

    
    def setNewFileName(self, index: int):
        if self.dateTime:
            self.newFileName = f"{self.dateTime.strftime('%Y_%m_%d')}-{index:03d}"
        else:
            self.newFileName = f"{index:03d}"

    def getFullNewPath(self) -> str:
        return f"{self.newPath}.{self.newFileName}.{self.path.extension}"


    def getDateTime(self) -> datetime:
        return self.dateTime if self.dateTime else datetime(1970, 6, 2)


    def __lt__(self, other):
        return self.getDateTime() < other.getDateTime()
