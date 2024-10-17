# A graphical clock in Python using tkinter and math modules

import tkinter as tk
import time
import math
from tkinter import Canvas

# Create a window
window=tk.Tk()
window.title("Bibekster Clock")
window.geometry("400x400")
window.configure(bg='black')

# Creating a Canvas instance
canvas=Canvas(window, width=400,height=400)
canvas.pack()

# Drawing the clock face
def draw_clock_face():
    canvas.create_oval(50,505,350,350, width=4)  # Outer circle
    for i in range(12):
        angle=math.radians(i*30) # 30 degrees for each hour mark
        x=200+120*math.sin(angle)
        y=200-120*math.cos(angle)
        canvas.create_text(x,y, text=str(i+1), font=("calibri",14,'bold'))

# Drawing the hands of the clock
def draw_hand(length, angle, width, color):
    angle=math.radians(angle)
    x=200+length*math.sin(angle)
    y=200-length*math.cos(angle)
    return canvas.create_line(200,200,x,y, width=width, fill=color, tags="hands")   # This is necessary to remove previous hands

# Update the clock hands
def update_clock():
    canvas.delete("hands")     # Remove previous hands

    # Get the current time
    current_time=time.localtime()
    hours= current_time.tm_hour % 12
    minutes= current_time.tm_min
    seconds=current_time.tm_sec

    # Calculate the angles for the hands
    second_angle=seconds*6 # 360 degrees/ 60 seconds
    minute_angle=minutes*6 # 360 degrees / 60 minutes
    hour_angle = (hours+minutes/60)*30  # 360 degrees/12 hours

    # Drawing the hands with the calculated angles
    draw_hand(100, second_angle, 2, 'red')  # Second hand
    draw_hand(80, minute_angle,4,'blue')  # Minute hand
    draw_hand(60,hour_angle, 6,'black')   # Hour Hand

    canvas.create_oval(195,195,205,205, fill='black')   # drawing clock center point

    # making the function to run again after 1000ms i.e. 1 second
    window.after(1000, update_clock)

# Drawing the clock face and updating the time
draw_clock_face()
update_clock()

# Run the application
window.mainloop()

    