from dataclasses import dataclass

from misc.Types import FileType


PHOTO_EXTS = {"heic", "png", "jpg", "jpeg"}
VIDEO_EXTS = {"mp4", "mov"}


@dataclass
class FilePath:
    dir: str
    name: str
    extension: str


    def getFullPath(self) -> str:
        return f"{self.dir}/{self.name}.{self.extension}"
    

    def getLivePhotoMatchKey(self) -> str:
        return f"{self.dir}/{self.name}"


    def getFileType(self) -> FileType:
        ext = self.extension.lower()
        if ext in PHOTO_EXTS:
            return FileType.PHOT0
        elif ext in VIDEO_EXTS:
            return FileType.VIDEO
        else:
            return FileType.OTHER


    def __str__(self) -> str:
        return self.getFullPath()

