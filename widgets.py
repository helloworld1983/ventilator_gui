import tkinter as tk

class UpDownWidget():
    def __init__(self, frame, title = "Value", xpos = 0, ypos = 0, default = 0.0, vmin = 0.0, vmax = 1.0, step = 0.1):
        self.canvas = tk.Canvas(frame, width = 200, height = 136, bg = "gray", bd=0, highlightthickness=0)
        self.canvas.place(x = xpos, y = ypos)
        
        self.canvas.create_text(30, 24, text = title, font = ("Arial","24","bold"), fill="darkgray")
        
        photo_down = tk.PhotoImage(file = "down.png")
        button_down = tk.Button(self.canvas, background="white", border = 2, image = photo_down, command = self.on_down)
        button_down.image = photo_down
        button_down.place(x = 0, y=64)
        
        photo_up = tk.PhotoImage(file = "up.png")
        button_up = tk.Button(self.canvas, background="white", border = 2, image = photo_up, command = self.on_up)
        button_up.image = photo_up
        button_up.place(x = 128, y=64)
        
        self.value = default
        self.step = step
        self.vmin = vmin
        self.vmax = vmax
        self.on_up()
    def on_up(self):
        self.value += self.step;
        if self.value > self.vmax:
            self.value = self.vmax;
         
        self.canvas.delete("tag_value")
        self.canvas.create_text(130, 24, text=str("{:6.2f}".format(self.value)), font = ("Arial","36"), fill="white", tag = "tag_value")
    def on_down(self):
        self.value -= self.step;
        if self.value < self.vmin:
            self.value = self.vmin;

        self.canvas.delete("tag_value")
        self.canvas.create_text(130, 24, text=str("{:6.2f}".format(self.value)), font = ("Arial","36"), fill="white", tag = "tag_value")
        
    def get_value(self):
        return self.value
        