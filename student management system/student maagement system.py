#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


# In[2]:


root = tk.Tk()
root.title("Management")


# In[3]:


connection = sqlite3.connect('management.db')


# In[4]:


TABLE_NAME = "management_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"


# In[5]:


connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " +
                   STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER);")


# In[6]:


appLabel = tk.Label(root, text="Student Management System", fg="#06a099", width=35)
appLabel.config(font=("Sylfaen", 30))
appLabel.grid(row=0, columnspan=2, padx=(10,10), pady=(30, 0))


# In[7]:


class Student:
    studentName = ""
    collegeName = ""
    phoneNumber = 0
    address = ""


# In[8]:


def __init__(self, studentName, collegeName, phoneNumber, address):
        self.studentName = studentName
        self.collegeName = collegeName
        self.phoneNumber = phoneNumber
        self.address = address


# In[9]:


nameLabel = tk.Label(root, text="Enter your name", width=40, anchor='w',
                     font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0),
                                                pady=(30, 0))
collegeLabel = tk.Label(root, text="Enter your college", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))
phoneLabel = tk.Label(root, text="Enter your phone number", width=40, anchor='w',
                      font=("Sylfaen", 12)).grid(row=3, column=0, padx=(10,0))
addressLabel = tk.Label(root, text="Enter your address", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=4, column=0, padx=(10,0))


# In[10]:


nameEntry = tk.Entry(root, width = 30)
collegeEntry = tk.Entry(root, width = 30)
phoneEntry = tk.Entry(root, width = 30)
addressEntry = tk.Entry(root, width = 30)


# In[11]:


nameEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
collegeEntry.grid(row=2, column=1, padx=(0,10), pady = 20)
phoneEntry.grid(row=3, column=1, padx=(0,10), pady = 20)
addressEntry.grid(row=4, column=1, padx=(0,10), pady = 20)


# In[12]:


def takeNameInput():
    global nameEntry, collegeEntry, phoneEntry, addressEntry
    # global username, collegeName, phone, address
    global list
    global TABLE_NAME, STUDENT_NAME, STUDENT_COLLEGE, STUDENT_ADDRESS, STUDENT_PHONE
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)
    collegeName = collegeEntry.get()
    collegeEntry.delete(0, tk.END)
    phone = int(phoneEntry.get())
    phoneEntry.delete(0, tk.END)
    address = addressEntry.get()
    addressEntry.delete(0, tk.END)

    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                       STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " +
                       STUDENT_PHONE + " ) VALUES ( '"
                       + username + "', '" + collegeName + "', '" +
                       address + "', " + str(phone) + " ); ")
    connection.commit()
    messagebox.showinfo("Success", "Data Saved Successfully.")


# In[13]:


def destroyRootWindow():
    root.destroy()
    secondWindow = tk.Tk()

    secondWindow.title("Display results")

    appLabel = tk.Label(secondWindow, text="Student Management System",
                        fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four")

    tree.heading("one", text="Student Name")
    tree.heading("two", text="College Name")
    tree.heading("three", text="Address")
    tree.heading("four", text="Phone Number")
    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i = 0
    for row in cursor:
        tree.insert('', i, text="Student " + str(row[0]),
                    values=(row[1], row[2],row[3], row[4]))
        i = i + 1
    tree.pack()
    secondWindow.mainloop()  


# In[14]:


button = tk.Button(root, text="Take input", command=lambda :takeNameInput())
button.grid(row=5, column=0, pady=30)

displayButton = tk.Button(root, text="Display result", command=lambda :destroyRootWindow())
displayButton.grid(row=5, column=1)

root.mainloop()


# In[ ]:




