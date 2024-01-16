from dataclasses import dataclass
from misc.FileType import FileType

PHOTO_EXTS = {"heic", "png", "jpg", "jpeg"}
VIDEO_EXTS = {"mp4", "mov"}

@dataclass
class FileInfo:
    def __init__(self, dir: str, name: str, ext: str, root: str):
        self.folder = dir
        self.name = name
        self.extension = ext.lower()
        self.fullPath = dir + "/" + name + "." + ext
        self.fileType = self._getFileTypeOf(self.extension)
        self.rootFolder = root
    
    @staticmethod
    def _getFileTypeOf(ext: str) -> FileType:
        if ext in PHOTO_EXTS:
            return FileType.PHOT0
        elif ext in VIDEO_EXTS:
            return FileType.VIDEO
        else:
            return FileType.OTHER

    def __str__(self):
        return f"path: {self.fullPath}\ndir: {self.folder}\nname: {self.name}\next: {self.extension}\ntype: {self.fileType.name}\n"
