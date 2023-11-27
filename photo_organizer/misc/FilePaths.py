class FilePaths:
    def __init__(self, photos: list[str], videos: list[str], other: list[str] = []):
        self.photos = photos
        self.videos = videos
        self.other = other
