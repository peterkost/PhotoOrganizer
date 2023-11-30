class FilePaths:
    def __init__(self, photos: list[str], videos: list[str], other: list[str] = []):
        self.photos = photos
        self.videos = videos
        self.other = other

    def __str__(self) -> str:
        return f"{len(self.photos)} photos\n{len(self.videos)} videos\n{len(self.other)} others"
