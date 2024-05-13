from turtle import Turtle,Screen

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        self.score = 0
        self.penup()
        self.goto(0,350)
        self.speed("fastest")
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self):
        self.write(f"Score is {self.score}", move=False, align='center', font=('Arial', 20, 'normal'))        
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over...", move=False, align='center', font=('Arial', 20, 'normal'))
        
    def is_increase(self):
        self.score = self.score + 1
        self.clear()
        self.update_scoreboard()
        
        
# is_score = Scoreboard()
 
# screen = Screen()
# screen.exitonclick()