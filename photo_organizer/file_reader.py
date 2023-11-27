import argparse
import os

def readFilePaths() -> list[str]:
    folderPath = _getFolderPath()
    filesInPaths = _getFilesInPath(folderPath)
    return filesInPaths 


def _getFolderPath() -> str:
    parser = argparse.ArgumentParser(
        description="Get files in current directory.")
    parser.add_argument("folder_path", type=str,
                        help="Path to folder containing image files.")
    args = parser.parse_args()
    return args.folder_path


def _getFilesInPath(dir: str) -> list[str]:
    try:
        files = os.listdir(dir)
        return [dir + "/" + file for file in files]
    except Exception as e:
        print("error opening: ", dir, e)
        return []


