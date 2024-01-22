#from typing import List
from file_path_reader import getFilePathsInArgDir 
from file_sorter import sortFiles
#from misc.Photo import Photo
#from video_processor import processVideos
#from photo_processor import generateFoldersFor
from pillow_heif import register_heif_opener
import pickle


usePickledFiles = False
pickledPhotoListName = 'photoList.p'

def main():
#    if usePickledFiles:
#        files = unpickleFiles()
#    else:
    filePaths = getFilePathsInArgDir()
    register_heif_opener()
    files = sortFiles(filePaths)
    [print(f"{x}\n  ↳{x.getFullNewPath()}") for x in files]
        #pickleFiles(photos=files)
    
    #processedPhotos = generateFoldersFor(files.photos)
    #processedVideos = processVideos(files.videos)


#def pickleFiles(photos: Files) -> None:
#    file = open(pickledPhotoListName, 'wb')
#    pickle.dump(photos, file)
#    file.close()
#
#def unpickleFiles() -> Files:
#    file = open(pickledPhotoListName, 'rb')
#    photos = pickle.load(file)
#    file.close()
#    return photos
#
if __name__ == "__main__":
    main()
