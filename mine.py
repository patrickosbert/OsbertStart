from tkinter import *
from matplotlib import pyplot as plt
from pylab import plot,show,xlabel, ylabel
x=0
window =Tk()
window.geometry("300x300")
window.title("bar graph")

firstVar =StringVar()
secondVar=StringVar()
thirdVar=StringVar()
fourVar=StringVar()
fiveVar=StringVar()
sixVar=StringVar()

firstInput =Entry(window,textvariable=firstVar)
firstInput.grid(row=0,column=0,padx=5,pady=5,ipady=5)
firstBtn = Button(window,text="Thiba",command=lambda:LoadFirstGraph())
firstBtn.grid(row=0,column=1,pady=5,padx=5)

secondInput =Entry(window,textvariable=secondVar)
secondInput.grid(row=2,column=0,padx=5,pady=5,ipady=5)
secondBtn = Button(window,text="Karaba",command=lambda:LoadSecondGraph())
secondBtn.grid(row=2,column=1,pady=5,padx=5)

thirdInput =Entry(window,textvariable=thirdVar)
thirdInput.grid(row=3,column=0,padx=5,pady=5,ipady=5)
thirdBtn = Button(window,text="Wamumu",command=lambda:LoadThirdGraph())
thirdBtn.grid(row=3,column=1,pady=5,padx=5)

fourInput =Entry(window,textvariable=fourVar)
fourInput.grid(row=4,column=0,padx=5,pady=5,ipady=5)
fourBtn = Button(window,text="Nderwa",command=lambda:LoadFourGraph())
fourBtn.grid(row=4,column=1,pady=5,padx=5)

fiveInput =Entry(window,textvariable=fiveVar)
fiveInput.grid(row=5,column=0,padx=5,pady=5,ipady=5)
fiveBtn = Button(window,text="T3-T9",command=lambda:LoadFiveGraph())
fiveBtn.grid(row=5,column=1,pady=5,padx=5)

sixInput =Entry(window,textvariable=sixVar)
sixInput.grid(row=6,column=0,padx=5,pady=5,ipady=5)
sixBtn = Button(window,text="W3-W5",command=lambda:LoadSixGraph())
sixBtn.grid(row=6,column=1,pady=5,padx=5)

def LoadFirstGraph():
    global firstVar
    global x
    y=float(firstVar.get())
    x+=1
    plt.bar(x,y,label="Thiba",color="red")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.legend()
    plt.show()

def LoadSecondGraph():
    global secondVar
    global x
    y=float(firstVar.get())
    x+=1
    plt.bar(x,y,label="Karaba",color="green")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.legend()
    plt.show()

def LoadThirdGraph():
    global thirdVar
    global x
    y=float(thirdVar.get())
    x+=1
    plt.bar(x,y,label="Wamumu",color="blue")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.legend()
    plt.show()

def LoadFourGraph():
    global fourVar
    global x
    y=float(fourVar.get())
    x+=1
    plt.bar(x,y,label="Nderwa",color="black")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.legend()
    plt.show()

def LoadFiveGraph():
    global fiveVar
    global x
    y=float(fiveVar.get())
    x+=1
    plt.bar(x,y,label="T3-T9",color="yellow")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.legend()
    plt.show()

def LoadSixGraph():
    global sixVar
    global x
    y=float(sixVar.get())
    x+=1
    plt.bar(x,y,label="W3-W5",color="brown")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.legend()
    plt.show()

window.mainloop()