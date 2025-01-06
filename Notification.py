from tkinter import *
import time
from pygame import mixer

Continue = True
timer = 3
time.sleep(timer)

root = Tk()
root.title("!!Notification!!")

def Extend():
    timer = 60
    time.sleep(timer)
def STOP():
    mixer.music.stop()

mixer.init()
mixer.music.load("Sound Effects/Alarm sound effect.mp3")  # Relative path
mixer.music.play(-1)

Notif = Label(root, text="Remember your Schedule!")
Notif.grid(row=0, column=0, columnspan=2)
Stop = Button(root, width=20, text="Stop Alarm", borderwidth=4, command=STOP)
Stop.grid(row=1, column=0)
Snooze = Button(root, width=20, text="Snooze", borderwidth=4, command=Extend)
Snooze.grid(row=1, column=1)

# e = Entry(root, width=44, borderwidth=5)
# e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# numbers = []
# operation = ""
# result = 0

# def button_click(num):
#     current_num = e.get()
#     e.delete(0, END)
#     e.insert(0, str(current_num) + str(num))
#     return

# def button_clear():
#     e.delete(0, END)

# def button_add():
#     num1 = e.get()
#     numbers.append(int(num1))
#     e.delete(0, END)
#     operation = 1
    
# def button_sub(num):
#     operation = num
#     num1 = e.get()

# def button_equals():
#     global result
#     global numbers
#     result = e.get()
#     for i in numbers:
#         result = result =+ i
#     e.delete(0, END)
#     e.insert(0, result)
#     numbers = []
#     result = 0

# # Define Buttons
# button_1 = Button(root,text=1, padx=40, pady=20, command=lambda: button_click(1))
# button_2 = Button(root,text=2, padx=40, pady=20, command=lambda: button_click(2))
# button_3 = Button(root,text=3, padx=40, pady=20, command=lambda: button_click(3))
# button_4 = Button(root,text=4, padx=40, pady=20, command=lambda: button_click(4))
# button_5 = Button(root,text=5, padx=40, pady=20, command=lambda: button_click(5))
# button_6 = Button(root,text=6, padx=40, pady=20, command=lambda: button_click(6))
# button_7 = Button(root,text=7, padx=40, pady=20, command=lambda: button_click(7))
# button_8 = Button(root,text=8, padx=40, pady=20, command=lambda: button_click(8))
# button_9 = Button(root,text=9, padx=40, pady=20, command=lambda: button_click(9))
# button_0 = Button(root,text=0, padx=40, pady=20, command=lambda: button_click(0))
# button_add = Button(root,text="+", padx=39, pady=20, command=button_add)
# button_sub = Button(root,text="-", padx=39, pady=20, command=lambda: button_sub("sub"))
# button_eq = Button(root,text="=", padx=88, pady=20, command=button_equals)
# button_clear = Button(root,text="clear", padx=29, pady=20, command=button_clear)
# #Put buttons on screen
# button_1.grid(row=3, column=0)
# button_2.grid(row=3, column=1)
# button_3.grid(row=3, column=2)
# button_4.grid(row=2, column=0)
# button_5.grid(row=2, column=1)
# button_6.grid(row=2, column=2)
# button_7.grid(row=1, column=0)
# button_8.grid(row=1, column=1)
# button_9.grid(row=1, column=2)
# button_0.grid(row=4, column=0)

# button_add.grid(row=4, column=1)
# button_sub.grid(row=4, column=2)
# button_eq.grid(row=5, column=0, columnspan=2)
# button_clear.grid(row=5, column=2)

root.mainloop()