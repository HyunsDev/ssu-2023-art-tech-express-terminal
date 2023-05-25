from ..share.workClass import Work
from context import assetsContext

class Work1(Work):
    def __init__(self) -> None:
        super().__init__(assetsContext.images['img1.png'], '#A58660')

    pass