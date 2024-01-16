from typing import DefaultDict, List
from misc.FileInfo import FileInfo
from misc.FileType import FileType
from misc.Photo import Photo
from tqdm import tqdm
from dataclasses import dataclass
from typing import List
from misc.Photo import Photo


@dataclass
class Files:
    photos: List[Photo]
    videos: List[FileInfo]
    other: List[FileInfo]



def sortFiles(filePaths: list[FileInfo]) -> Files:
    potentialLivePhotos = DefaultDict(list)
    other = []

    for filePath in filePaths:
        if filePath.fileType == FileType.OTHER:
            other.append(filePath)
        else:
            potentialLivePhotos[filePath.folder+'/'+filePath.name].append(filePath)

    photos, videos = [], []
    values = list(potentialLivePhotos.values())
    for i in tqdm(range(len(values))):
        paths = values[i]
        
        if len(paths) == 1 and paths[0].fileType == FileType.VIDEO:
            videos.append(paths[0])
        else:
            photos.append(Photo(paths)) 


    return Files(photos, videos, other)
    
