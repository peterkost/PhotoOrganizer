#from typing import List
from file_reader import getFilesInArgDir 
#from file_sorter import Files, sortFiles
#from misc.Photo import Photo
#from video_processor import processVideos
#from photo_processor import generateFoldersFor
#from pillow_heif import register_heif_opener
import pickle


usePickledFiles = False
pickledPhotoListName = 'photoList.p'

def main():
#    if usePickledFiles:
#        files = unpickleFiles()
#    else:
    filePaths = getFilesInArgDir()
        #register_heif_opener()
        #files = sortFiles(filePaths)
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

#
## ==================
#PHOTO_EXTS = {"heic", "png", "jpg", "jpeg"}
#VIDEO_EXTS = {"mp4", "mov"}
#def getFileType(extension: str) -> FileType:
#    if extension in PHOTO_EXTS:
#        return FileType.PHOT0
#    elif extension in VIDEO_EXTS:
#        return FileType.VIDEO
#    else:
#        return FileType.OTHER
#
#
#
##====================
#def _guessYear(self) -> str:
#    dir = self.folder
#        
#    yearRegex = re.compile(r'^(1|2)\d{3}$')
#    for s in dir.split('/'):
#        if yearRegex.match(s):
#            return s
#    return ''
