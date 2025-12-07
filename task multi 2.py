from tkinter import *
from tkinter import ttk
root =Tk()
root.geometry("470x340")
##title
root.title("Student Information")
title=Label(root,text="Student Information", font="Claibre 15 bold")
title.grid(column=0, row=0,pady=5,columnspan=4)

##first and last name
fname=Label(root, text="First Name :",font="Claibre 10")
fname.grid(column=0 , row=1,padx=10,sticky="w")
fname=Entry(root, width=20)
fname.grid(column=1, row=1)
lname=Label(root, text="  Last Name :",font="Claibre 10")
lname.grid(column=2, row=1, padx=10)
lname=Entry(root, width=20)
lname.grid(column=3, row=1, pady=5)

##birth

birth=Label(root, text="Birth Date :", font="Claibre 10")
birth.grid(column=0 , row=2,padx=10,sticky="w")
birth=Entry(root, width=20)
birth.grid(column=1, row=2,columnspan=3,sticky="we")

##gender
Gender=Label(root, text="Gender", font="Claibre 10")
Gender.grid(column=0 , row=3, padx=10, sticky="w")
gender=StringVar()
gender.set("none")
male = Radiobutton(root, text="Male", variable=gender,value= "Male",font="Claibre 10")
male.grid(column=1, row=3, pady=5, sticky="w")
female = Radiobutton(root, text="Female" , variable=gender,value="Female",font="Claibre 10")
female.grid(column=2, row=3, pady=5, sticky="w")

##country

country=Label(root, text="Country", font="Claibre 10")
country.grid(column=0 , row=4, padx=10, sticky="w")
countryC=ttk.Combobox(root, width=20, values=["Egypt","Morocco","syria","Tunisia","Saudia Arabia"])
countryC.grid(column=1 , row=4, pady=5, columnspan=3, sticky="we")

##address

address=Label(root, text="Address :", font="Claibre 10")
address.grid(column=0 , row=5, padx=10, sticky="nw")
address=Text(root, width=20, height=5)
address.grid(column=1, row=5, pady=5, columnspan=3,sticky="we")

## empty label to show messages
msg = Label(root, text="", font="Claibre 10 bold", fg="green")
msg.grid(column=0, row=6, columnspan=4, pady=5)


##fun
def save_but():
   msg.config(text="✔️ Student data has been saved", fg="green")
def cancel_but():
   msg.config(text="❌ Student data has been canceled", fg="red")    
##button 
save =Button(root, text="Save", fg="black", bg="orange", command=save_but, font="Claibre 10 bold")
save.grid(column=1, row=7, padx=10, sticky="e", ipadx=10)

cancel =Button(root, text="Cancel", fg="black", bg="orange", command=cancel_but, font="Claibre 10 bold")
cancel.grid(column=2, row=7, padx=10, sticky="w", ipadx=10)

root.mainloop()