import tkinter as tk

LIGHT_ORANGE = "#ffa64d"

class ToDoList():

    def __init__(self):
        # General options of window
        self.window = tk.Tk()
        self.window.geometry("500x700")
        self.window.resizable(0,0)
        self.window.title("To Do List")
        # self.window.configure(background=LIGHT_ORANGE)
        


        # List for tasks
        self.tasks = ['Do your loundry !!', 'clean your dishes']

        # Tasks in list
        self.tasks_list = self.tasks_in_list()


        self.options_frame = self.create_options_frame()
        self.tasks_frame = self.create_tasks_frame()
        

        self.tasks_list = self.create_tasks_list()




    # Creates a frame for options buttons
    def create_options_frame(self):
        frame = tk.Frame(self.window, bg='green')
        frame.pack(expand=True, fill='both')
        return frame

    # Creates a frame for tasks list
    def create_tasks_frame(self):
        frame = tk.Frame(self.window, height=300, bg="yellow")
        frame.pack(expand=True, fill='both')
        return frame


    # Create tasks list
    def create_tasks_list(self):
        label_list = tk.Label(self.tasks_frame, text=self.tasks_list, fg="white", bg="grey",anchor="w", justify="left")
        label_list.pack(expand=True, fill='both')
        return label_list


    # create buttons for list options
    def list_button_frame(self):
        button = tk.Button(self.options_frame, bg="red", text='2')
        button.pack()
        return button


    def tasks_in_list(self):
        result = ''
        for task in self.tasks:
            result += (task + '\n')

        return result











    # Run program
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    TDL = ToDoList()
    TDL.run()
