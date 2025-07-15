from tkinter import *
from tkinter import messagebox
task_file =[]
with open("file.txt","r", encoding="utf-8") as f:
    for i in f.readlines():
        task_file.append(i.strip())
def save_file():
    with open("file.txt","w", encoding="utf-8") as f:
        for i in task_file:
            f.write(i+"\n")


def show_task():
    global task_file
    tk = task.get()
    if tk:
        task_file.append(tk)
        listbox.insert(END,tk)
        task.delete(0,END)
        save_file()
  

def delete_task():
    
    try:
        global task_file
        selected = listbox.curselection()
        listbox.delete(selected[0])
        err_l.config(text="")
        del task_file[selected[0]]
        save_file()
    except:
        err_l.config(text="Sorry! You haven't selected any task")

def mark_task():
    global task_file
    try:
        selected = listbox.curselection()
        cmplted = listbox.get(selected[0])
        if "✔️" not in cmplted:
            listbox.delete(selected[0])
            del task_file[selected[0]]
            new = cmplted+ "✔️"
            listbox.insert(END,cmplted+"✔️" )
            task_file.append(new)
            save_file()
            err_l.config(text="")
    except:
         err_l.config(text="Sorry! You haven't selected any task")
def unmark_task():
    global task_file
    try:
        selected = listbox.curselection()
        index = selected[0]
        task_text = listbox.get(index)
        if "✔️" in task_text: 
            new = task_text.replace("✔️", "").strip()
            listbox.delete(selected[0])
            del task_file[selected[0]]
            listbox.insert(END,new)
            task_file.append(new)
            save_file()
            err_l.config(text="")
    except:
         err_l.config(text="Sorry! You haven't selected any task")

def Clear():
    global task_file
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?")
    if confirm :
        listbox.delete(0, END)
        task_file.clear()
        save_file()

window = Tk()
window.title("To-Do-List")
window.geometry("400x530")
window.config(bg="#AEC6CF")

header = Label(window, text="📝 My To-Do List", font=("Arial", 16, "bold"), fg="#2e2e2e", bg="#f7f7f7")
header.pack(pady=10)

l = Label(window,text = "Add new task: ")
l.pack()
task = Entry(window,width = 30)
task.pack(pady=10)

add = Button(window,text="Add Task",bg="#86addc",fg="black",command=show_task)
add.pack()


listbox = Listbox(window,width=45, height=10, font = ("Helvetica", 12), selectbackground="#d3d3d3")
for i in task_file: 
    listbox.insert(END,i)
listbox.pack(pady=10)

err_l = Label(window,bg="#AEC6CF")
err_l.pack()
delete = Button(window,text="🗑️Delete",bg="#ffabab",fg="black",command=delete_task)
delete.pack(pady=10)

mark = Button(window,text="\u2705"+" Mark",bg="#8ac3a6",fg="black",command=mark_task)
mark.place(x=130,y=420)

unmark = Button(window,text="\u2705"+" Un-Mark",bg="#8ac3a6",fg="black",command=unmark_task)
unmark.place(x=190,y=420)

clear = Button(window,text="Clear",bg="grey",fg="white",command=Clear)
clear.pack(pady=35)
window.mainloop()
