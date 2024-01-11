from dataclasses import dataclass
from misc.FileType import FileType

PHOTO_EXTS = {"heic", "png", "jpg", "jpeg"}
VIDEO_EXTS = {"mp4", "mov"}

@dataclass
class FilePath:
    def __init__(self, dir: str, name: str, ext: str, root: str):
        self.dir = dir
        self.name = name
        self.ext = ext.lower()
        self.path = dir + "/" + name + "." + ext
        self.ty = self._getFileTypeOf(self.ext)
        self.root = root
    
    @staticmethod
    def _getFileTypeOf(ext: str) -> FileType:
        if ext in PHOTO_EXTS:
            return FileType.PHOT0
        elif ext in VIDEO_EXTS:
            return FileType.VIDEO
        else:
            return FileType.OTHER

    def __str__(self):
        return f"path: {self.path}\ndir: {self.dir}\nname: {self.name}\next: {self.ext}\ntype: {self.ty.name}\n"
