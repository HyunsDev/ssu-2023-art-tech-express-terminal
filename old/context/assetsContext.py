from p5 import *


class AssetsContext:
    def __init__(self) -> None:
        self.fonts = {}
        self.images = {}
        pass

    def init(self):
        self.fonts["NotoSerifKR-Regular"] = load_font(
            "assets/fonts/NotoSerifKR-Regular.otf"
        )
        self.fonts["NotoSansKR-Regular"] = load_font(
            "assets/fonts/NotoSansKR-Regular.otf"
        )
        self.fonts["NotoSansKR-Bold"] = load_font("assets/fonts/NotoSansKR-Bold.otf")

        self.images["img1.png"] = load_image("assets/images/img1.png")
        self.images["img2.png"] = load_image("assets/images/img1.png")
        self.images["img3.png"] = load_image("assets/images/img1.png")
        self.images["img4.png"] = load_image("assets/images/img1.png")

        pass


assetsContext = AssetsContext()
__all__ = ["assetsContext"]
