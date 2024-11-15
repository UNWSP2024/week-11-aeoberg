import tkinter
import tkinter.messagebox
from os.path import commonpath


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title('Address GUI')


        self.my_button= tkinter.Button(self.main_window,\
                                       text='Show Info',\
                                       command = self.do_something)

        self.quit_button = tkinter.Button(self.main_window,
                                          text = "Quit",
                                          command=self.main_window.destroy)

        self.my_button.pack()
        self.quit_button.pack()

        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Response',\
                                    'Addison Oberg\n1915 134th Lane NE\n Ham Lake, Minnesota, 55304')

if __name__ == '__main__':
    my_qui = MyGUI()