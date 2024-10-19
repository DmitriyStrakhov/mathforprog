import tkinter as tk
import random

class ArkanoidGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Arkanoid Game")
        self.canvas = tk.Canvas(root, width=400, height=400, bg='green')
        self.canvas.pack()
        
        self.ball = self.canvas.create_oval(330, 330, 350, 350, fill='yellow')
        self.ball_velocity_x = 10  
        self.ball_velocity_y = -10

        self.ball2 = self.canvas.create_oval(100, 100, 120, 120, fill='blue')  # Изменил начальную позицию второго шара
        self.ball_velocity_x2 = 5  
        self.ball_velocity_y2 = -5  
 
        
        self.start_button = tk.Button(root, text="начать", command=self.start_game)
        self.start_button.pack()
        
        self.is_running = False
        self.root.after(50, self.update_game)

    def start_game(self):
        self.is_running = not self.is_running
        self.start_button.config(text="Cтоп" if self.is_running else "Начать")

    def update_game(self):
        if self.is_running:
            self.ball_velocity_x, self.ball_velocity_y = self.move_ball(self.ball, self.ball_velocity_x, self.ball_velocity_y)
            self.ball_velocity_x2, self.ball_velocity_y2 = self.move_ball(self.ball2, self.ball_velocity_x2, self.ball_velocity_y2)
            self.check_collision()
        self.root.after(50, self.update_game)

    def move_ball(self, ball, velocity_x, velocity_y):
        self.canvas.move(ball, velocity_x, velocity_y)
        ball_position = self.canvas.coords(ball)
        
        if ball_position[1] <= 0 or ball_position[1] >= 400:  # Изменил на 400
            velocity_y = -velocity_y
            self.create_sparks(ball_position[0], ball_position[1])
        if ball_position[0] <= 0 or ball_position[0] >= 400:  # Изменил на 400
            velocity_x = -velocity_x
            self.create_sparks(ball_position[0], ball_position[1])
        
        return velocity_x, velocity_y

    def check_collision(self):
        pos1 = self.canvas.coords(self.ball)
        pos2 = self.canvas.coords(self.ball2)
        
        if self.is_collision(pos1, pos2):
            self.ball_velocity_x, self.ball_velocity_x2 = -self.ball_velocity_x, -self.ball_velocity_x2
            self.ball_velocity_y, self.ball_velocity_y2 = -self.ball_velocity_y, -self.ball_velocity_y2

    def is_collision(self, pos1, pos2):
        return not (pos1[0] + 20 < pos2[0] or pos1[0] > pos2[0] + 20 or pos1[1] + 20 < pos2[1] or pos1[1] > pos2[1] + 20)

    def create_sparks(self, x, y):
        for _ in range(5):
            spark = self.canvas.create_oval(x-5, y-5, x+5, y+5, fill='red')
            self.canvas.after(100, self.canvas.delete, spark)  

if __name__ == "__main__":
    root = tk.Tk()
    game = ArkanoidGame(root)
    root.mainloop()
