#from typing import override

from misc.Photo import Photo
from misc.FilePath import FilePath


class LivePhoto(Photo):
    def __init__(self, photoPath: FilePath, videoPath: FilePath):
        self.videoExtension = videoPath.extension
        Photo.__init__(self, photoPath)


    def _renameFile(self):
        print(f"{self.path.getFullPath()} -> {self.getFullNewPath()}")
        print(f"   -> {self.newPath}.{self.newFileName}.{self.videoExtension}")
        return ""
