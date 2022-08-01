from tkinter import *
import pickle


def jobChat():
    print("""
    JOB CHAT:
    ---------

    Joe[Boss]: We need to publish the software by friday

    Tommy[SE]: This is not possible :|

    Frank[CE]: I agree...

    Elisha[SE]: Yea...

    Noam[SE]: Not possible there are still bugs that we need to fix and the Error Handling


    """)


def createTask():
    a = input("enter a task: ")

    with open('filename.pickle', 'wb') as handle:
        pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)


def cloudFiles():
    print("""
    CLOUD_FILES:
    ------------
    todo.txt
    cloud.ini
    main.c
    errH.c
    backendTools.py
    serverSideScript.lua
    """)


def staff():
    print("""
    staff:
    ------
    [SE] Noam
    [SE] Elisha
    [SE] Tommy
    [CE] Frank
    [BOSS] Joe
    """)


def login():
    name = entry2.get()
    label1.config(text=f"Hello {name} welcome to LatteBoard™\n")
    entry1.delete(0, 100)
    entry2.delete(0, 100)


def settings():
    print("""
    ☕ LatteBoard™

    Created by Noam Nahum

    [resolution]:400x590 | 590p

    [GUIv2.3]

    """)


def newClass():
    a = input("Name of the Class: ")
    print(f"class name: {a}")


def tasks():
    with open('filename.pickle', 'rb') as handle:
        b = pickle.load(handle)

    print(f"{b}")


# Software (GUI)

# frame -> frames

tk = Tk()

tk.geometry("780x590")

tk.title("LatteBoard")

tk.config(bg="#303752")

label1 = Label(tk, text="Hello USER welcome to LatteBord™\n",
               font=("Arial", 13, "bold"), bg="#303752", fg="#BDC7EF")
label1.pack()

button1 = Button(tk, text="Tasks", command=tasks, width="30",
                 height="5", font=("Arial", 13, "bold"), bg="#4C5C9A")
button1.pack()

button2 = Button(tk, text="Job Chat", command=jobChat, width="30",
                 height="5", font=("Arial", 13, "bold"), bg="#4C5C9A")
button2.pack()

button3 = Button(tk, text="Cloud Files", command=cloudFiles,
                 width="30", height="5", font=("Arial", 13, "bold"), bg="#4C5C9A")
button3.pack()

button4 = Button(tk, text="Members", command=staff, width="30",
                 height="5", font=("Arial", 13, "bold"), bg="#4C5C9A")
button4.pack()

entry2 = Entry(
    tk,
    font=("Arial", 13),
    bg="#303752",
    fg="#A5ADCE"
)
entry2.pack()

entry1 = Entry(
    tk,
    font=("Arial", 13),
    bg="#303752",
    fg="#A5ADCE",
    show="*"
)
entry1.pack()

button5 = Button(tk, text="Login", command=login, bg="#4C5C9A")
button5.pack()

label2 = Label(tk, text="\nLatteBoard™ LLC.", bg="#303752")
label2.pack()

button6 = Button(tk, text="settings", command=settings, bg="#4C5C9A")
button6.place(x=0, y=0)

button7 = Button(tk, text="create new class", command=newClass, bg="#4C5C9A")
button7.place(x=0, y=30)

button8 = Button(tk, text="create task", command=createTask, bg="#4C5C9A")
button8.place(x=0, y=60)

# MainLoop (runs the software repeatedly)

tk.mainloop()
