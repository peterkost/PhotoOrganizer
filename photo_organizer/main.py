from file_reader import getFilesInArgDir 
from file_sorter import sortFiles
from photo_processor import addMetaDataToPhotos
from pillow_heif import register_heif_opener
import pickle
#from video_processor import processVideos


usePickle = True


def main():
    register_heif_opener()

    
    if usePickle:
        groupedFiles = unpickle()
        
    else:
        filePaths = getFilesInArgDir()
        groupedFiles = sortFiles(filePaths)
        funniestShitIveEverSeen(groupedFiles)

    noDate = date = 0
    for photo in groupedFiles:
        if not photo.dateTime:
            noDate += 1
            print(photo.paths[0].path)
        else:
            date += 1
    #processedPhotos = addMetaDataToPhotos(groupedFiles.photos)
    print("date", date, "nodate", noDate)


def funniestShitIveEverSeen(obj):
    file = open('funnestShitIveEverSeen', 'ab')
    pickle.dump(obj, file)
    file.close()

def unpickle():
    file = open("funnestShitIveEverSeen", 'rb')
    p = pickle.load(file)
    file.close()
    return p

if __name__ == "__main__":
    main()
