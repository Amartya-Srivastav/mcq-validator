from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import json

y = 0
a = ttk.Notebook()
frame1 = ttk.Frame(a)
frame2 = ttk.Frame(a)
frame3 = ttk.Frame(a)
root = ttk.Frame(a)


def quiz(a):
    a.add(frame1, text="Q1")
    a.add(frame2, text="Q2")
    a.add(frame3, text="Q3")

    Label(frame1, text="Convert the given fraction into mixed fraction 22/7", font=("Arial", 30, "bold")).grid(row=2,
                                                                                                               column=2)
    Button(frame1, text="3*1/7", font=("Arial", 20, "bold"), bg="light pink", command=a1_right).grid(row=3, column=1)
    Button(frame1, text="3*2/7", font=("Arial", 20, "bold"), bg="light pink", command=a1_wrong).grid(row=3, column=2)
    Button(frame1, text="4*1/7", font=("Arial", 20, "bold"), bg="light pink", command=a1_wrong).grid(row=5, column=1)
    Button(frame1, text="4*2/7", font=("Arial", 20, "bold"), bg="light pink", command=a1_wrong).grid(row=5, column=2)

    Label(frame2, text="What is equivalent of 9/15", font=("Arial", 30, "bold")).grid(row=2, column=2)

    Button(frame2, text="18/30", font=("Arial", 20, "bold"), bg="light pink", command=a2_right).grid(row=3, column=1)
    Button(frame2, text="10/20", font=("Arial", 20, "bold"), bg="light pink", command=a2_wrong).grid(row=3, column=2)
    Button(frame2, text="18/20", font=("Arial", 20, "bold"), bg="light pink", command=a2_wrong).grid(row=5, column=1)
    Button(frame2, text="12/20", font=("Arial", 20, "bold"), bg="light pink", command=a2_wrong).grid(row=5, column=2)

    Label(frame3, text="What is the value of (3*4/7)/7", font=("Arial", 30, "bold")).grid(row=2, column=2)

    Button(frame3, text="12/49", font=("Arial", 20, "bold"), bg="light pink", command=a3_wrong).grid(row=3, column=1)
    Button(frame3, text="25/49", font=("Arial", 20, "bold"), bg="light pink", command=a3_right).grid(row=3, column=2)
    Button(frame3, text="3/7", font=("Arial", 20, "bold"), bg="light pink", command=a3_wrong).grid(row=5, column=1)
    Button(frame3, text="21/49", font=("Arial", 20, "bold"), bg="light pink", command=a3_wrong).grid(row=5, column=2)


def a1_right():
    Label(frame1, text=" Correct ", font=("Arial", 30, "bold"), bg="green", fg="white").grid(row=1, column=2)
    Label(frame1, text="Points : 1", font=("Arial", 30, "bold"), bg="Black", fg="light Pink").grid(row=1, column=3)


def a1_wrong():
    Label(frame1, text=" Incorrect ", font=("Arial", 30, "bold"), bg="red", fg="white").grid(row=1, column=2)
    Label(frame1, text="Points : 0", font=("Arial", 30, "bold"), bg="Black", fg="light Pink").grid(row=1, column=3)


def a2_right():
    Label(frame2, text=" Correct ", font=("Arial", 30, "bold"), bg="green", fg="white").grid(row=1, column=2)
    Label(frame2, text="Points : 1", font=("Arial", 30, "bold"), bg="Black", fg="light Pink").grid(row=1, column=3)


def a2_wrong():
    Label(frame2, text=" Incorrect ", font=("Arial", 30, "bold"), bg="red", fg="white").grid(row=1, column=2)
    Label(frame2, text="Points : 0", font=("Arial", 30, "bold"), bg="Black", fg="light Pink").grid(row=1, column=3)


def a3_right():
    Label(frame3, text=" Correct", font=("Arial", 30, "bold"), bg="green", fg="white").grid(row=1, column=2)
    Label(frame3, text="Points : 1", font=("Arial", 30, "bold"), bg="Black", fg="light Pink").grid(row=1, column=3)


def a3_wrong():
    Label(frame3, text=" Incorrect", font=("Arial", 30, "bold"), bg="red", fg="white").grid(row=1, column=2)
    Label(frame3, text="Points : 0", font=("Arial", 30, "bold"), bg="Black", fg="light Pink").grid(row=1, column=3)


quiz(a)
a.pack()
a.mainloop()
