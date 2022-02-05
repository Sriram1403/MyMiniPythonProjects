from cgitb import text
from tkinter import *

# assign tkinter to root
root = Tk()
# set value of the frame
root.geometry("500x200")


def getvals():
    print("Accepted")

# Heading
Label(root, text="Registration Form", font="arial 15 bold").grid(row=0, column=3)

# Field Name
name = Label(root, text="Name")
Gender = Label(root, text="Gender")
Year = Label(root, text="Year")
phone = Label(root, text="Phone")
Area_Interest = Label(root, text="Area Of Interest")

# Packing Fields
name.grid(row=1, column=2)
Gender.grid(row=2, column=2)
Year.grid(row=3, column=2)
phone.grid(row=4, column=2)
Area_Interest.grid(row=5, column=2)

#Variable For Storing Data
nameValue = StringVar
GenderValue = StringVar
YearValue = StringVar
phoneValue = StringVar
Area_InterestValue = StringVar
checkValue = IntVar

# Creating Entry Field
nameentry = Entry(root, textvariable=nameValue)
Genderentry = Entry(root, textvariable=GenderValue)
Yearentry = Entry(root, textvariable=YearValue)
phoneentry = Entry(root, textvariable=phoneValue)
Area_Interestentry = Entry(root, textvariable=Area_InterestValue)

# Packing Our Entry Field 
nameentry.grid(row=1, column=3)
Genderentry.grid(row=2, column=3)
Yearentry.grid(row=3, column=3)
phoneentry.grid(row=4, column=3)
Area_Interestentry.grid(row=5, column=3)

# Creating Checkbox

Checkbt = Checkbutton(text="Remember me", variable = checkValue)
Checkbt.grid(row=6, column=3)

# Submit Button
Button(text="Submit", command=getvals).grid(row=7, column=3)

root.mainloop()