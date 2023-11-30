from misc.FilePaths import FilePaths
from misc.FilePath import FilePath
from misc.FileType import FileType

def sortFiles(filePaths: list[FilePath]) -> FilePaths:
    photos,videos, other = [], [], []
    for filePath in filePaths:
        match filePath.ty:
            case FileType.PHOT0:
                photos.append(filePath)
            case FileType.VIDEO:
                videos.append(filePath)
            case _:
                other.append(filePath)
    return FilePaths(photos, videos, other)
    
