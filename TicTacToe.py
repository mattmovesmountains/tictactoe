#========================================================
# Practice script to switch back and forth between 
# different images on a button.
#========================================================

from tkinter import *

root = Tk()
root.title("Tic Tac Toe")

q_for_button = PhotoImage(file="/home/pi/Pictures/questionmark.png")
x_for_button = PhotoImage(file="/home/pi/Pictures/red-X.png")
o_for_button = PhotoImage(file="/home/pi/Pictures/green-O.png")

def switch_image(whichbutton, number):
    # When 2 is passed into button, change to an O
    # and change the pass-through number to 1
    if number==2:
        whichbutton.config(image=o_for_button, command=lambda:switch_image(whichbutton, 1))
    # When 1 is passed into button, change to an X
    # and change the pass-through number to 2
    if number==1:
        whichbutton.config(image=x_for_button, command=lambda:switch_image(whichbutton, 2))

def reset():
    buttonlist = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]

    for item in buttonlist:
        item.config(image=q_for_button)

def oneORtwo():
    pass


# Instantiate the button and default "2" to change from X to O
btn1 = Button(root, image=q_for_button, height=200, width=200, command=lambda:switch_image(btn1, 2))
btn1.grid(row=0,column=0)

btn2 = Button(root, image=q_for_button, height=200, width=200, command=lambda:switch_image(btn2, 2))
btn2.grid(row=0,column=1)

btn3 = Button(root, image=q_for_button, height=200, width=200, command=lambda:switch_image(btn3, 2))
btn3.grid(row=0,column=2)
#--------------------------------------------------------------------------------------------
btn4 = Button(root, image=q_for_button, height=200, width=200, command=lambda:switch_image(btn4, 2))
btn4.grid(row=1,column=0)

btn5= Button(root, image=q_for_button, height=200, width=200, command=lambda:switch_image(btn5, 2))
btn5.grid(row=1,column=1)

btn6 = Button(root, image=q_for_button, height=200, width=200, command=lambda:switch_image(btn6, 2))
btn6.grid(row=1,column=2)
#---------------------------------------------------------------------------------------------
btn7 = Button(root, image=q_for_button, height=200, width=200, command=lambda:switch_image(btn7, 2))
btn7.grid(row=2,column=0)

btn8= Button(root, image=q_for_button, height=200, width=200, command=lambda:switch_image(btn8, 2))
btn8.grid(row=2,column=1)

btn9 = Button(root, image=q_for_button, height=200, width=200, command=lambda:switch_image(btn9, 2))
btn9.grid(row=2,column=2)

reset_button = Button(root, text="Reset", command=reset)
reset_button.grid(row=3,columnspan=3)

mainloop()