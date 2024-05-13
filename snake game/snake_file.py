from turtle import Turtle

FORWARD = 20
DIRECTION_LIST = [0,90,180,270]
class Snake:
    
    def __init__(self) -> None:
        self.square_segments = []
        self.snake_making()
        
    def snake_making(self):
        for _ in range(0,3): 
            self.add_segment(0,0) 
            
        
    def add_segment(self,x,y):
        square = Turtle()
        square.shape("square")
        square.shapesize(stretch_wid=1,stretch_len=1)
        square.color("white")
        square.penup()
        square.goto(x,y)
        x = x-20
        self.square_segments.append(square)
        
    
    # Extending the snake
    def extend_snake(self):
        x_cordinate = self.square_segments[-1].xcor()
        y_cordinate = self.square_segments[-1].ycor()
        self.add_segment(x_cordinate,y_cordinate)
        
    
    def move(self):
        for segment in range(len(self.square_segments)-1,0,-1 ):
            new_x = self.square_segments[segment-1].xcor()
            new_y = self.square_segments[segment-1].ycor()
            self.square_segments[segment].goto(new_x,new_y)
        self.square_segments[0].forward(FORWARD)
        
    def right(self):
        if self.square_segments[0].heading() != DIRECTION_LIST[2]:
            self.square_segments[0].setheading(DIRECTION_LIST[0])
        
    def left(self):
        if self.square_segments[0].heading() != DIRECTION_LIST[0]:
            self.square_segments[0].setheading(DIRECTION_LIST[2])
        
    def up(self):
        if self.square_segments[0].heading() != DIRECTION_LIST[3]:
            self.square_segments[0].setheading(DIRECTION_LIST[1])
            
    def down(self):
        if self.square_segments[0].heading() != DIRECTION_LIST[1]:
            self.square_segments[0].setheading(DIRECTION_LIST[3])
    
    