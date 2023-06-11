from p5react import *
from screen import Router

window = Window(1280, 720)
window.init()

window.assets.addFont("NotoSerifKR-Regular", "assets/fonts/NotoSerifKR-Regular.otf")
window.assets.addFont("NotoSansKR-Regular", "assets/fonts/NotoSansKR-Regular.otf")
window.assets.addFont("NotoSansKR-Bold", "assets/fonts/NotoSansKR-Bold.otf")
window.assets.addImage("img1.png", "assets/images/img1.png")
window.assets.addImage("img2.png", "assets/images/img2.png")
window.assets.addImage("img3.png", "assets/images/img1.png")
window.assets.addImage("img4.png", "assets/images/img1.png")


window.setRoot(Router)
window.run()
