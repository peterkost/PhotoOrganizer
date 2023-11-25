import argparse
import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from pillow_heif import register_heif_opener


def getFolderPath():
    parser = argparse.ArgumentParser(
        description="Get files in current directory.")
    parser.add_argument("folder_path", type=str,
                        help="Path to folder containing image files.")
    args = parser.parse_args()
    return args.folder_path


def getFilePaths(dir):
    register_heif_opener()
    try:
        files = os.listdir(dir)
        return [dir + "/" + file for file in files]
    except Exception as e:
        print("error opening: ", dir, e)
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


def main():
    folderPath = getFolderPath()
    filesInPaths = getFilePaths(folderPath)
    processFiles(filesInPaths)


if __name__ == "__main__":
    main()
