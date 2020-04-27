"""
Made by William Clavier
Clicker Game!!!
"""
from tkinter import *
import tkinter.messagebox
import pickle
import sys

AC = 0
CA = 1
Points = 0

pickle_in = open("score.pickle", "rb")
example = pickle.load(pickle_in)

print(str(example[1]) + " Auto Clickers")
print(str(example[2]) + " Click Amount")
print(str(example[3]) + " Points")

if example[1] > 0:
    AC = example[1]

if example[2] > 1:
    CA = example[2]

if example[3] > 0:
    Points = example[3]

root = Tk()
AutoClickers = Tk()
ScoreWindow = Tk()
Settings = Tk()
Clickers = Tk()
Stats = Tk()

ScoreBoard = Label(ScoreWindow, text=Points, font=("Arial", 30))

click_amount = Label(
    Stats,
    text="Points Per Click: " + str(CA) + "    Auto Clicks Per Second: " + str(AC),
    font=("Arial", 20))
click_amount.pack()

w = 350  # width for the Tk root
h = 400  # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth()  # width of the screen
hs = root.winfo_screenheight()  # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

x1 = (ws/2) - (w/2)
y1 = (hs/2) - (h/2)
y1 -= 70
w1 = 350
h1 = 40
ScoreWindow.geometry('%dx%d+%d+%d' % (w1, h1, x1, y1))

# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

x2 = (ws/2) - (w/2)
y2 = (hs/2) - (h/2)
x2 -= 795
y2 -= 340
w2 = 300
h2 = 800
AutoClickers.geometry('%dx%d+%d+%d' % (w2, h2, x2, y2))

w4 = 350
h4 = 70
x4 = (ws/2) - (w4/2)
y4 = (hs/2) - (h4/2)
x4 -= 0
y4 += 440
Settings.geometry('%dx%d+%d+%d' % (w4, h4, x4, y4))

x5 = (ws/2) - (w/2)
y5 = (hs/2) - (h/2)
x5 += 825
y5 -= 340
w5 = 300
h5 = 800
Clickers.geometry('%dx%d+%d+%d' % (w5, h5, x5, y5))

w6 = 1000
h6 = 40
x6 = (ws/2) - (w6/2)
y6 = (hs/2) - (h6/2)
y6 -= 520
Stats.geometry('%dx%d+%d+%d' % (w6, h6, x6, y6))


def quit_game():
    prompt = tkinter.messagebox.askquestion('Quit?',
                                            '''Are you sure you would like to quit?
                                             All progress will be saved either way.''')

    if prompt == 'yes':
        shutdown()
        sys.exit()


def shutdown():
    data = {1: AC, 2: CA, 3: Points}
    pickle_out = open("score.pickle", "wb")
    pickle.dump(data, pickle_out)
    pickle_out.close()
    print("~~~~~~~~~~~~~~~~~~~~")
    print(str(AC) + " Auto Clickers")
    print(str(CA) + " Click Amount")
    print(str(Points) + " Points")
    Settings.destroy()
    ScoreWindow.destroy()
    AutoClickers.destroy()
    root.destroy()
    Clickers.destroy()
    Stats.destroy()


def restart():
    global Points
    global AC
    global CA
    data = {1: 0, 2: 1, 3: 0}
    pickle_out = open("score.pickle", "wb")
    pickle.dump(data, pickle_out)
    pickle_out.close()
    AC = 0
    CA = 1
    Points = 0
    ScoreBoard.configure(text=str(Points))


def reset():
    question = tkinter.messagebox.askquestion('Restart?',
                                              'Are you sure you would like to Restart? All progress will be LOST.')
    if question == 'yes':
        restart()


def save():
    data = {1: AC, 2: CA, 3: Points}
    pickle_out = open("score.pickle", "wb")
    pickle.dump(data, pickle_out)
    pickle_out.close()
    tkinter.messagebox.showinfo("Saved Successfully", "Your Data Was Saved.")


def auto_clicks():
    global Points
    ScoreWindow.after(1000, auto_clicks)
    Points = Points + AC
    ScoreBoard.configure(text=str(Points))
    AutoClickers.after(0, ac_shop1)
    Clickers.after(0, ca_shop)
    click_amount.config(text="Points Per Click: " + str(CA) + "    Auto Clicks Per Second: " + str(AC))


def left_click():
    global Points
    Points += CA
    ScoreBoard.configure(text=str(Points))
    AutoClickers.after(0, ac_shop1)
    Clickers.after(0, ca_shop)
    click_amount.config(text="Points Per Click: " + str(CA) + "    Auto Clicks Per Second: " + str(AC))


def middle_click():
    global Points
    Points += 1435674
    ScoreBoard.configure(text=str(Points))
    AutoClickers.after(0, ac_shop1)
    Clickers.after(0, ca_shop)
    click_amount.config(text="Points Per Click: " + str(CA) + "    Auto Clicks Per Second: " + str(AC))


def right_click():
    global Points
    Points += CA
    ScoreBoard.configure(text=str(Points))
    AutoClickers.after(0, ac_shop1)
    Clickers.after(0, ca_shop)
    click_amount.config(text="Points Per Click: " + str(CA) + "    Auto Clicks Per Second: " + str(AC))


def ac_shop1():
    global Points
    global Auto1
    if Points >= 1000:
        Auto1.config(bg="Green")
        if Points >= 5000:
            Auto2.config(bg="Green")
            if Points >= 20000:
                Auto3.config(bg="Green")
                if Points >= 300000:
                    Auto4.config(bg="Green")
                    if Points >= 700000:
                        Auto5.config(bg="Green")
                        if Points >= 2000000:
                            Auto6.config(bg="Green")
                            if Points >= 1000000000:
                                Auto7.config(bg="Green")
    elif Points <= 1000000000:
        Auto7.config(bg="Red")
        if Points <= 2000000:
            Auto6.config(bg="Red")
            if Points <= 700000:
                Auto5.config(bg="Red")
                if Points <= 3000000:
                    Auto4.config(bg="Red")
                    if Points <= 20000:
                        Auto3.config(bg="Red")
                        if Points <= 5000:
                            Auto2.config(bg="Red")
                            if Points <= 1000:
                                Auto1.config(bg="Red")


def ca_shop():
    global Points
    if Points >= 50:
        Click1.config(bg="Green")
        if Points >= 500:
            Click2.config(bg="Green")
            if Points >= 1000:
                Click3.config(bg="Green")
                if Points >= 9000:
                    Click4.config(bg="Green")
                    if Points >= 30000:
                        Click5.config(bg="Green")
                        if Points >= 100000:
                            Click6.config(bg="Green")
                            if Points >= 1000000000000:
                                Click7.config(bg="Green")
    elif Points <= 1000000000000:
        Click7.config(bg="Red")
        if Points <= 100000:
            Click6.config(bg="Red")
            if Points <= 30000:
                Click5.config(bg="Red")
                if Points <= 9000:
                    Click4.config(bg="Red")
                    if Points <= 1000:
                        Click3.config(bg="Red")
                        if Points <= 500:
                            Click2.config(bg="Red")
                            if Points <= 50:
                                Click1.config(bg="Red")


def ca1():
    global Points
    global CA
    if Points >= 50:
        CA += 1
        Points -= 50
        ScoreBoard.configure(text=str(Points))


Click1 = Button(Clickers, text="GRANDMA    +1 Points Per Click    Cost=50", command=ca1, bg="red")
Click1.pack(fill=X, side=TOP)
Click1.config(height=7)


def ca2():
    global Points
    global CA
    if Points >= 500:
        CA += 10
        Points -= 500
        ScoreBoard.configure(text=str(Points))


Click2 = Button(Clickers, text="PARENT    +10 Points Per Click    Cost=500", command=ca2, bg="red")
Click2.pack(fill=X, side=TOP)
Click2.config(height=7)


def ca3():
    global Points
    global CA
    if Points >= 1000:
        CA += 75
        Points -= 1000
        ScoreBoard.configure(text=str(Points))


Click3 = Button(Clickers, text="BABY    +75 Points Per Click    Cost=1,000", command=ca3, bg="red")
Click3.pack(fill=X, side=TOP)
Click3.config(height=7)


def ca4():
    global Points
    global CA
    if Points >= 9000:
        CA += 150
        Points -= 9000
        ScoreBoard.configure(text=str(Points))


Click4 = Button(Clickers, text="CHILD    +150 Points Per Click    Cost=9,000", command=ca4, bg="red")
Click4.pack(fill=X, side=TOP)
Click4.config(height=7)


def ca5():
    global Points
    global CA
    if Points >= 30000:
        CA += 500
        Points -= 30000
        ScoreBoard.configure(text=str(Points))


Click5 = Button(Clickers, text="TEEN    +500 Points Per Click    Cost=30,000", command=ca5, bg="red")
Click5.pack(fill=X, side=TOP)
Click5.config(height=7)


def ca6():
    global Points
    global CA
    if Points >= 100000:
        CA += 1000
        Points -= 100000
        ScoreBoard.configure(text=str(Points))


Click6 = Button(Clickers, text="ROBOT    +1,000 Points Per Click    Cost=100,000", command=ca6, bg="red")
Click6.pack(fill=X, side=TOP)
Click6.config(height=7)


def ca7():
    global Points
    global CA
    if Points >= 1000000000000:
        CA += 1000000
        Points -= 1000000000000
        ScoreBoard.configure(text=str(Points))


Click7 = Button(Clickers, text="GOD    +1 Million Points Per Click    Cost=1 Trillion", command=ca7, bg="red")
Click7.pack(fill=X, side=TOP)
Click7.config(height=7)


def ac1():
    global Points
    global AC
    if Points >= 1000:
        AC += 1
        Points -= 1000
        ScoreBoard.configure(text=str(Points))


def ac2():
    global Points
    global AC
    if Points >= 5000:
        AC += 20
        Points -= 5000
        ScoreBoard.configure(text=str(Points))


def ac3():
    global Points
    global AC
    if Points >= 20000:
        AC += 80
        Points -= 20000
        ScoreBoard.configure(text=str(Points))


def ac4():
    global Points
    global AC
    if Points >= 300000:
        AC += 500
        Points -= 300000
        ScoreBoard.configure(text=str(Points))


def ac5():
    global Points
    global AC
    if Points >= 700000:
        AC += 1000
        Points -= 700000
        ScoreBoard.configure(text=str(Points))


def ac6():
    global Points
    global AC
    if Points >= 2000000:
        AC += 10000
        Points -= 2000000
        ScoreBoard.configure(text=str(Points))


def ac7():
    global Points
    global AC
    if Points >= 1000000000:
        AC += 1000000
        Points -= 1000000000
        ScoreBoard.configure(text=str(Points))


Auto1 = Button(AutoClickers, text="NOOB    +1 Clicks Per Second    Cost=1,000", command=ac1, bg="red")
Auto1.pack(fill=X, side=TOP)
Auto1.config(height=7)


Auto2 = Button(AutoClickers, text="SCRUB    +20 Clicks Per Second    Cost=5,000", command=ac2, bg="red")
Auto2.pack(fill=X, side=TOP)
Auto2.config(height=7)


Auto3 = Button(AutoClickers, text="AVERAGE    +80 Clicks Per Second    Cost=20,000", command=ac3, bg="red")
Auto3.pack(fill=X, side=TOP)
Auto3.config(height=7)


Auto4 = Button(AutoClickers, text="YOUTUBER    +500 Clicks Per Second    Cost=300,000", command=ac4, bg="red")
Auto4.pack(fill=X, side=TOP)
Auto4.config(height=7)


Auto5 = Button(AutoClickers, text="NINJA    +1,000 Clicks Per Second    Cost=700,000", command=ac5, bg="red")
Auto5.pack(fill=X, side=TOP)
Auto5.config(height=7)


Auto6 = Button(AutoClickers, text="SAVAGE    +10,000 Clicks Per Second    Cost=2,000,000", command=ac6, bg="red")
Auto6.pack(fill=X, side=TOP)
Auto6.config(height=7)


Auto7 = Button(AutoClickers, text="HACKS    +1 Million Clicks Per Second    Cost=1 Billion", command=ac7, bg="red")
Auto7.pack(fill=X, side=TOP)
Auto7.config(height=7)

mainButton = Button(root, text="Click!!", font=("Arial", 50), fg="Blue")
mainButton.bind("<Button-1>", left_click)
mainButton.bind("<Button-3>", right_click)
mainButton.config(width=50, height=27)
mainButton.pack()
root.title("Main Clicker Window")

ACFrame = Frame(AutoClickers, width=300, height=800)
ACFrame.pack()
AutoClickers.title("AutoClicker Shop")

ScoreBoard.pack()
ScoreWindow.title("Score:")

Settings.title("Made By William C")
Quit = Button(Settings, text="Quit", bg="Red", command=quit_game, font=("Arial", 20))
Quit.bind("<Button-2>", middle_click)
Quit.pack(side=RIGHT)
Quit.config(height=70)
Reset = Button(Settings, text="Restart", bg="Red", command=reset, font=("Arial", 20))
Reset.pack(side=RIGHT)
Reset.config(height=70)
Save1 = Button(Settings, text="Save", bg="Green", command=save, font=("Arial", 20))
Save1.pack(side=RIGHT)
Save1.config(height=70, width=30)

Clickers.title("Click Shop")

auto_clicks()

Stats.title("Stats")

root.mainloop()
