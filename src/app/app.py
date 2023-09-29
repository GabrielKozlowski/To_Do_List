from tkinter import *
import sqlite3

LIGHT_ORANGE = "#ffa64d"


class ToDoList():

    def __init__(self):
        # General options of window
        self.window = Tk()
        self.window.geometry("500x700")
        self.window.resizable(0, 0)
        self.window.title("To Do List")
        self.window.configure(background=LIGHT_ORANGE)

        self.database = self.sqlite3_db()

        # Frames
        self.options_frame = self.create_options_frame()
        self.tasks_frame = self.create_tasks_frame()

        # Input field
        self.input_field = self.create_input_field()

        # Submit Button
        self.button = self.create_add_task_button()

        # List for tasks
        self.tasks = self.get_all_tasks_from_db()

        # List of tasks
        self.list_of_tasks = self.create_list_of_tasks()


        # All task in list
        self.all_tasks = self.tasks_in_list()

        # List Scrollbar
        self.list_scrollbar = self.create_scrollbar()

        # Add Scrollbar
        self.scrollbar = self.add_scrollbar()


        # Functions buttons
        self.add_to_completed_button = self.create_add_to_completed_button()
        self.delete_button = self.create_delete_button()


    def sqlite3_db(self):
        # Create or connect to database
        db_connector = sqlite3.connect('to_do_list.db')

        # Create cursor
        cursor = db_connector.cursor()

        # Create tables
        cursor.execute("""CREATE TABLE IF NOT EXISTS all_tasks(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name VARCHAR(255) NOT NULL
                       )""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS task_to_do(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name VARCHAR(255) NOT NULL
                       )""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS comleted_tasks(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name VARCHAR(255) NOT NULL
                       )""")
        
        # Commit changes in database
        db_connector.commit()
        db_connector.close()






    # Creates a frame for options buttons
    def create_options_frame(self):
        frame = Frame(self.window, height=250, bg='red')
        frame.pack(fill='both', expand=True)
        return frame


    # Create input field
    def create_input_field(self):
        field = Entry(self.options_frame, width=30, bg='gray', fg='black', font='Georgia 12')        
        field.pack(side=LEFT, expand=True, pady=20)
        return field

    # Create add task button

    def create_add_task_button(self):
        button = Button(self.options_frame, width=8, bg='green', text="Add Task", command=self.add_task_to_list)
        button.pack(side=RIGHT, expand=True)
        return button


    # Creates a frame for tasks list
    def create_tasks_frame(self):
        frame = Frame(self.window, width=50, height=450, bg='yellow')
        frame.pack(expand=True, fill="both")
        return frame


    # Create frame for tasks list
    def create_list_of_tasks(self):
        tasks_list = Listbox(self.tasks_frame, fg="white", bg="grey", width=52, height=15, bd=0,highlightthickness=0, selectbackground='#5e5555', activestyle='none', font=12)
        tasks_list.pack(pady=20, padx=30)

        # Change tasks to list and capitalize 
        tasks = [task[0].capitalize() for task in list(self.tasks)]
        for task in tasks:
            tasks_list.insert(END, task)

        return tasks_list


    # Create scrollbar
    def create_scrollbar(self):
        list_scrollbar = Scrollbar(self.tasks_frame)
        list_scrollbar.place(x=470, y=20, height=360)
        return list_scrollbar
    
    # Add scrollbar to list
    def add_scrollbar(self):
        self.list_of_tasks.config(yscrollcommand=self.list_scrollbar)
        self.list_scrollbar.config(command=self.list_of_tasks.yview)
        


    # Get tasks from list and return tasks in string
    def tasks_in_list(self):
        tasks_list = [task[0].capitalize() for task in list(self.tasks)]
        return '\n'.join(tasks_list)


    # Add task to db lists
    def add_task_to_list(self):
        # Get task name from input
        new_task = self.input_field.get()

        # Add task to list
        self.list_of_tasks.insert(END, new_task.capitalize())

        # Connect to database
        db_connector = sqlite3.connect('to_do_list.db')

        # Create cursor
        cursor = db_connector.cursor()

        # Get tasks from all_tasts db
        cursor.execute(f"""INSERT INTO all_tasks(id, name) VALUES(null, '{new_task.capitalize()}')""")
        cursor.execute(f"""INSERT INTO task_to_do(id, name) VALUES(null, '{new_task.capitalize()}')""")

        # Commit changes in database
        db_connector.commit()
        db_connector.close()

        # Clear task input
        self.input_field.delete(0, END)


    # Get all tasks from db
    def get_all_tasks_from_db(self):
        # Connect to database
        db_connector = sqlite3.connect('to_do_list.db')

        # Create cursor
        cursor = db_connector.cursor()

        # Get tasks from all_tasts db
        tasks = cursor.execute("""SELECT name FROM all_tasks""")

        return tasks


    # Delete task from bd
    def delete_tast_in_db(self):
        task_to_delete = self.list_of_tasks.selection_get()
        self.list_of_tasks.delete(ANCHOR)
        db_connect = sqlite3.connect('to_do_list.db')
        cursor = db_connect.cursor()
        cursor.execute(f"""DELETE FROM all_tasks WHERE name='{task_to_delete}'""")
        db_connect.commit()
        db_connect.close()
        


    # Add task to completed list
    def add_to_completed_list(self):
        pass


    # Create Function Buttons
    def create_delete_button(self):
        delete_button = Button(self.tasks_frame, width=20, text="Delete task", bg="red", fg="white", font='bold', command=self.delete_tast_in_db)
        delete_button.pack(side=RIGHT, padx=30)
        return delete_button
        

    def create_add_to_completed_button(self):
        add_to_completed_button = Button(self.tasks_frame, width=20, text="Add to completed", bg='green', fg="white", font='bold', command=self.add_to_completed_list)
        add_to_completed_button.pack(side=LEFT, padx=30)
        return add_to_completed_button








    # Run program

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    TDL = ToDoList()
    TDL.run()
