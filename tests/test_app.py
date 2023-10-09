import os, sys

# Add path to main file application 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

# Import class from main 
from src.app.main import ToDoList

# Set class object
window = ToDoList()

# Testing created frame in program

def test_create_options_frame():
    var = window.create_options_frame()    
    assert str(var) == '.!frame3'


def test_create_tasks_frame():
    var = window.create_tasks_frame()
    assert str(var) == ".!frame4"


def test_create_update_frame():
    var = window.create_update_frame()
    assert str(var) == ".!frame2.!frame"


def test_update_frame():
    var = window.create_update_frame()
    assert str(var) == ".!frame2.!frame2"


def test_create_list_of_tasks():
    var = window.create_list_of_tasks()
    assert str(var) == ".!frame2.!listbox2"


# Testing created scrollbar

def test_create_scrollbar():
    var = window.create_scrollbar()
    assert str(var) == ".!frame2.!scrollbar2"


# Testing created buttons

def test_create_add_task_button():
    var = window.create_add_task_button()
    assert str(var) == ".!frame.!button6"


def test_create_add_to_completed_button():
    var = window.create_add_to_completed_button()
    assert str(var) == ".!frame2.!button4"


def test_create_edit_task_button():
    var = window.create_edit_task_button()
    assert str(var) == ".!frame2.!button5"


def test_create_delete_button():
    var = window.create_delete_button()
    assert str(var) == ".!frame2.!button6"


def test_create_email_button():
    var = window.create_email_button()
    assert str(var) == ".!frame.!button7"


def test_create_button_for_list_of_tasks_to_do():
    var = window.create_button_for_list_of_tasks_to_do()
    assert str(var) == ".!frame.!button8"


def test_create_button_for_all_task_list():
    var = window.create_button_for_all_task_list()
    assert str(var) == ".!frame.!button9"


def test_create_button_for_completed_tasks_list():
    var = window.create_button_for_completed_tasks_list()
    assert str(var) == ".!frame.!button10"


def test_create_lists_button():
    var = window.create_lists_button()
    assert str(var) == ".!frame.!button11"


# # Testing created fields and inputs

def test_create_email_field():
    var = window.create_email_field()
    assert str(var) == ".!frame5"


def test_create_input_field():
    var = window.create_input_field()
    assert str(var) == ".!frame.!entry2"


# Testing created entry for update task

def test_create_entry_for_update_task():
    var = window.create_entry_for_update_task('sample')
    assert str(var) == ".!frame2.!frame3.!entry"


# Testing showing list of tasks

def test_show_list_of_tasks():
    var = window.show_list_of_tasks()
    assert str(var) == ".!frame2.!listbox"


# Testing is it string

def test_tasks_in_list():
    var = window.tasks_in_list()
    assert var == ''


# Testing if new task is string

def test_add_task_to_list():
    var = window.add_task_to_list()
    assert isinstance(var, str) == True


# Testing error message

def test_send_error1_box():
    error = "Email Address or Password incorrect !!! Try again. Remember you must use SMTP password for your email. Go to your email options and SET SMTP password."
    error_title = "Email validation error."
    var = window.send_error_box(error=error, error_title=error_title)
    assert str(var) == "Email Address or Password incorrect !!! Try again. Remember you must use SMTP password for your email. Go to your email options and SET SMTP password."


def test_send_error2_box():
    error = "Wrong Recipient Address !!! Try again."
    error_title = "Email validation error."
    var = window.send_error_box(error=error, error_title=error_title)
    assert str(var) == "Wrong Recipient Address !!! Try again."


def test_send_error3_box():
    error = "Something's gone wrong, try again."
    error_title = "Connect Error"
    var = window.send_error_box(error=error, error_title=error_title)
    assert str(var) == "Something's gone wrong, try again."


def test_send_error4_box():
    error = "Email account dose'nt exists"
    error_title = "Connect Error"
    var = window.send_error_box(error=error, error_title=error_title)
    assert str(var) == "Email account dose'nt exists"


# Testing pie chart label

def test_pie_chart_label():
    var = window.pie_chart_label()
    assert str(var) == ".!frame2.!label2"

# Testing update pie chart label

def test_update_pie_chart_label():
    var = window.update_pie_chart_label()
    assert str(var) == ".!frame2.!label3"

