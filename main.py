from p5react import *
from screen import Router
import builtins

builtins.cameraId = 1

window = Window(1280, 720)
window.init()

window.assets.addFont("NotoSerifKR-Regular", "assets/fonts/NotoSerifKR-Regular.otf")
window.assets.addFont("NotoSansKR-Regular", "assets/fonts/NotoSansKR-Regular.otf")
window.assets.addFont("NotoSansKR-Bold", "assets/fonts/NotoSansKR-Bold.otf")
window.assets.addFont("D2Coding", "assets/fonts/D2Coding.ttf")

window.assets.addImage("img1.png", "assets/images/img1.png")
window.assets.addImage("img2.png", "assets/images/img2.png")
window.assets.addImage("img3.png", "assets/images/img3.png")
window.assets.addImage("img4.png", "assets/images/img4.png")
window.assets.addImage("img5.png", "assets/images/img5.png")
window.assets.addImage("img6.png", "assets/images/img6.png")

window.assets.addImage("x-black.png", "assets/images/x-black.png")
window.assets.addImage("x-white.png", "assets/images/x-white.png")
window.assets.addImage("x.png", "assets/images/x.png")


window.setRoot(Router)
window.run()
