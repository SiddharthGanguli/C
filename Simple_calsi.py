from tkinter import *
import math

root=Tk()
root.title("Simple Calculator")

root.minsize(390,350)
root.maxsize(390,350)

display=Entry(root,width=40,borderwidth=5)
display.grid(row=0,column=0,columnspan=3)


def button_click(number):
    # it will get input 1st from the buttons then convert into str and then concetinate to each other 
    current=display.get()
    # delete use becuse it will add the first number to last that's why we use this
    display.delete(0,END)
    display.insert(0, str(current)+str(number))
def clear():
    display.delete(0,END)

def add():
    global math
    math='addition'
    first_number=display.get()
    global f_num
    f_num=int(first_number)
    display.delete(0,END)

def Sub():
    global math
    math='Subtraction'
    first_number=display.get()
    global f_num
    f_num=int(first_number)
    display.delete(0,END)

def Mul():
    global math
    math='Multiplication'
    first_number=display.get()
    global f_num
    f_num=int(first_number)
    display.delete(0,END)

def Div():
    global math
    math='Division'
    first_number=display.get()
    global f_num
    f_num=int(first_number)
    display.delete(0,END)
def sin():
    global math
    math='sin'
    first_number=display.get()
    global f_num
    f_num=float(first_number)
    # display.delete(0,END)
    global k
    k=display.insert(0,math.sin(math.radians((f_num))))
    n=str(k)
    
def sqrt():
    global math
    math='sqrt'
    first_number=display.get()
    global f_num
    f_num=int(first_number)
    # display.delete(0,END)
    display.insert(0,math.sqrt(f_num))   
def cos():
    pass
def tan():
    pass
def equel():
    secound_number=display.get()
    display.delete(0,END)
    if(math=='addition'):
        display.insert(0,f_num + int(secound_number))
    elif(math=='Subtraction'):
        display.insert(0,f_num - int(secound_number))
    elif(math=='Division'):
        display.insert(0,f_num / int(secound_number))
    elif(math=='Multiplication'):
        display.insert(0,f_num *int(secound_number))
    elif(math=='sin'):
        sin()
    
    
button_1=Button(root,text='1',padx=40,pady=10,command=lambda:button_click(1))
button_2=Button(root,text='2',padx=40,pady=10,command=lambda:button_click(2))
button_3=Button(root,text='3',padx=40,pady=10,command=lambda:button_click(3))
button_4=Button(root,text='4',padx=40,pady=10,command=lambda:button_click(4))
button_5=Button(root,text='5',padx=40,pady=10,command=lambda:button_click(5))
button_6=Button(root,text='6',padx=40,pady=10,command=lambda:button_click(6))
button_7=Button(root,text='7',padx=40,pady=10,command=lambda:button_click(7))
button_8=Button(root,text='8',padx=40,pady=10,command=lambda:button_click(8))
button_9=Button(root,text='9',padx=40,pady=10,command=lambda:button_click(9))
button_0=Button(root,text='0',padx=40,pady=10,command=lambda:button_click(0))


button_equal=Button(root,text='=',padx=100,pady=10,command=equel,)
button_clear=Button(root,text='clear',padx=30,pady=10,command=clear)

button_add=Button(root,text='+',padx=40,pady=10,command=add)
button_sub=Button(root,text='-',padx=40,pady=10,command=Sub)
button_mul=Button(root,text='x',padx=40,pady=10,command=Mul)
button_div=Button(root,text='÷',padx=40,pady=10,command=Div)
button_sin=Button(root,text='sin',padx=40,pady=10,command=sin)
button_cos=Button(root,text='sqrt',padx=40,pady=10,command=sqrt)
button_tan=Button(root,text='tan',padx=40,pady=10,command=tan)


button_1.grid(row=3, column=2)
button_2.grid(row= 3, column=1)
button_3.grid(row= 3, column=0)
button_4.grid(row= 2, column=2)
button_5.grid(row=2, column=1)
button_6.grid(row= 2, column=0)
button_7.grid(row=1, column=2)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=0)

button_0.grid(row=4, column=0)

button_equal.grid(row=4, column=1,columnspan=2)
button_clear.grid(row=5, column=0)

button_add.grid(row=5,column=1)
button_sub.grid(row=5,column=2)
button_mul.grid(row=6,column=0)
button_div.grid(row=6,column=1)

button_sin.grid(row=7,column=0)
button_cos.grid(row=7,column=1)
button_tan.grid(row=7,column=2)


root.mainloop()