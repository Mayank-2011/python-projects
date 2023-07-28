FONT = font=("Arial", 14)
from tkinter import *

window = Tk()
window.title("Miles to KM converter")
window.minsize(width = 300, height = 200)
window.config(padx=30, pady=30)

def miles_to_km():
    km = round(float(mile_input.get())*1.609,1)
    km_label.config(text=str(km))



mile_input = Entry(width= 8, font=FONT)
mile_input.grid(column=1, row=0)

# labels
is_equal_to = Label(text='is equal to', font=FONT)
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=5)

km_label = Label(text="0", font=FONT)
km_label.grid(column=1, row=1)

miles = Label(text = "Miles", font = FONT)
miles.grid(column=2, row=0)
miles.config(padx=5)

km = Label(text = "Km", font=FONT)
km.grid(column=2, row=1)

#button
button = Button(text='Calculate', font=FONT, command=miles_to_km)
button.grid(column=1,row=2)


window.mainloop()