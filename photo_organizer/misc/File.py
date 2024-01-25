import re
from datetime import datetime

from misc.FilePath import FilePath


class File:
    def __init__(self, path: FilePath) -> None:
        self.path = path
        self.newPath = self.dateTime = None
        self._setDateTime()
        self._setNewPath()


    def getFullNewPath(self) -> str:
        return f"{self.newPath}.{self.newFileName}.{self.path.extension}"


    def getDateTime(self) -> datetime:
        return self.dateTime if self.dateTime else datetime(1970, 6, 2)


    def setNewFileName(self, index: int):
        if self.dateTime:
            self.newFileName = f"{self.dateTime.strftime('%Y_%m_%d')}-{index:03d}"
        else:
            self.newFileName = f"{index:03d}"


    def _setDateTime(self):
        raise NotImplemented
    

    def _renameFile(self):
        raise NotImplemented
    

    def _setNewPath(self):
        if self.dateTime:
            self.newPath = f"{self.path.dir}/{self.dateTime.year}/{self.dateTime.strftime('%m-%B')}"
        else:
            year = self._guessYear()
            self.newPath = f"{self.path.dir}{'/' + year if year else ''}/Undated"


    def _guessYear(self) -> str:
        dir = self.path.dir
        yearRegex = re.compile(r'^(1|2)\d{3}$')
        for s in dir.split('/'):
            if yearRegex.match(s):
                return s
        return ''


    def __str__(self) -> str:
        return f"{self.path.getFullPath()}"


    def __lt__(self, other):
        return self.getDateTime() < other.getDateTime()
