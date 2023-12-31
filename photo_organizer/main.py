from file_reader import getFilesInArgDir 
from file_sorter import sortFiles
from photo_processor import processImages
#from video_processor import processVideos

def main():
    filePaths = getFilesInArgDir()
    groupedFiles = sortFiles(filePaths)
    processedPhotos = processImages(groupedFiles.photos)
    #processedVideos = processImages(groupedFiles)


if __name__ == "__main__":
    main()
