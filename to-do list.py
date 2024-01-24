import tkinter 
import tkinter.messagebox
import pickle
from tkinter import *

root = tkinter.Tk()
root.title("Task 1 :- TO-DO list")     

root.geometry("500x350")

def change_color():
   root.configure(bg='grey')


def add_task():
    task = entry_task.get()
    if task !="":
        listbox_task.insert(tkinter.END, task)
        entry_task.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Error!", message="task shouldn't be empty.")

def delete_task():
    try:
        task_index = listbox_task.curselection()[0]
        listbox_task.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Error!" , message="you must select a task.")

def load_task():
    try:
        tasks = pickle.load(open("task.txt",'rb'))
        listbox_task.delete(0,tkinter.END)
        for task in tasks:
            listbox_task.insert(tkinter.END,task)
    except:
        tkinter.messagebox.showwarning(title="Error!" ,message="Cannot find the file task.txt")

def save_task():
    tasks = listbox_task.get(0,listbox_task.size())
    pickle.dump(tasks,open('task.txt','wb'))            #write binary

def clear_task():
    listbox_task.delete(0, tkinter.END)


# GUI
frame_task = tkinter.Frame(root)
frame_task.pack()

listbox_task = tkinter.Listbox(frame_task,height=10,width=50)
listbox_task.pack(side=tkinter.LEFT)

scroll_bar = tkinter.Scrollbar(frame_task)
scroll_bar.pack(side=tkinter.RIGHT,fill=tkinter.Y)

listbox_task.config(yscrollcommand= scroll_bar.set)
scroll_bar.config(command=listbox_task.yview)


entry_task = tkinter.Entry(root,width=50)
entry_task.pack()

button_add = tkinter.Button(root,text="Add task",bg='skyblue', width=48,command=add_task)
button_add.pack()

button_Delete = tkinter.Button(root,text="Delete task",bg='red', width=48,command=delete_task)
button_Delete.pack()

button_load = tkinter.Button(root,text="Load task",bg="skyblue", width=48,command=load_task)
button_load.pack()

button_save = tkinter.Button(root,text="Save task", bg='skyblue', width=48,command=save_task)
button_save.pack()

button_save = tkinter.Button(root,text="Clear", bg='skyblue', width=48, command=clear_task)
button_save.pack()


button=Button(root, text= "Change Color",  command=change_color)
button.pack()



root.mainloop()