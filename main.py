from tkinter import *

root = Tk()
root.title('заголовок')
root.geometry("400x600")
root.resizable(True, True)

lab = Label(root, width=100, height=100, bg='green',fg='red', text="help me:)")
lab.pack(side="left")

ent = Entry(root, width=100)
ent.pack()

but = Button(root, text="кнопка")
but.pack()

root.mainloop()