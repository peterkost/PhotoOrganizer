from typing import List
from file_reader import getPathsOfFilesIn 
from file_sorter import sortFiles
from misc.Photo import Photo
from photo_processor import generateFoldersFor
from pillow_heif import register_heif_opener
import pickle
import argparse


usePickledPhotos= True
pickledPhotoListName = 'photoList.p'

def main():
    rootDir = getDir()
    if usePickledPhotos:
        photos = unpicklePhotos()
    else:
        filePaths = getPathsOfFilesIn(rootDir, rootDir)
        register_heif_opener()
        photos = sortFiles(filePaths)
        picklePhotos(photos=photos)

    processedPhotos = generateFoldersFor(photos)

def getDir() -> str:
    parser = argparse.ArgumentParser(
        description="Get files in current directory.")
    parser.add_argument("folder_path", type=str,
                        help="Path to folder containing media files.")
    args = parser.parse_args()
    return args.folder_path

def picklePhotos(photos: List[Photo]) -> None:
    file = open(pickledPhotoListName, 'wb')
    pickle.dump(photos, file)
    file.close()

def unpicklePhotos() -> List[Photo]:
    file = open(pickledPhotoListName, 'rb')
    photos = pickle.load(file)
    file.close()
    return photos

if __name__ == "__main__":
    main()
