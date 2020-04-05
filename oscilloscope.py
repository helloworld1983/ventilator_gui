import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

from matplotlib import style
NB_POINTS = 100

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
        

        
        self.time_points = range(NB_POINTS)
        self.pressure_points = [0.0] * NB_POINTS
        self.volume_points = [0.0] * NB_POINTS
     
    def animate(self, i):
    
        self.ax1.clear()
        self.ax1.grid(True, color = 'dimgray')
        self.ax1.set(xlim = (0.0, NB_POINTS), ylim = (-0.2, 1.0))
        self.ax1.plot(self.time_points, self.volume_points)
        
        self.ax2.clear()
        self.ax2.grid(True, color = 'dimgray')
        self.ax2.set(xlim = (0.0, NB_POINTS), ylim = (-50.0, 50.0))         
        self.ax2.plot(self.time_points, self.pressure_points)  
    def get_figure(self):
        return self.fig
    def add_pressure_sample(self, pressure):
        self.pressure_points = self.pressure_points[1:] + self.pressure_points[:1]
        self.pressure_points[-1] = pressure
    
    def add_volume_sample(self, volume):
        self.volume_points = self.volume_points[1:] + self.volume_points[:1]
        self.volume_points[-1] = volume        