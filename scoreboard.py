from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        
        self.score = 0
        with open("highscore.txt")as data:
            self.high_score = int(data.read())
        self.goto(0, 270)
        self.ht()
        self.penup()
        self.color("White")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}" , align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("highscore.txt", mode="w") as data: 
                data.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.update_scoreboard()
