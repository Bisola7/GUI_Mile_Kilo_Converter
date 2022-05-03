from tkinter import *
window = Tk()
window.title("Miles to Kilometre Converter")
window.minsize(width=600, height=400)
window.config(padx=20, pady=20)


def converter():
    miles = float(e.get())
    kilometre = miles * 1.689
    l3.config(text=f"{kilometre}")


e = Entry(width=8)
e.grid(column=1, row=0)

l1 = Label(text="Miles", font=("Arial", 10, "bold"))
l1.grid(column=2, row=0)

l2 = Label(text="is equal to", font=("Arial", 10, "bold"))
l2.grid(column=0, row=1)

l3 = Label(text="0", font=("Arial", 10, "bold"))
l3.grid(column=1, row=1)

l4 = Label(text="Km", font=("Arial", 10, "bold"))
l4.grid(column=2, row=1)

b = Button(text="Convert", command=converter)
b.grid(column=1, row=2)

window.mainloop()
