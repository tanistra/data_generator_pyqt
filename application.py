from tkinter import *
from data_generator import generator


class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.dt_label = Label(frame, text="Type data type")
    self.dt_label.pack()
    self.data_type = Entry(frame)
    self.data_type.pack()
    self.s_label = Label(frame, text="Type string length")
    self.s_label.pack()
    self.size = Entry(frame)
    self.size.pack()
    self.tex = Text(frame)
    self.tex.pack()

    self.button = Button(frame,
                           text="QUIT", fg="red",
                           command=frame.quit)
    self.button.pack(side=LEFT)
    self.slogan = Button(frame,
                           text="Generate",
                           command=self.write_slogan)
    self.slogan.pack(side=LEFT)


  def get_data_type(self):
      return self.data_type.get()

  def get_size(self):
      return self.size.get()

  def print_data(self, data):
      self.tex.delete('1.0',END)
      self.tex.insert(END, data)

  def write_slogan(self):
      data = generator(self.get_data_type(), self.get_size())
      self.print_data(data)


root = Tk()
app = App(root)
root.mainloop()