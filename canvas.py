class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)

    def update(self):
        for obj in self.objects:
            obj.update()
    
    def __str__(self):
        result = ''
        cords = []
        for obj in self.objects:
            cords += obj.cords()
        cords = set(cords)
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in cords:
                    result += '@'
                elif x == 0 or y == 0 or x == self.width - 1 or y == self.height - 1:
                    result += '#'
                else:
                    result += ' '
            result += '\n'
        return result