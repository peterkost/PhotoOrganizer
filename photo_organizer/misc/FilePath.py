from misc.FileType import FileType

PHOTO_EXTS = set(["HEIC", "PNG", "JPG"])
VIDEO_EXTS = set(["MP4", "MOV"])

class FilePath:
    def __init__(self, dir: str, name: str, ext: str):
        self.dir = dir
        self.name = name
        self.ext = ext
        self.path = dir + name + "." + ext
        self.ty = self._getFileTypeOf(ext)
    
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
