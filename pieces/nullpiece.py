WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from pieces.piece import piece


class nullpiece(piece):
    alliance = None
    def __init__(self):
        pass

    def tostring(self):
        return "-"

