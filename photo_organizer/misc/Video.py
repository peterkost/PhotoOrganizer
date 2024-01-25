import re
import subprocess 
#rom typing import override
from datetime import datetime

from misc.File import File
from misc.FilePath import FilePath


CREATION_TIME_REGEX = r"creation_time\s*:\s*(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z)"

class Video(File):
    def __init__(self, path: FilePath):
        File.__init__(self, path)
        

    #@override
    def _setDateTime(self):
        try:
            command = ['ffmpeg', '-i', self.path.getFullPath()]
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            match = re.search(CREATION_TIME_REGEX, result.stderr)
            if match:
                date = match[0].split(' ')[-1]
                self.dateTime = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
            else:
                print("Creation time not found in FFmpeg output.")

        except Exception as e:
            print("error", e)


    def _renameFile(self):
        print(f"{self.path.getFullPath()} -> {self.getFullNewPath()}")
        return ""
    
