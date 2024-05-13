from turtle import Turtle,Screen
import random

class Food(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        
        self.shape("circle")
        self.shapesize(stretch_len=0.75,stretch_wid=0.75)
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        self.goto(random.randint(-290,290),random.randint(-290,290))
        
        
# food = Food()


# screen = Screen()
# screen.exitonclick()