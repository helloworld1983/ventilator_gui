import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

from matplotlib import style
NB_POINTS = 50

class Oscilloscope():
    def __init__(self, tkroot):
        #plot
        style.use('dark_background')
        self.fig, (self.ax1, self.ax2) = plt.subplots(2, sharex=True)
        canvas = FigureCanvasTkAgg(self.fig, master=tkroot)  # A tk.DrawingArea.
        canvas.draw()
        #canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        canvas.get_tk_widget().pack(fill=tk.X)
        
        self.ax1.autoscale(False)
        self.ax2.autoscale(False)  
        self.fig.subplots_adjust(left=0.12, bottom=0.1, right=0.98, wspace=0.2, hspace=0.2)
        
        self.ax1.grid(True, color = 'dimgray')
        self.ax2.grid(True, color = 'dimgray')
        self.ax1.set(xlim = (0.0, NB_POINTS), ylim = (-0.2, 1.0))
        self.ax2.set(xlim = (0.0, NB_POINTS), ylim = (-50.0, 50.0))         
        
        
        #Volume
        txt = tk.Label(tkroot, text = "V", fg = "white", bg = "black", font=("Arial", 44))
        txt.place(x = 10, y = 250)
        txt = tk.Label(tkroot, text = "[L]", fg = "gray", bg = "black", font=("Arial", 14))
        txt.place(x = 50, y = 300)
        
        
        #Pressure
        txt = tk.Label(tkroot, text = "P", fg = "white", bg = "black", font=("Arial", 44))
        txt.place(x = 10, y = 450)
        txt = tk.Label(tkroot, text = "[cm H2O]", fg = "gray", bg = "black", font=("Arial", 14))
        txt.place(x = 30, y = 500)        
        
        self.time_points = range(NB_POINTS)
        self.pressure_points = [0.0] * NB_POINTS
        self.volume_points = [0.0] * NB_POINTS
     
    def animate(self, i):
        if len(self.ax1.lines) > 0:
            self.ax1.lines[0].remove()        
        self.ax1.plot(self.time_points, self.volume_points, color = "red")
        
        if len(self.ax2.lines) > 0:
            self.ax2.lines[0].remove()
        
        self.ax2.plot(self.time_points, self.pressure_points, color = "blue")  
    def get_figure(self):
        return self.fig
    def add_pressure_sample(self, pressure):
        self.pressure_points = self.pressure_points[1:] + self.pressure_points[:1]
        self.pressure_points[-1] = pressure
    
    def add_volume_sample(self, volume):
        self.volume_points = self.volume_points[1:] + self.volume_points[:1]
        self.volume_points[-1] = volume        