# ventilator_gui

## How to install:

```shell
$ git clone https://github.com/laffreux/ventilator_gui.git
```

## How to install dependencies:
```shell
$ pip install matplotlib
```

## How to execute on windows:

edit the gui.py
and set the window position to 0,0

```python
class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.wm_title("Ventilator")
        if "nt" in os.name:
            #set the window position
            ***x,y = -1400,-650***
        else:
            #sur le pi
            #self.root.attributes('-fullscreen', True)
            x,y = -80,-34
        self.w,self.h = 1280,800
        self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, x, y))
```python		
		
double-click on the gui.bat shortcut
