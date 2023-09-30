from tkinter import *
from time import sleep
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

        # Lists buttons
        self.tasks_to_do_list_button = self.create_button_for_list_of_tasks_to_do()
        self.all_tasks_list_button = self.create_button_for_all_task_list()
        self.completed_tasks_list_button = self.create_button_for_completed_tasks_list()

        # List for tasks
        self.tasks = self.get_all_tasks_from_db()

        # List of tasks
        self.list_of_tasks = self.create_list_of_tasks()

        # Show list of tasks
        self.show_list = self.show_list_of_task()

        # All task in list
        self.all_tasks = self.tasks_in_list()

        # List Scrollbar
        self.list_scrollbar = self.create_scrollbar()

        # Add Scrollbar
        self.scrollbar = self.add_scrollbar()


        # Functions buttons
        self.add_to_completed_button = self.create_add_to_completed_button()
        self.delete_button = self.create_delete_button()

        # Email button
        self.email_button = self.create_email_button()



    def sqlite3_db(self):
        # Create or connect to database
        db_connector = sqlite3.connect('to_do_list.db')

        # Create cursor
        cursor = db_connector.cursor()

        # Create tables
        cursor.execute("""CREATE TABLE IF NOT EXISTS all_tasks(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name VARCHAR(255) UNIQUE NOT NULL
                       )""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS task_to_do(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name VARCHAR(255) UNIQUE NOT NULL
                       )""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS completed_tasks(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name VARCHAR(255) UNIQUE NOT NULL
                       )""")
        
        # Commit changes in database
        db_connector.commit()
        db_connector.close()








    # Creates a frame for options buttons
    def create_options_frame(self):
        frame = Frame(self.window, height=150, bg='red')
        frame.pack(fill='both', expand=False)
        return frame


    # Create button for email
    def create_email_button(self):
        button = Button(self.options_frame, width=20, bg='grey', fg='white', text="Send task to email")
        
        button.grid(row=1, column=1)
        button.bind("<Button>",  lambda e: self.email_window())
        return button


    # Create button to list of tasks to do 
    def create_button_for_list_of_tasks_to_do(self):
        button = Button(self.options_frame, width=15, bg='grey', fg='white', text="Tasks to do", command=self.show_tasks_to_do_list)
        button.grid(row=0, column=0, pady=20, sticky='')
        return button


    # Create button for all task to do list
    def create_button_for_all_task_list(self):
        button = Button(self.options_frame, width=15, bg='grey', fg='white', text="All Tasks", command=self.show_all_tasks_list)
        button.grid(row=0, column=1, pady=20, sticky='')
        return button
    

    # Create button for completed tasks list
    def create_button_for_completed_tasks_list(self):
        button = Button(self.options_frame, width=15, bg='grey', fg='white', text="Completed Tasks", command=self.show_completed_tasks_list)
        button.grid(row=0, column=2, pady=20, padx=10, sticky='', columnspan=2)
        return button

    
    # Show list of tasks to do
    def show_tasks_to_do_list(self):
        # Connect to database
        db_connector = sqlite3.connect('to_do_list.db')

        # Create cursor
        cursor = db_connector.cursor()

        # Get tasks from all_tasts db
        tasks = cursor.execute("""SELECT name FROM task_to_do""")
        self.tasks = tasks
        self.show_list_of_task()
        return tasks
    

    # Show list of tasks to do
    def show_all_tasks_list(self):
        # Connect to database
        db_connector = sqlite3.connect('to_do_list.db')

        # Create cursor
        cursor = db_connector.cursor()

        # Get tasks from all_tasts db
        tasks = cursor.execute("""SELECT name FROM all_tasks""")
        self.tasks = tasks
        self.show_list_of_task()
        return tasks
    

    # Show list of tasks to do
    def show_completed_tasks_list(self):
        # Connect to database
        db_connector = sqlite3.connect('to_do_list.db')

        # Create cursor
        cursor = db_connector.cursor()

        # Get tasks from all_tasts db
        tasks = cursor.execute("""SELECT name FROM completed_tasks""")
        self.tasks = tasks
        self.show_list_of_task()
        return tasks
    

    # Open email window
    def email_window(self):
        master = Tk()
        master.title("New Window")
        master.geometry("500x500")

        own_email_address_field = Label(master, text="Your email address:")
        passwd_to_email_field = Label(master, text="Password for email:")
        email_address_to_send_field = Label(master, text ="Recipient Address:")
        message_to_send_field = Label(master, text ="Message:")

        own_email_address_entry = Entry(master, width=40)
        passwd_to_email_entry = Entry(master, width=40)
        email_addres_to_send_entry = Entry(master, width=40)
        message_to_send_entry = Entry(master, width=40)

        send_email_buton = Button(master, width=20, text='Send Email')
        
        choosen_field = Label(master, text="Which List You Want Send ?")


        choosen_list = IntVar()
        Radiobutton(master, text="To Do", variable=choosen_list, value=1).grid(row=5, column=0)
        Radiobutton(master, text="All Tasks", variable=choosen_list, value=2).grid(row=5, column=1)
        Radiobutton(master, text="Completed", variable=choosen_list, value=3).grid(row=5, column=2)

        own_email_address_field.grid(row=0, column=0)
        own_email_address_entry.grid(row=0, column=1, columnspan=2)
        passwd_to_email_field.grid(row=1, column=0)
        passwd_to_email_entry.grid(row=1, column=1, columnspan=2)


        email_address_to_send_field.grid(row=2, column=0)
        email_addres_to_send_entry.grid(row=2, column=1, columnspan=2)

        message_to_send_field.grid(row=3, column=0)
        message_to_send_entry.grid(row=3, column=1, columnspan=2)

        choosen_field.grid(row=4, column=1)

        send_email_buton.grid(row=6, column=1)
        

        return master




    # Create input field
    def create_input_field(self):
        field = Entry(self.options_frame, width=27, bg='gray', fg='white', font='Georgia 12')
        field.grid(row=2, column=0, columnspan=3, padx=30, pady=20)
        return field

    # Create add task button

    def create_add_task_button(self):
        button = Button(self.options_frame, width=8, fg='white', bg='green', text="Add Task", command=self.add_task_to_list)
        button.grid(row=2, column=3, sticky='', padx=10, pady=20)
        return button


    # Creates a frame for tasks list
    def create_tasks_frame(self):
        frame = Frame(self.window, width=50, height=550, bg='yellow')
        frame.pack(expand=True, fill="both")
        return frame


    # Create list of tasks
    def create_list_of_tasks(self):
        list_of_tasks = Listbox(self.tasks_frame, fg="white", bg="grey", width=52, height=15, bd=0,highlightthickness=0, selectbackground='#5e5555', activestyle='none', font=12)
        list_of_tasks.pack(pady=20, padx=30)

        return list_of_tasks


    # Show list of task
    def show_list_of_task(self):
        # Get ListBox frame
        list_of_tasks = self.list_of_tasks
        list_of_tasks.delete(0, END)

        tasks = [task[0].capitalize() for task in self.tasks]
        for task in tasks:
            list_of_tasks.insert(END, task)

        return list_of_tasks


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
        if new_task != '':


            # Connect to database
            db_connector = sqlite3.connect('to_do_list.db')

            # Create cursor
            cursor = db_connector.cursor()

            # Get all tasks name
            tasks = cursor.execute("""SELECT name FROM all_tasks""")
            # Convert to list
            tasks_list = [task[0] for task in list(tasks)]

            if new_task.capitalize() not in tasks_list:

                # Add task to list
                self.list_of_tasks.insert(END, new_task.capitalize())

                # Add task to database (all_tasks, task_to_do) tables
                cursor.execute(f"""INSERT INTO all_tasks(id, name) VALUES(null, '{new_task.capitalize()}')""")
                cursor.execute(f"""INSERT INTO task_to_do(id, name) VALUES(null, '{new_task.capitalize()}')""")

                # Commit changes in database
                db_connector.commit()

                # Clear task input
                self.input_field.delete(0, END)   

            db_connector.close()
            return new_task

        return new_task


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
        # Get name of task to delete from selected task
        task_to_delete = self.list_of_tasks.selection_get()

        if task_to_delete != '':

            # Delete selected task in list
            self.list_of_tasks.delete(ANCHOR)

            # Connect to database
            db_connect = sqlite3.connect('to_do_list.db')
            cursor = db_connect.cursor()

            # Delete task in database
            cursor.execute(f"""DELETE FROM all_tasks WHERE name='{task_to_delete}'""")
            cursor.execute(f"""DELETE FROM task_to_do WHERE name='{task_to_delete}'""")
            cursor.execute(f"""DELETE FROM completed_tasks WHERE name='{task_to_delete}'""")
        
            # Commit changes in database and close connections
            db_connect.commit()
            db_connect.close()

            return task_to_delete
        
        return task_to_delete


    # Add task to completed list
    def add_to_completed_list(self):
        # Get name of task to transferred to list of completed task
        task_to_transfer = self.list_of_tasks.selection_get()

        if task_to_transfer != '':

            # Delete selected task in task to do list
            self.list_of_tasks.delete(ANCHOR)

            # Connect to database
            db_connect = sqlite3.connect('to_do_list.db')
            cursor = db_connect.cursor()

            # Delete task in "task to do" table in database
            cursor.execute(f"""DELETE FROM task_to_do WHERE name='{task_to_transfer}'""")

            # Add task to "completed task" table in database
            cursor.execute(f"""INSERT INTO completed_tasks(id, name) VALUES(null, '{task_to_transfer.capitalize()}')""")

            # Commit changes in database and close connections
            db_connect.commit()
            db_connect.close()

            return task_to_transfer
        
        return task_to_transfer



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
