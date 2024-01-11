from typing import List
from file_reader import getFilesInArgDir 
from file_sorter import sortFiles
from misc.Photo import Photo
from photo_processor import addMetaDataToPhotos
from pillow_heif import register_heif_opener
import pickle
#from video_processor import processVideos


usePickledPhotos= True
pickledPhotoListName = 'photoList.p'


def main():
    if usePickledPhotos:
        photos = unpicklePhotos()
    else:
        filePaths = getFilesInArgDir()
        register_heif_opener()
        photos = sortFiles(filePaths)
        picklePhotos(photos=photos)

    processedPhotos = addMetaDataToPhotos(photos)


def picklePhotos(photos: List[Photo]) -> None:
    file = open(pickledPhotoListName, 'ab')
    pickle.dump(photos, file)
    file.close()

def unpicklePhotos() -> List[Photo]:
    file = open(pickledPhotoListName, 'rb')
    photos = pickle.load(file)
    file.close()
    return photos

if __name__ == "__main__":
    main()
