from Gameobject import Gameobject

class Player(Gameobject):
    def __init__(self, pos, width, height, img, game):
        super().__init__(self, pos, width, height, img, game)

        self.speed = 3
        self.direction = 0
        self.x_velocity = 0
        self.y_velocity = 0