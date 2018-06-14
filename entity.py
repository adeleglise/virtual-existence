class Entity:
    """
    A genereic object to represent player
    """
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        #Move the entity by a certain amount
        self.x += dx
        self.y += dy
