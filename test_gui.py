import tkinter as tk

# window
root = tk.Tk()
root.title('hello world')
root.geometry('1400x700')

# label
my_label = tk.Label(root, text='hello world', font=('Arial', 18))
my_label.pack()

# btn
def button_event():
    my_btn['text'] = 'hello btn'
my_btn = tk.Button(root, text='button', command=button_event)
my_btn.pack()

mylabel = tk.Label(root, text='Name:')
mylabel.grid(row=0, column=0)
myentry = tk.Entry(root)
myentry.grid(row=0, column=1)

mylabel2 = tk.Label(root, text='Password:')
mylabel2.grid(row=1, column=0)
myentry2 = tk.Entry(root, show='*')
myentry2.grid(row=1, column=1)

mybutton = tk.Button(root, text='Login')
mybutton.grid(row=2, column=1)


root.mainloop()