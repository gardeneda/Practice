from tkinter import *

window = Tk()
window.title("Miles to Km converter")
window.config(padx=20, pady=20)

miles_label = Label(text="Miles")
miles_label.grid(column=3, row=1)

km_label = Label(text="Km")
km_label.grid(column=3, row=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=1, row=2)

km_number_label = Label(text="0")
km_number_label.grid(column=2, row=2)

miles_entry = Entry(width=15)
miles_entry.insert(END, "0")
miles_entry.grid(column=2, row=1)


def miles_to_km_calculate_initiate():
    miles = float(miles_entry.get())
    km = miles * 1.609344
    float_km = "{:.2f}".format(km)
    km_number_label.config(text=float_km)
    return km


calculate_button = Button(text="Calculate", command=miles_to_km_calculate_initiate)
calculate_button.grid(column=2, row=3)

window.mainloop()
