class Ball:
    def __init__(self, x=0, y=0, vx=0, vy=0, mx=0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.g = -1
        self.mx = mx
    
    def update(self):
        if self.y + self.vy < 0:
            self.y = -(self.y + self.vy)
            self.vy *= -1 * 0.8
        else:
            self.y += self.vy
        if (self.x + self.vx) < 0 or (self.x + self.vx) > self.mx:
            self.x = -((self.x + self.vx) % self.mx) + self.mx
            self.vx *= -1
        else:
            self.x += self.vx
        self.vy += self.g

    def __str__(self) -> str:
        return f'{self.x}, {self.y}, {self.vx}, {self.vy}'
    
    def cords(self):
        return [
            (self.x, self.y * -1 + 40),
            (self.x + 1, self.y * -1 + 40),
            (self.x - 1, self.y * -1 + 40),
            (self.x, self.y * -1 + 40 - 1),
            (self.x, self.y * -1 + 40 + 1),
            ]