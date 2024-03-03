from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("./highscore.txt", mode = "r") as f:
            self.highscore = int(f.read())
        self.color("white")
        self.penup()
        self.goto(0,280)   
        self.update()  
        self.hideturtle()
        
        

    def update(self):

        self.clear()
        self.write(f"Score : {self.score} HighScore: {self.highscore}" , False , align="center", font=("Courier" , 12 , "normal")) 

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("snake_game\highscore.txt", mode = "w") as f:
                    f.write(str(self.highscore))

        self.score = 0      
        self.update()

    def increase_score(self):
            self.score += 1
            self.update()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(" Game Over. " , False , align="center", font=("Courier" , 18 , "normal"))  