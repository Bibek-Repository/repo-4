Modules used in this project are:
tkinter : A python library for creating Graphical User Interface(GUI)
time : It helps to get the current time
math : It helps to do mathematical operations. In the code sin and cos method are used

Create the window:
It creates a window for the clock using tkinter with the title "Bibekster Clock". The size can be specified to be 400*400 and a black background.

Creating a canvas:
Canvas is used to draw shapes and text. The hands and face of clock are drawn using the Canvas

Drawing the Clock Face:
create_oval(50,50,350,350, width=4): This will draw the boarder for the clock face. The arguments define the bounding box for the boarder(top-left and bottom-right corners)
Hour marks: using the for loop in the range(0,12). It will keep the hour on the clock. Each hour is seperated by 30 degrees (360 deg/ 12 hours)
x and y calculate the position for each hour using sin and cos functions
120 is the radius for the center of the circle to where the numbers will be placed.
200 is the center of the canvas(half of 400width/height)

Drawing the Hands:

It draws the line from center(200,200) to the point x and y using sin and cos functions of math module
Parameters:
length: how far it reaches from the center
angle: Angle in degrees to rotate the hand
width: thickness of the hand
color: Color of the hand(in the code: red is for seconds and so on)
math.radians(angle): Converts degrees to radians because sin and cos work with radians
End point (x,y) is calculated using the trigonometric functions to find the correct position for each angle.

Updating the Clock Hands:

canvas.delete("hands"): It clears the previously drawn hands using the tags so that the previous hands are completely removed
time.localtime(): It gives the current time, Hours, minutes and seconds are taken
Calculated angles:
seconds*6: Each second equals to 6 degrees(360 deg/60 seconds)
minutes*6: Each minute equals to 6 degrees (360 deg/60 minutes)
(hours+minutes/60)*30: Each hour equals to 30 degrees(360 deg/12 hours), with a fractional adjustment for minutes
draw_hand() this draws the hour, minute and second hand with different lengths, widths, and colors
windows.after(1000, update_clock): Schedules the update_clock function to be called again after 1000 milliseconds(1 Second) for continuous updating.

Run the Application:
draw_clock_face(): It draws the clock face and hour numbers.
update_clock(): Starts the clock's hands by calling it.
window.mainloop(): It keeps the window open and allows the program to interact with user inputs, updates, and GUI events

The code from the file clock.py will create a window that displays an analog clock bibekster clock. The hands are moving based on the current time. The draw_hand() function handles the drawing of the hands, while update_clock() updates their positions every second. The clock face remains static, while the hands are dynamic.

