import tkMessageBox
from Tkinter import *
import csv

def show_entry_fields():
	with open('sipdevices.csv', 'rt') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
		  	for field in row:
		   		if field == e:
		   		    print "yes"
		   		#else:
		   		#	print "no"
	#print("SIP device: %s" %(e.get()))

master = Tk()
Label(master, text="SIP device").grid(row=0)

e = Entry(master)

e.grid(row=0, column=1)

Button(master, text='Show', command=show_entry_fields).grid(row=3, column=0, sticky=W, pady=4)

mainloop()
