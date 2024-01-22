import os
import argparse
from misc.FilePath import FilePath
from typing import List


def getFilePathsInArgDir() -> List[FilePath]:
    argDir = getDirFromArgs()
    return getFiles(argDir)


def getDirFromArgs() -> str:
    parser = argparse.ArgumentParser(
        description="Get files in current directory.")
    parser.add_argument("folder_path", type=str,
                        help="Path to folder containing media files.")
    args = parser.parse_args()
    return args.folder_path


def getFiles(dir: str) -> List[FilePath]:
    filePaths = []
    try:
        files = os.listdir(dir)
        for file in files:
            if os.path.isdir(f"{dir}/{file}"):
                filePaths += getFiles(f"{dir}/{file}")
            else:
                name, extensionRaw = os.path.splitext(file)
                extension = extensionRaw.lower().replace('.', '')
                filePaths.append(FilePath(dir, name, extension))
        return filePaths
    except Exception as e:
        print(f"Exception occured while reading file in {dir}\n{e}")
        exit(1)
