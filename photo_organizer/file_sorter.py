from tqdm import tqdm
from typing import DefaultDict, List

from misc.FilePath import FilePath
from misc.Types import FileType
from misc.Photo import Photo
from misc.File import File
from misc.Photo import Photo
from misc.Video import Video
from misc.LivePhoto import LivePhoto


# goal -> by the end of this function, each of the files shold have all of the necessary info to be renmaed
def sortFiles(filePaths: List[FilePath]) -> List[File]:
    files = createFiles(filePaths)
    setNewFileNames(files)
    return files



def createFiles(filePaths: List[FilePath]) -> List[File]:
    files = []
    pathsWithSameName = DefaultDict(list)
    [pathsWithSameName[filePath.getLivePhotoMatchKey()].append(filePath) for filePath in filePaths]

    fileNames = list(pathsWithSameName.values())
    for i in tqdm(range(len(fileNames))):
        pathsWithSameName = fileNames[i]

        photoPath = videoPath = otherPath = None
        for path in pathsWithSameName:
            match path.getFileType():
                case FileType.PHOT0:
                    if photoPath: raise Exception("Photo path being replaced!")
                    photoPath = path
                case FileType.VIDEO:
                    if videoPath: raise Exception("Video path being replaced!")
                    videoPath = path
                case FileType.OTHER:
                    if otherPath: raise Exception("Other path being replaced!")
                    otherPath = otherPath

        if photoPath and videoPath:
            files.append(LivePhoto(photoPath, videoPath))
        elif photoPath:
            files.append(Photo(photoPath))
        elif videoPath:
            files.append(Video(videoPath))
        else:
            print(f"Coldn't figure out what to do with paths!\n{pathsWithSameName},{photoPath}, {videoPath}, {otherPath}")
    return files    


def setNewFileNames(files: List[File]) -> None:
    filesByFolder = DefaultDict(list)
    [filesByFolder[file.newPath].append(file) for file in files]

    for folderGroup in filesByFolder.values():
        folderGroup.sort()
        [file.setNewFileName(i+1) for i, file in enumerate(folderGroup)]
