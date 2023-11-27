import argparse
import os


def getFilesInArgDir() -> list[str]:
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


def _getPathsOfFilesIn(dir: str) -> list[str]:
    try:
        files = os.listdir(dir)
        return [dir + "/" + file for file in files]
    except Exception as e:
        print("error opening: ", dir, e)
        return []


