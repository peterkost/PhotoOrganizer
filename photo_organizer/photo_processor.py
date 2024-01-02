from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from pillow_heif import register_heif_opener
from tqdm import tqdm

from misc.FilePath import FilePath

def processImages(filePaths: list[FilePath]):
    register_heif_opener()
    data = noCode = error = noExif = 0
    for i in tqdm(range(len(filePaths))):
        filePath = filePaths[i]
        try:
            image = Image.open(filePath.path)
            exif = image.getexif()
            if exif:
                date = exif.get(306, "Can't get code 306")
                if data != "Can't get code 306":
                    data += 1
                else:
                    noCode += 1
            else:
                noExif += 1
                print("No EXIF data for ", filePath)
        except Exception as e:
            error += 1
            print("Error processessing files", e)

    print(data, noCode, error, noExif)
    return []

