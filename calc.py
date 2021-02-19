from tkinter import *

root = Tk()
root.title("Tip Calculator")

total_cost= StringVar()

""" why does function have to be on the top? """
def tipcalc():
    mealcost = float(entry_1.get())
    tip= mealcost * (int(entry_2.get())/100)
    total_amt= mealcost + tip

    total_cost.set(total_amt)

label_1=Label(root, text="Total Meal Cost")
label_1.grid(row=0, sticky=E)

entry_1 = Entry(root)
entry_1.grid(row=0, column=1)


label_2=Label(root, text="Tip %")
label_2.grid(row=1, sticky=E)


entry_2 = Entry(root)
entry_2.grid(row=1, column=1)


button_1= Button(root, text = "calculate", command = tipcalc)
button_1.grid(row=3, column=1)


label_3 = Label(root, text="Your Grand total is $:")
label_3.grid(row=4, column=1)

label_4 = Label(root, textvariable= total_cost)
label_4.grid(row=4, column=2)




root.mainloop()

