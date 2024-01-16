from datetime import datetime
import imageio_ffmpeg
import os
import imageio
from tqdm import tqdm
import subprocess 
import re


regex_pattern = r"creation_time\s*:\s*(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z)"


def processVideos(filePaths):
    for i in tqdm(range(len(filePaths))):
        file = filePaths[i]
        try:
            command = ['ffmpeg', '-i', file.fullPath]
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


            match = re.search(regex_pattern, result.stderr)

            if match:
                date = match[0].split(' ')[-1]
                creation_time = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
            else:
                print("Creation time not found in FFmpeg output.")

        except Exception as e:
            print("error", e)


