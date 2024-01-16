from collections import defaultdict
from misc.Photo import Photo

def generateFoldersFor(photos: list[Photo]):
    dirs = defaultdict(list)
    for p in photos:
        dirs[p.newPath].append(p)

    for ps in dirs.values():
        ps.sort()
        for i, e in enumerate(ps):
            e.setNewFileName(i+1)


    i = 0
    while i < 20:
        p = photos[i]
        newPath = f"{p.newPath}/{p.newFileName}.{p.photoPath.extension}"
        print(newPath)

        i += 1


