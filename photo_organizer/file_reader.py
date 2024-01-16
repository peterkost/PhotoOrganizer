import os
from misc.FileInfo import FileInfo


def getPathsOfFilesIn(dir: str, rootDir: str) -> list[FileInfo]:
    try:
        filePaths = []
        files = os.listdir(dir)
        for file in files:
            d = f"{dir}/{file}"
            if os.path.isdir(d):
                filePaths += getPathsOfFilesIn(d, rootDir)
            else:
                name, ext = os.path.splitext(file)
                filePaths.append(FileInfo(dir, name, ext[1:], rootDir))
        return filePaths
    except Exception as e:
        print(e)
        exit(1)


