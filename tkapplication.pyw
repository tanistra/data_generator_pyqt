from tkinter import *

from src.data_generator import generator


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.var = StringVar()
        self.dt_label = Label(root, text="Select data type:")
        self.R1 = Radiobutton(
            root,
            text="String",
            variable=self.var,
            value='str',
            indicatoron=True)
        self.R2 = Radiobutton(root,
                              text="Integer",
                              variable=self.var,
                              value='int')
        self.R3 = Radiobutton(root,
                              text="Special characters",
                              variable=self.var,
                              value='special')
        self.R4 = Radiobutton(root,
                              text="All types",
                              variable=self.var,
                              value='all')
        self.s_label = Label(root, text="Type string length:")
        self.upper_var = BooleanVar()
        self.checkbox_upper = Checkbutton(root, text="String Uppercase", variable=self.upper_var)
        self.quit_btn = Button(root,
                               text="Quit",
                               command=root.quit)
        self.generate_btn = Button(root,
                                   text="Generate",
                                   command=self.generate_data)
        self.tex = Text(root)
        self.scrl = Scrollbar(root)
        self.set_widget()

    def set_widget(self):
        self.var.set(value='str')
        self.dt_label.place(x=10, y=10)
        self.dt_label.config(width=15, height=1)

        self.R1.place(y=50, anchor=W)
        self.R1.config(width=9, height=1)

        self.R2.place(y=70, anchor=W)
        self.R2.config(width=10, height=1)

        self.R3.place(y=90, anchor=W)
        self.R3.config(width=18, height=1)

        self.R4.place(y=110, anchor=W)
        self.R4.config(width=11, height=1)

        self.s_label.place(y=130, anchor=W)
        self.s_label.config(width=20, height=1)
        self.size = Entry(root)
        self.size.place(x=20, y=160, anchor=W)
        self.size.config(width=20)

        self.upper_var.set(True)
        self.checkbox_upper.place(x=10, y=190, anchor=W)
        self.checkbox_upper.config(width=15)

        self.quit_btn.place(x=15, y=350)
        self.quit_btn.config(width=10, height=2)
        self.generate_btn.place(x=105, y=350)
        self.generate_btn.config(width=10, height=2)

        self.scrl.pack(side=RIGHT, fill=Y)
        self.tex.place(x=200, y=1)
        self.tex.config(width=60, height=24, wrap=CHAR, yscrollcommand=self.scrl.set)
        self.scrl.config(command=self.tex.yview)

    def get_data_type(self):
        return self.var.get()

    def get_upper(self):
        return self.upper_var.get()

    def get_size(self):
        return self.size.get()

    def print_data(self, data):
        self.tex.delete('1.0', END)
        self.tex.insert(END, data)

    def generate_data(self):
        try:
            data = generator(self.get_data_type(), self.get_size(), self.get_upper())
        except ValueError as e:
            data = e
        self.print_data(data)


root = Tk()
root.title("Random string generator")
root.geometry("650x400")
app = Application(root)
root.mainloop()
