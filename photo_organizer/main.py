from file_reader import getFilesInArgDir 
from file_sorter import sortFiles
from photo_processor import addMetaDataToPhotos
from pillow_heif import register_heif_opener
#from video_processor import processVideos

def main():
    register_heif_opener()

    filePaths = getFilesInArgDir()
    groupedFiles = sortFiles(filePaths)
    noDate = 0
    for photo in groupedFiles:
        if not photo.dateTime:
            noDate += 1
            print(photo.paths[0].path)
    #processedPhotos = addMetaDataToPhotos(groupedFiles.photos)



if __name__ == "__main__":
    main()
