# -*- coding: utf-8 -*-
import tkinter as tk
#import tkFont
import os
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import numpy as np



class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.wm_title("Ventilator")
        if "nt" in os.name:
            #Pour debug sur laptop avec 2e ecran
            x,y = -1400,-650
        else:
            #sur le pi
            #self.root.attributes('-fullscreen', True)
            x,y = -80,-34
        self.w,self.h = 1280,800
        self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, x, y))

        self.root.bind("<Button-1>", self.onLeftClick)
        self.root.bind('<KeyPress>', self.onKeyPress)
        self.canvas = tk.Canvas(self.root, width=self.w, height=self.h, borderwidth=0, highlightthickness=0, bg="blue")
        #self.canvas.grid()

        #plot
        style.use('dark_background')
        fig, (self.ax1, self.ax2) = plt.subplots(2, sharex=True)
        canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        canvas.draw()
        #canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        canvas.get_tk_widget().pack(fill=tk.X)

        
 #       self.on_timer()       
        ani = animation.FuncAnimation(fig, self.animate, interval = 1000)      
        self.root.mainloop()
    def onKeyPress(self, e):
        print(ord(e.char))
        #exit on escape
        if ord(e.char) == 27:
            self.root.destroy()
#        if e.char == "c":
#            self.canvas.delete("tagvitesse")
    def animate(self, i):
        graph_data = open('samplefile.txt','r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                xs.append(int(x))
                ys.append(int(y))
        self.ax1.clear()
        self.ax2.clear()
        self.ax1.plot(xs, ys)
        self.ax2.plot(xs, ys)
    
    def onLeftClick(self, e):
        self.root.destroy()
#    def on_timer(self):
#        self.root.after(1500, self.on_timer)
        


app=App()
