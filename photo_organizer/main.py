from typing import List
from file_reader import getPathsOfFilesIn 
from file_sorter import Files, sortFiles
from misc.Photo import Photo
from video_processor import processVideos
from photo_processor import generateFoldersFor
from pillow_heif import register_heif_opener
import pickle
import argparse


usePickledFiles = True
pickledPhotoListName = 'photoList.p'

def main():
    rootDir = getDir()
    if usePickledFiles:
        files = unpickleFiles()
    else:
        filePaths = getPathsOfFilesIn(rootDir, rootDir)
        register_heif_opener()
        files = sortFiles(filePaths)
        pickleFiles(photos=files)
    
    #processedPhotos = generateFoldersFor(files.photos)
    processedVideos = processVideos(files.videos)

def getDir() -> str:
    parser = argparse.ArgumentParser(
        description="Get files in current directory.")
    parser.add_argument("folder_path", type=str,
                        help="Path to folder containing media files.")
    args = parser.parse_args()
    return args.folder_path

def pickleFiles(photos: Files) -> None:
    file = open(pickledPhotoListName, 'wb')
    pickle.dump(photos, file)
    file.close()

def unpickleFiles() -> Files:
    file = open(pickledPhotoListName, 'rb')
    photos = pickle.load(file)
    file.close()
    return photos

if __name__ == "__main__":
    main()
