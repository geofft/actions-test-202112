import sys
print(sys.executable)
print(sys.path)
import subprocess
from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
root.after(5000, root.destroy)
root.after_idle(subprocess.check_call, ["screencapture", "screenshot.png"])
root.focus_force()
root.mainloop()
