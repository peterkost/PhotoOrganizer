from collections import defaultdict
from misc.Photo import Photo
import re

def generateFoldersFor(photos: list[Photo]):
    inventory = {}
    noDate = defaultdict(int)
    for p in photos:
        if p.dateTime:
            year, month = p.dateTime.year, p.dateTime.month
            if year not in inventory:
                inventory[year] = [0] * 13
            inventory[year][month - 1] += 1
        else:
            noDate[p.photoPath.dir] += 1
            guess = guessYear(p)
            if guess:
                year = int(guess)
                if year not in inventory:
                    inventory[year] = [0] * 13
                inventory[year][-1] += 1

    stats = list(inventory.items())
    stats.sort()
    for year, months in stats:
        print(year, months)
    guessedYear, noDateCount = sum(x[1][-1] for x in stats), sum(noDate.values())
    print("photos with no date:", noDateCount)
    print("guessed years:", guessedYear)
    print("no date even with guess:", noDateCount - guessedYear)
    #print("----Photos without dates----")
    #for path, count in noDate.items():
    #    print(path, count)


def guessYear(p: Photo) -> str:
    dir = p.photoPath.dir
    
    yearRegex = re.compile(r'^(1|2)\d{3}$')
    for s in dir.split('/'):
        if yearRegex.match(s):
            return s
    return ''

