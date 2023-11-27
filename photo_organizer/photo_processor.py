from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from pillow_heif import register_heif_opener

def processImages(filePaths):
    register_heif_opener()
    return []

def processFiles(files):
    for filePath in files:
        try:
            image = Image.open(filePath)
            exif = image.getexif()
            if exif:
                date = exif.get(306, "???")
                print(filePath, date)
            else:
                print("No EXIF data for ", filePath)
        except Exception as e:
            print("Error processessing files", e)
