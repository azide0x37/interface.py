import tkMessageBox
from Tkinter import *
import csv
import re
import pandas as pd

with open('sipdevices.csv') as f:
    reader = pd.read_csv(f, delimiter=',')

def show_entry_fields():
    value.get()
    b = reader.loc[reader['SIP System Name'] == value]
    print type(value)
    print b


"""def show_entry_fields():
	with open('sipdevices.csv', 'rb') as f:
		reader = csv.reader(f, delimiter=',')
		result = [row[1].strip()]
		for field in reader: 
		    print field
		   		    #c213wjdzpha00"""

master = Tk()
Label(master, text="SIP device").grid(row=0)

value = StringVar()
e = Entry(master, textvariable=value)

e.grid(row=0, column=1)

Button(master, text='Show', command=show_entry_fields).grid(row=3, column=0, sticky=W, pady=4)

mainloop()
