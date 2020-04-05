# -*- coding: utf-8 -*-
import tkinter as tk
#import tkFont
import os
import math
import matplotlib.animation as animation
import numpy as np
from oscilloscope import *
import random

OSCILLOSCOPE_REFRESH_INTERVAL = 100
        
class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.wm_title("Ventilator")
        if "nt" in os.name:
            #set the window position
            #x,y = -1400,-650
            x,y = 0,0
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

        self.oscilloscope = Oscilloscope(self.root)
        ani = animation.FuncAnimation(self.oscilloscope.get_figure(), self.oscilloscope.animate, interval = OSCILLOSCOPE_REFRESH_INTERVAL)
        self.p = 0.0
        self.increase_p = True
        
        self.v = 0.0
        self.increase_v = True        
        
        random.seed()
        
        self.on_timer()       
        self.root.mainloop()
        
    def onKeyPress(self, e):
        print(ord(e.char))
        #exit on escape
        if ord(e.char) == 27:
            self.root.destroy()
#        if e.char == "c":
#            self.canvas.delete("tagvitesse")

    
    def onLeftClick(self, e):
        self.root.destroy()
    def on_timer(self):
        self.root.after(OSCILLOSCOPE_REFRESH_INTERVAL, self.on_timer)
        
        
        #pressure
        if self.p > 25.0:
            self.increase_p = False
        elif self.p < -10.0:
            self.increase_p = True
            
        if self.increase_p:
            self.p += 2.0
        else:
            self.p -= 3.2
        self.p += 5.0 * (random.random() - 0.5)
            
        self.oscilloscope.add_pressure_sample(self.p);    
            
            
        #volume
        if self.v > 0.5:
            self.increase_v = False
        elif self.v < 0.0:
            self.increase_v = True
            
        if self.increase_v:
            self.v += 0.02
        else:
            self.v -= 0.1            
        self.v += 0.02 * (random.random() - 0.5)
        
        
        self.oscilloscope.add_volume_sample(self.v);
        


app=App()
