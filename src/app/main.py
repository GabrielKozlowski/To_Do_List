from tkinter import *
from tkinter import messagebox, PhotoImage
from email.message import EmailMessage
import plotly.express as px
import smtplib
import sqlite3
import sys, os

# Add path to email passwd func
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

# Import passwd from function in other folder
# from app.email_passwd.email_password import email_passwd

# email_password = email_passwd()


# BackGround Color
APP_BACKGROUND = "#cf6f0e"
INPUTS_BACKGROUND = '#ffcb96'
BUTTONS_BACKGROUND = '#c44b00'


class ToDoList():

    def __init__(self):
        # General options of window
        self.window = Tk()
        self.window.geometry("500x700")
        self.window.resizable(0, 0)
        self.window.title("To Do List")
        self.window.iconbitmap(r'E:/Programing/List_To_Do/To_Do_List/images/icon/List.ico')
        self.window.configure(background=APP_BACKGROUND)

        self.database = self.sqlite3_db()

        # Frames
        self.options_frame = self.create_options_frame()
        self.tasks_frame = self.create_tasks_frame()

        # Input field
        self.input_field = self.create_input_field()

        # Submit Button
        self.add_task_button = self.create_add_task_button()

        # Lists buttons
        self.tasks_to_do_list_button = self.create_button_for_list_of_tasks_to_do()
        self.all_tasks_list_button = self.create_button_for_all_task_list()
        self.completed_tasks_list_button = self.create_button_for_completed_tasks_list()

        # For start set bg and fg color for button showing current list
        self.tasks_to_do_list_button.config(fg=APP_BACKGROUND, bg=INPUTS_BACKGROUND)

        # List for tasks
        self.tasks = self.get_to_do_tasks_from_db()

        # List of tasks
        self.list_of_tasks = self.create_list_of_tasks()

        # Show list of tasks
        self.show_list = self.show_list_of_tasks()

        # All task in list
        self.all_tasks = self.tasks_in_list()

        # List Scrollbar
        self.list_scrollbar = self.create_scrollbar()

        # Add Scrollbar
        self.scrollbar = self.add_scrollbar()


        # Functions buttons
        self.delete_button = self.create_delete_button()        
        self.edit_task_button = self.create_edit_task_button()
        self.add_to_completed_button = self.create_add_to_completed_button()


        # Email button
        self.email_button = self.create_email_button()


        self.pie_chart = self.create_pie_chart()

        self.label_of_pie_chart = self.pie_chart_label()


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
        frame = Frame(self.window, height=150, bg=APP_BACKGROUND)
        frame.pack(fill='both', expand=False)
        return frame


    # Create button for email
    def create_email_button(self):
        email_button = Button(self.options_frame, width=20, bg=BUTTONS_BACKGROUND, fg='white', text="Send tasks to email")
        email_button.grid(row=1, column=1)    
        email_button.bind("<Button>",  lambda e: self.email_window(True))
        return email_button


    # Create button for lists
    def create_lists_button(self):
        lists_button = Button(self.options_frame, width=20, bg='#a82200', fg='white', text="Back to tasks list")
        lists_button.grid(row=1, column=1)          
        lists_button.bind("<Button>", lambda e: self.email_window(False))
        return lists_button  



    # Create button to list of tasks to do 
    def create_button_for_list_of_tasks_to_do(self):
        button = Button(self.options_frame, width=15, bg=BUTTONS_BACKGROUND, fg='white', text="Tasks to do", command=self.show_tasks_to_do_list)
        button.grid(row=0, column=0, padx=15, pady=20, sticky='')
        return button


    # Create button for all task to do list
    def create_button_for_all_task_list(self):
        button = Button(self.options_frame, width=15, bg=BUTTONS_BACKGROUND, fg='white', text="All Tasks", command=self.show_all_tasks_list)
        button.grid(row=0, column=1, padx=10, pady=20, sticky='')
        return button
    

    # Create button for completed tasks list
    def create_button_for_completed_tasks_list(self):
        button = Button(self.options_frame, width=15, bg=BUTTONS_BACKGROUND, fg='white', text="Completed Tasks", command=self.show_completed_tasks_list)
        button.grid(row=0, column=2, pady=20, padx=20, sticky='', columnspan=2)
        return button

    
    # Show list of tasks to do
    def show_tasks_to_do_list(self):
        # Changing fg and bg for clicked button
        self.tasks_to_do_list_button.config(fg=APP_BACKGROUND, bg=INPUTS_BACKGROUND)
        self.all_tasks_list_button.config(fg="white", bg=BUTTONS_BACKGROUND)
        self.completed_tasks_list_button.config(fg="white", bg=BUTTONS_BACKGROUND)

        # Connect to database
        db_connector = sqlite3.connect('to_do_list.db')

        # Create cursor
        cursor = db_connector.cursor()

        # Get tasks from all_tasks db
        tasks = cursor.execute("""SELECT name FROM task_to_do""")
        self.tasks = tasks
        self.show_list_of_tasks()
        return tasks
    

    # Show list of tasks to do
    def show_all_tasks_list(self):
        # Changing fg and bg for clicked button
        self.tasks_to_do_list_button.config(fg="white", bg=BUTTONS_BACKGROUND)
        self.all_tasks_list_button.config(fg=APP_BACKGROUND, bg=INPUTS_BACKGROUND)
        self.completed_tasks_list_button.config(fg="white", bg=BUTTONS_BACKGROUND)


        # Connect to database
        db_connector = sqlite3.connect('to_do_list.db')

        # Create cursor
        cursor = db_connector.cursor()

        # Get tasks from all_tasks db
        tasks = cursor.execute("""SELECT name FROM all_tasks""")
        self.tasks = tasks
        self.show_list_of_tasks()
        return tasks
    

    # Show list of tasks to do
    def show_completed_tasks_list(self):
        # Changing fg and bg for clicked button
        self.tasks_to_do_list_button.config(fg="white", bg=BUTTONS_BACKGROUND)
        self.all_tasks_list_button.config(fg="white", bg=BUTTONS_BACKGROUND)
        self.completed_tasks_list_button.config(fg=APP_BACKGROUND, bg=INPUTS_BACKGROUND)

        # Connect to database
        db_connector = sqlite3.connect('to_do_list.db')

        # Create cursor
        cursor = db_connector.cursor()

        # Get tasks from all_tasks db
        tasks = cursor.execute("""SELECT name FROM completed_tasks""")
        self.tasks = tasks
        self.show_list_of_tasks()
        return tasks
    



    # Create email frame
    def create_email_field(self):
        frame = Frame(self.window, width=450, height=450, bg=APP_BACKGROUND)
        frame.pack(expand=True, fill="both")
        return frame


    def email_window(self, email_frame:bool):


        # # Display email frame
        if email_frame == False:
            # Hide email frame and back to lists button
            self.email_frame.pack_forget()
            self.lists_button.grid_forget()

            # Show tasks frame, buttons, lists and input
            self.tasks_frame.pack(expand=True, fill="both")  
            # self.email_button = self.create_email_button()
            self.email_button.grid(row=1, column=1) 
            self.list_of_tasks.pack(pady=10, padx=30)
            self.input_field.grid(row=2, column=0, columnspan=3, padx=30, pady=20)
            self.add_task_button.grid(row=2, column=3, sticky='', padx=10, pady=20)

        else:
            # Hide tasks frame and buttons
            self.tasks_frame.forget()
            self.email_button.grid_forget()             
            self.input_field.grid_forget()
            self.add_task_button.grid_forget()     

            # Create email frame and back to list button
            self.email_frame = self.create_email_field() 
            self.lists_button = self.create_lists_button()


        # Create labels
        own_email_address_field = Label(self.email_frame, text="Your email address:", bg=APP_BACKGROUND, fg='white',font='bold')
        passwd_to_email_field = Label(self.email_frame, text="Password to email:", bg=APP_BACKGROUND, fg='white',font='bold')
        email_address_to_send_field = Label(self.email_frame, text ="Recipient Address:", bg=APP_BACKGROUND, fg='white',font='bold')
        subject_field = Label(self.email_frame, text="Subject:", bg=APP_BACKGROUND, fg='white', font='bold')        
        message_to_send_field = Label(self.email_frame, text ="Message:", bg=APP_BACKGROUND, fg='white', font='bold')

        # Create entries
        own_email_address_entry = Entry(self.email_frame, width=30, bg=INPUTS_BACKGROUND)
        passwd_to_email_entry = Entry(self.email_frame, width=30, bg=INPUTS_BACKGROUND)
        email_address_to_send_entry = Entry(self.email_frame, width=30, bg=INPUTS_BACKGROUND)
        subject_entry = Entry(self.email_frame, width=30, bg=INPUTS_BACKGROUND)        
        message_to_send_entry = Entry(self.email_frame, width=30, bg=INPUTS_BACKGROUND)

        # Create send email button
        send_email_button = Button(self.email_frame, width=18, bg='green', fg='white', font='bold', text='Send Email')
        
        # Create message label
        chosen_field = Label(self.email_frame, bg=APP_BACKGROUND, fg='white', font='bold', text="Which List You Want Send ?")

        # Place labels
        own_email_address_field.place(x=10, y=18)
        passwd_to_email_field.place(x=10, y=58)
        email_address_to_send_field.place(x=10, y=98)
        subject_field.place(x=10, y=138)        
        message_to_send_field.place(x=10, y=178)

        # Place entries
        own_email_address_entry.place(x=200, y=20)
        passwd_to_email_entry.place(x=200, y=60)
        email_address_to_send_entry.place(x=200, y=100)
        subject_entry.place(x=200, y=140)
        message_to_send_entry.place(x=200, y=180)

        # Create label of choosing lists
        chosen_field.place(x=90, y=240)

        # Create and places Radio buttons
        chosen_field1 = IntVar()
        chosen_field2 = IntVar()
        chosen_field3 = IntVar()
        Radiobutton(self.email_frame, text="To Do",selectcolor=APP_BACKGROUND, variable=chosen_field1, value=1, bg=APP_BACKGROUND, fg='white').place(x=50, y=280)
        Radiobutton(self.email_frame, text="All Tasks",selectcolor=APP_BACKGROUND, variable=chosen_field2, value=2, bg=APP_BACKGROUND, fg='white').place(x=150, y=280)
        Radiobutton(self.email_frame, text="Completed",selectcolor=APP_BACKGROUND, variable=chosen_field3, value=4, bg=APP_BACKGROUND, fg='white').place(x=280, y=280)

        # Place send email button
        send_email_button.place(x=110, y=360)
        # When button click, sends data to send email function
        send_email_button.bind("<Button>", lambda e: self.send_email_with_tasks(own_email_address_entry.get(), passwd_to_email_entry.get(), email_address_to_send_entry.get(),subject_entry.get(), message_to_send_entry.get(),chosen_list_nr=(chosen_field1.get() + chosen_field2.get() + chosen_field3.get())))



    # Creates a frame for tasks list
    def create_tasks_frame(self):
        frame = Frame(self.window, width=50, height=550, bg=APP_BACKGROUND)
        frame.pack(expand=True, fill="both")
        return frame


    # Create input field
    def create_input_field(self):
        field = Entry(self.options_frame, width=27, bg=INPUTS_BACKGROUND, fg='black', font='Georgia 12')
        field.grid(row=2, column=0, columnspan=3, padx=30, pady=20)
        return field


    # Create add task button
    def create_add_task_button(self):
        button = Button(self.options_frame, width=8, fg='white', bg='green', text="Add Task", command=self.add_task_to_list)
        button.grid(row=2, column=3, sticky='', padx=10, pady=20)
        return button


    # Create list of tasks
    def create_list_of_tasks(self):
        list_of_tasks = Listbox(self.tasks_frame, fg="black", bg=INPUTS_BACKGROUND, width=52, height=10, bd=0, highlightthickness=0, selectbackground='#5e5555', activestyle='none', font=12)
        list_of_tasks.pack(pady=10, padx=30)
        return list_of_tasks


    # Show list of task
    def show_list_of_tasks(self):
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
        list_scrollbar.place(x=470, y=10, height=240)
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

                # Update tasks widget
                self.create_pie_chart()
                self.update_pie_chart_label()

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

        # Get tasks from all_tasks db
        tasks = cursor.execute("""SELECT name FROM all_tasks""")
        return tasks
    

    # Get to do tasks from db
    def get_to_do_tasks_from_db(self):
        # Connect to database
        db_connector = sqlite3.connect('to_do_list.db')

        # Create cursor
        cursor = db_connector.cursor()

        # Get tasks from task to do db
        tasks = cursor.execute("""SELECT name FROM task_to_do""")
        return tasks
    

    # Get completed tasks from db
    def get_completed_tasks_from_db(self):
        # Connect to database
        db_connector = sqlite3.connect('to_do_list.db')

        # Create cursor
        cursor = db_connector.cursor()

        # Get tasks from completed tasks db
        tasks = cursor.execute("""SELECT name FROM completed_tasks""")
        return tasks


    # Create update frame
    def create_update_frame(self):
        update_frame = Frame(self.tasks_frame, width=500, height=80, bg=APP_BACKGROUND)
        update_frame.pack(expand=True, fill="both")
        return update_frame





    # Edit task
    def edit_task(self):
        try:
            # Get name of task to update from selected task
            task_to_update = self.list_of_tasks.selection_get()

            if task_to_update != '':
                # Delete old task
                self.list_of_tasks.delete(ANCHOR)

                # Hide list of task frame
                self.list_of_tasks.forget()

                # Show update frame
                self.create_entry_for_update_task(task_to_update)

                return task_to_update

        except TclError as err:
            return err
            

    # Edit and Update task in lists
    def update_task(self, task_to_update, updated_task):

        # Insert to list new task
        self.list_of_tasks.insert(END, updated_task)

        # Connect to database
        db_connector = sqlite3.connect('to_do_list.db')

        # Create cursor
        cursor = db_connector.cursor()

        # Update database task in table 'task to do'
        cursor.execute(f"""UPDATE task_to_do SET name='{updated_task}' WHERE name='{task_to_update}'""")
        
        # Update database task in table 'all task'
        cursor.execute(f"""UPDATE all_tasks SET name='{updated_task}' WHERE name='{task_to_update}'""")
       
        # Update database task in table 'completed tasks'
        cursor.execute(f"""UPDATE completed_tasks SET name='{updated_task}' WHERE name='{task_to_update}'""")

        # Commit changes and close connection
        db_connector.commit()
        db_connector.close()

        # Hide update frame
        self.update_frame.forget()

        # Show list frame and buttons
        self.list_of_tasks.pack(pady=10, padx=30)

        self.tasks_to_do_list_button.grid(row=0, column=0, padx=15, pady=20, sticky='')
        self.all_tasks_list_button.grid(row=0, column=1, padx=10, pady=20, sticky='')
        self.completed_tasks_list_button.grid(row=0, column=2, pady=20, padx=20, sticky='', columnspan=2)
        self.email_button.grid(row=1, column=1)

        self.input_field.grid(row=2, column=0, columnspan=3, padx=30, pady=20)
        self.add_task_button.grid(row=2, column=3, sticky='', padx=10, pady=20)

        self.delete_button.place(x=20, y=440)
        self.edit_task_button.place(x=20, y=380)
        self.add_to_completed_button.place(x=20, y=320)       

        # Show widget
        self.label_of_pie_chart.place(x=270, y=300)

        return updated_task

    
    # Create function for back to lists field
    def back_to_lists(self, no_updated_task):
        
        # Hide update frame
        self.update_frame.forget()

        # Show list frame and buttons
        self.list_of_tasks.pack(pady=10, padx=30)

        self.tasks_to_do_list_button.grid(row=0, column=0, padx=15, pady=20, sticky='')
        self.all_tasks_list_button.grid(row=0, column=1, padx=10, pady=20, sticky='')
        self.completed_tasks_list_button.grid(row=0, column=2, pady=20, padx=20, sticky='', columnspan=2)
        self.email_button.grid(row=1, column=1)
        
        self.input_field.grid(row=2, column=0, columnspan=3, padx=30, pady=20)
        self.add_task_button.grid(row=2, column=3, sticky='', padx=10, pady=20)
        
        self.delete_button.place(x=20, y=440)
        self.edit_task_button.place(x=20, y=380)
        self.add_to_completed_button.place(x=20, y=320) 


        # Show widget
        self.label_of_pie_chart.place(x=270, y=300)


        # Insert to list not updated task
        self.list_of_tasks.insert(END, no_updated_task)



    # Create new entry for updates task
    def create_entry_for_update_task(self, task_to_update):
        # Show update form
        self.update_frame = self.create_update_frame()

        # Hide buttons
        self.delete_button.forget()
        self.add_to_completed_button.forget()
        self.edit_task_button.pack_forget()
        self.tasks_to_do_list_button.grid_forget()
        self.all_tasks_list_button.grid_forget()
        self.completed_tasks_list_button.grid_forget()
        self.email_button.grid_forget()
        self.input_field.grid_forget()
        self.add_task_button.grid_forget()



        # Create label to update task in update form
        updated_task_label = Label(self.update_frame, text="Update this task:", bg=APP_BACKGROUND, fg='white', font='Arial 16')
        updated_task_label.place(x=40, y=40)

        # Create entry for update task in update form
        updated_task_entry = Entry(self.update_frame, width=35, bg=INPUTS_BACKGROUND, fg='black', font='bold')
        updated_task_entry.insert(0, task_to_update)
        updated_task_entry.place(x=40, y=90)


        # Create button for update task
        update_button = Button(self.update_frame, text='Update task', width=15, bg='green', fg='white', font='bold')
        update_button.place(x=40, y=150)
        update_button.bind("<Button>", lambda e: self.update_task(task_to_update, updated_task_entry.get()))

        # Create button for back to lists
        back_button = Button(self.update_frame, text="Back to tasks", width=15,  bg="#a82200", fg="white", font="bold")
        back_button.place(x=275, y=150)
        back_button.bind("<Button>", lambda e: self.back_to_lists(task_to_update))

        return updated_task_entry



    # Delete task from bd
    def delete_task_in_db(self):
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

            # Update tasks widget
            self.create_pie_chart()
            self.update_pie_chart_label()

            return task_to_delete
        
        return task_to_delete


    # Add task to completed list
    def add_to_completed_list(self):
        # Get name of task to transferred to list of completed task
        task_to_transfer = self.list_of_tasks.selection_get()

        if task_to_transfer != '':

            # Connect to database
            db_connect = sqlite3.connect('to_do_list.db')
            cursor = db_connect.cursor()    

            completed_tasks = cursor.execute("""SELECT name FROM completed_tasks""")
            completed_tasks = [task[0] for task in list(completed_tasks)]
            
            if task_to_transfer not in completed_tasks:

                # Delete selected task in task to do list
                self.list_of_tasks.delete(ANCHOR)



                # Delete task in "task to do" table in database
                cursor.execute(f"""DELETE FROM task_to_do WHERE name='{task_to_transfer}'""")

                # Add task to "completed task" table in database
                cursor.execute(f"""INSERT INTO completed_tasks(id, name) VALUES(null, '{task_to_transfer.capitalize()}')""")

                # Commit changes in database and close connections
                db_connect.commit()
                db_connect.close()

                # Update tasks widget
                self.create_pie_chart()
                self.update_pie_chart_label()

                return task_to_transfer
            
            return task_to_transfer
        
        return task_to_transfer

    # Create add task to completed list button
    def create_add_to_completed_button(self):
        add_to_completed_button = Button(self.tasks_frame, width=20, text="Add to completed", bg='green', fg="white", font='bold', command=self.add_to_completed_list)
        add_to_completed_button.place(x=20, y=320)
        return add_to_completed_button


    # Create update task button
    def create_edit_task_button(self):
        edit_task_button = Button(self.tasks_frame, width=20, text="Edit This Task", bg='blue', fg="white", font='bold', command=self.edit_task)
        edit_task_button.place(x=20, y=380)
        return edit_task_button


    # Create delete button
    def create_delete_button(self):
        delete_button = Button(self.tasks_frame, width=20, text="Delete task", bg="red", fg="white", font='bold', command=self.delete_task_in_db)
        delete_button.place(x=20, y=440)
        return delete_button
        

    # Create send error box
    def send_error_box(self, error):
        messagebox.showinfo('ERROR !!!', error)
        return error


    # Send email with tasks
    def send_email_with_tasks(self, my_email:str, email_passwd:str, email_to_send:str,subject:str, message:str, chosen_list_nr:int):
            # My email data         
            # my_email = "gabrielnauka2020@gmail.com"            
            # email_passwd = email_password

            
            # Tags string for lists
            topTagTaskToDo = '\n\n---=== Task To Do ===---\n'
            topTagAllTasks = '\n\n---=== All Tasks ===---\n'
            topTagCompletedTasks = '\n\n---=== Completed Tasks ===---\n'

            # Lists variable for send to email
            task_to_do_list = ''
            all_tasks_list = ''
            completed_tasks_list = ''
            
            # Checks if must send the contents of some lists
            if chosen_list_nr == 1:
                    # Add string on top the list
                    task_to_do_list += topTagTaskToDo
                    # Get tasks from 'task to do' DataBase  
                    task_to_do_list += '\n'.join([task[0] for task in list(self.get_to_do_tasks_from_db())])
                    
            elif chosen_list_nr == 2:
                    # Add string on top the list
                    all_tasks_list += topTagAllTasks
                    # Get tasks from 'all tasks' DataBase  
                    all_tasks_list += '\n'.join([task[0] for task in list(self.get_all_tasks_from_db())])
                                        
            elif chosen_list_nr == 3:
                    # Add string on top the list
                    task_to_do_list += topTagTaskToDo
                    # Get tasks from 'task to do' DataBase  
                    task_to_do_list += '\n'.join([task[0] for task in list(self.get_to_do_tasks_from_db())])

                    # Add string on top the list
                    all_tasks_list += topTagAllTasks
                    # Get tasks from 'all tasks' DataBase  
                    all_tasks_list += '\n'.join([task[0] for task in list(self.get_all_tasks_from_db())])

            elif chosen_list_nr == 4:
                    # Add string on top the list
                    completed_tasks_list += topTagCompletedTasks
                    # Get tasks from 'completed tasks' DataBase   
                    completed_tasks_list += '\n'.join([task[0] for task in list(self.get_completed_tasks_from_db())])
                    
            elif chosen_list_nr == 5:
                    # Add string on top the list
                    task_to_do_list += topTagTaskToDo
                    # Get tasks from 'task to do' DataBase  
                    task_to_do_list += '\n'.join([task[0] for task in list(self.get_to_do_tasks_from_db())])

                    # Add string on top the list
                    completed_tasks_list += topTagCompletedTasks                 
                    # Get tasks from 'completed tasks' DataBase   
                    completed_tasks_list += '\n'.join([task[0] for task in list(self.get_completed_tasks_from_db())])
            
            elif chosen_list_nr == 6:
                    # Add string on top the list
                    all_tasks_list += topTagAllTasks
                    # Get tasks from 'all tasks' DataBase  
                    all_tasks_list += '\n'.join([task[0] for task in list(self.get_all_tasks_from_db())])

                    # Add string on top the list
                    completed_tasks_list += topTagCompletedTasks
                    # Get tasks from 'completed tasks' DataBase   
                    completed_tasks_list += '\n'.join([task[0] for task in list(self.get_completed_tasks_from_db())])
            
            elif chosen_list_nr == 7:
                    # Add string on top the list
                    task_to_do_list += topTagTaskToDo                  
                    # Get tasks from 'task to do' DataBase  
                    task_to_do_list += '\n'.join([task[0] for task in list(self.get_to_do_tasks_from_db())])

                    # Add string on top the list
                    all_tasks_list += topTagAllTasks
                    # Get tasks from 'all tasks' DataBase  
                    all_tasks_list += '\n'.join([task[0] for task in list(self.get_all_tasks_from_db())])

                    # Add string on top the list
                    completed_tasks_list += topTagCompletedTasks
                    # Get tasks from 'completed tasks' DataBase   
                    completed_tasks_list += '\n'.join([task[0] for task in list(self.get_completed_tasks_from_db())])


            # Add all contents to sended message
            completed_message = f"{message}\n\n {task_to_do_list}{completed_tasks_list}{all_tasks_list}"

            # Create EmailMessage object
            msg = EmailMessage()
            msg.set_content(completed_message)

            # Config values of object
            msg['Subject'] = subject
            msg['From'] = my_email
            msg['To'] = email_to_send

            try:
                # Create smtplib SMTP object
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()

                # Login to email
                server.login(my_email, email_passwd)
                # Send message
                server.send_message(msg)

                # Hide email frame and button back to list
                self.email_frame.pack_forget()
                self.lists_button.grid_forget()

                # Show tasks frame , input and buttons (add, send to email)
                self.tasks_frame.pack(expand=True, fill="both")
                self.email_button.grid(row=1, column=1) 
                self.input_field.grid(row=2, column=0, columnspan=3, padx=30, pady=20)
                self.add_task_button.grid(row=2, column=3, sticky='', padx=10, pady=20)


            # Catch ten errors
            except smtplib.SMTPAuthenticationError:
                self.send_error_box("Email Address or Password incorrect !!! Try again.")

            except smtplib.SMTPRecipientsRefused:
                self.send_error_box("Wrong Recipient Address !!! Try again.")


    def create_pie_chart(self):
        # Connect to database
        db_connector = sqlite3.connect('to_do_list.db')

        # Create cursor
        cursor = db_connector.cursor()
        # Get tasks from task to do db
        tasks_to_do = cursor.execute("""SELECT name FROM task_to_do""")

        # Create cursor
        cursor = db_connector.cursor()
        # Get tasks from completed tasks db
        completed_tasks = cursor.execute("""SELECT name FROM completed_tasks""")

        # Create cursor
        cursor = db_connector.cursor()
        # Get tasks from all_tasks db
        all_tasks = cursor.execute("""SELECT name FROM all_tasks""")


        # Get len of tasks in all lists
        len_of_completed_tasks = len([task[0] for task in list(completed_tasks)])
        len_of_tasks_to_do = len([task[0] for task in list(tasks_to_do)])
        len_of_all_tasks = len([task[0] for task in list(all_tasks)])

        # Create names and values for widget
        field_names = [f"{len_of_completed_tasks}<br>Completed Tasks", f"{len_of_tasks_to_do}<br>Tasks To Do"]
        field_values = [len_of_completed_tasks, len_of_tasks_to_do]

        # Create title with len of all tasks
        title = f"All tasks<br>{len_of_all_tasks}"

        if len_of_all_tasks > 0:
            fig = px.pie(values=field_values, names=field_names, color=field_names, hole=0.35, color_discrete_map={(str(len_of_completed_tasks) + "<br>Completed Tasks") : "#458B00", (str(len_of_tasks_to_do)  + "<br>Tasks To Do") : "#FFA500"})

            fig.update_layout(autosize=False, width=350, height=350, showlegend=False, paper_bgcolor=APP_BACKGROUND)
            

    
            fig.update_traces(direction="clockwise",sort=False, rotation=90, textposition='inside',
                        title=title,
                        title_font_color="white",
                        textinfo='label+percent',
                        textfont_size=14,
                        textfont_color='white')
            
            if len_of_completed_tasks <= 0:
                fig.update_traces(rotation=180)

            elif len_of_tasks_to_do <= 0:
                fig.update_traces(rotation=0)
       
        else:
            fig = px.pie(values=[1,0], names=['Waiting for task',''], hole=0.35, color=['Waiting for task',''], color_discrete_map={'Waiting for task': INPUTS_BACKGROUND, '': INPUTS_BACKGROUND})

            fig.update_layout(autosize=False, width=350, height=350, showlegend=False, paper_bgcolor=APP_BACKGROUND)

            fig.update_traces(direction="clockwise",sort=False, rotation=0, textposition='inside',
                        title=title,
                        title_font_color="white",
                        textinfo='label',
                        textfont_size=18,
                        textfont_color='black')

        fig.write_image("images/pie_chart.png")


    # Create pie chart label
    def pie_chart_label(self):
        image = PhotoImage(file="images/pie_chart.png")
        label_of_pie_chart = Label(self.tasks_frame, image=image, width=220, height=220)
        label_of_pie_chart.photo = image
        label_of_pie_chart.place(x=270, y=300)
        return label_of_pie_chart


    # Update pie chart label
    def update_pie_chart_label(self):
        self.label_of_pie_chart.place_forget()
        image = PhotoImage(file="images/pie_chart.png")
        label_of_pie_chart = Label(self.tasks_frame, image=image, width=220, height=220)
        label_of_pie_chart.photo = image
        label_of_pie_chart.place(x=270, y=300)
        return label_of_pie_chart



    # Run program

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    TDL = ToDoList()
    TDL.run()


