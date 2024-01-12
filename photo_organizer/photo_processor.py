from collections import defaultdict
from misc.Photo import Photo
import re

def generateFoldersFor(photos: list[Photo]):
    dirs = defaultdict(list)
    for p in photos:
        dirs[p.newPath].append(p)

    for dir, ps in dirs.items():
        ps.sort()
        for i, e in enumerate(ps):
            name = f"{e.dateTime.strftime('%Y.%m.%d')}-IMG_{i:03d}"
            e.setNewFileName(name)
            print(name)

        break
