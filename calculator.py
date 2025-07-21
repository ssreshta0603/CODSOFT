from tkinter import *
import numpy as np
def button_click(value):
    rn = entry.get()
    entry.delete(0, END)
    x=['+','/','*','-']
    
    if value in x: 
        entry.insert(0, rn +" "+value+" ")
    else:
        entry.insert(0,rn+value)

def clear():
    entry.delete(0,END)

def backspace():
    ip = len(entry.get())
    entry.delete(ip-1,END)


def calculate():
    x=['+','/','*','-']
    ip = entry.get()
    entry.delete(0, END)
    nums = ip.strip().split(" ")
    print(nums)
    try :
        if "/" in nums:
            i = nums.index("/")
            n1 = nums[i-1]
            n2 = nums[i+1]
            nums.remove("/")
            nums.remove(n1)
            nums.remove(n2)
            v1 = float(n1)/float(n2)
            nums.insert(i,v1)

        if  "*" in nums:
            i = nums.index("*")
            n1 = nums[i-1]
            n2 = nums[i+1]
            nums.remove("*")
            nums.remove(n1)
            nums.remove(n2)
            v1 = float(n1)*float(n2)
            nums.insert(i,v1)

        if  "+" in nums:
            i = nums.index("+")
            n1 = nums[i-1]
            n2 = nums[i+1]
            nums.remove("+")
            nums.remove(n1)
            nums.remove(n2)
            v1 = float(n1)+float(n2)
            nums.insert(i,v1)

        if  "-" in nums:
            i = nums.index("-")
            n1 = nums[i-1]
            n2 = nums[i+1]
            nums.remove("-")
            nums.remove(n1)
            nums.remove(n2)
            v1 = float(n1)-float(n2)
            nums.insert(i,v1)

        entry.insert(0,nums)
    except:
        entry.delete(0,END)
        entry.insert(0,"ERROR")
window = Tk()
window.title("Calculator")
window.geometry("350x500")
window.config(bg="#242526")

entry = Entry(window,bg="#242526",fg="white", font=("Arial", 20), justify="right")
entry.pack(fill="both", padx=10, pady=20)

f = Frame(window, bg="#242526", bd=2)
f.pack()
f.pack_propagate(False)

f2 = Frame(window, bg="#242526", bd=2)
f2.pack()
f2.pack_propagate(False)

button = np.array([
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','bs','+'],
])

for i in range(4):
    for j in range(4):
        if button[i][j] == "bs":
            Button(f,text="\u232B",bg="#3A3B3C",fg="white",width=6,height=4,command=backspace).grid(row=i,column=j,padx=3,pady=3)
        else:
            Button(f,text=button[i][j],bg="#3A3B3C",fg="white",width=6,height=4,command=lambda val =button[i][j]: button_click(val)).grid(row=i,column=j,padx=3,pady=3)
output = Button(f2,text="=",bg="violet",width=25,height=3,command=calculate).grid(row=0, column=0,sticky="e")
bs = Button(f2,text="C",bg="#3A3B3C",fg="white",width=6,height=3,command=clear).grid(row=0, column=1)

window.mainloop()