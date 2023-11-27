import argparse
import os

from misc.FilePath import FilePath

def getFilesInArgDir() -> list[FilePath]:
    dir = _getDir()
    filePaths = _getPathsOfFilesIn(dir)
    return filePaths 


def _getDir() -> str:
    parser = argparse.ArgumentParser(
        description="Get files in current directory.")
    parser.add_argument("folder_path", type=str,
                        help="Path to folder containing media files.")
    args = parser.parse_args()
    return args.folder_path


def _getPathsOfFilesIn(dir: str) -> list[FilePath]:
    try:
        filePaths = []
        files = os.listdir(dir)
        for file in files:
            name, ext = os.path.splitext(file)
            filePaths.append(FilePath(dir, name, ext[1:]))
        return filePaths
    except Exception as e:
        print(e)
        exit(1)


