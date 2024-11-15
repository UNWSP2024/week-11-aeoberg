import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title('My First GUI')

        self.label = tkinter.Label(self.main_window, text = "Either you run the day or the day runs you - Jim Rohn")
        self.label.pack()

        tkinter.mainloop()

if __name__ == '__main__':
    my_qui = MyGUI()