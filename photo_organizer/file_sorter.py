from typing import DefaultDict, List
from misc.FileInfo import FileInfo
from misc.FileType import FileType
from misc.Photo import Photo
from tqdm import tqdm


def sortFiles(filePaths: list[FileInfo]) -> List[Photo]:
    files = DefaultDict(list)

    for filePath in filePaths:
        if filePath.ty != FileType.OTHER:
            files[filePath.name].append(filePath)

    photos = []
    values = list(files.values())
    for i in tqdm(range(len(values))):
        paths = values[i]
        hasPhoto = any(path.ty == FileType.PHOT0 for path in paths)
        if hasPhoto :
            photos.append(Photo(paths))

    return photos
    
