from ball import Ball
import os
from sleep import sleep
from canvas import Canvas


@sleep(0.05)
def draw(st):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(st)
    

def main():
    ball1 = Ball(20, 10, 2, mx=100)
    ball2 = Ball(50, 10, mx=100)
    canvas = Canvas(100, 40)
    canvas.add(ball1)
    canvas.add(ball2)

    while True:
        canvas.update()
        draw(canvas)
        # ball1.update()
        # draw(ball1)


if __name__ == '__main__':
    main()