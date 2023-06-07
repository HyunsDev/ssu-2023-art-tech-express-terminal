import p5


class AssetManager:
    def __init__(self):
        self.preloadFonts = {}
        self.fonts = {}

        self.preloadImages = {}
        self.images = {}

    def getFont(self, name):
        return self.fonts[name]

    def getImage(self, name):
        return self.images[name]

    def addFont(self, name, path):
        self.preloadFonts[name] = path

    def addImage(self, name, path):
        self.preloadImages[name] = path

    def load(self):
        for name, path in self.preloadFonts.items():
            self.fonts[name] = p5.load_font(path)

        for name, path in self.preloadImages.items():
            self.images[name] = p5.load_image(path)
