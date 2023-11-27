from file_reader import readFilePaths 
from file_sorter import sortFiles
from photo_processor import processImages
from video_processor import processVideos

# MVP: Renames photos and videos to Date - 01 

# Get exif for photos
    # Match photo with video for live photos
# Get create date for videos
def main():
    filePaths = readFilePaths()
    print(filePaths)
    #groupedFiles = sortFiles(filePaths)
    #processedPhotos = processImages(groupedFiles)
    #processedVideos = processImages(groupedFiles)


if __name__ == "__main__":
    main()
