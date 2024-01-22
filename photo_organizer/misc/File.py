import re
from misc.FilePath import FilePath


class File:
    def __init__(self, path: FilePath) -> None:
        self.path = path
        self.newPath = "New path not set"


    def _guessYear(self) -> str:
        dir = self.path.dir
            
        yearRegex = re.compile(r'^(1|2)\d{3}$')
        for s in dir.split('/'):
            if yearRegex.match(s):
                return s
        return ''
    
    def __str__(self) -> str:
        return f"{self.path.getFullPath()}"
