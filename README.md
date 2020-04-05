# ventilator_gui

## How to install:

```shell
$ git clone https://github.com/laffreux/ventilator_gui.git
```

## How to install dependencies:
```shell
$ pip install matplotlib
$ pip install tkinter
on Linux use
sudo apt-get install python-tk

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
            x,y = -1400,-650
```
		
double-click on the gui.bat shortcut
