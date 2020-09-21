import time
import tkinter as tk
import pyautogui

def Screenshot():
    num=int(round(time.time()*1000))
    image_name=f"D:/COURSES/Programming/Python tutorials/Screenshots_data/{num}.png"
    Image=pyautogui.screenshot(image_name)
    Image.show()
root=tk.Tk()
frame=tk.Frame(root)
frame.pack()
button=tk.Button(
    frame,
    text="Take screenshot",
    command=Screenshot
)
button.pack(side=tk.LEFT)
close=tk.Button(
    frame,
    text='Close',
    command=quit
)
close.pack(side=tk.LEFT)
root.mainloop()
