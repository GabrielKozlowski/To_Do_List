# import os, sys
# import matplotlib


# # Add path to main file application 
# current = os.path.dirname(os.path.realpath(__file__))
# parent = os.path.dirname(current)
# sys.path.append(parent)

# # Import class from main 
# from src.app.main import ToDoList


# matplotlib.use('Agg')



# def test_test_():
#     a = 12
#     assert a == 122

# def test_now():
#     print(56)
#     a = ToDoList().create_options_frame()
#     assert str(a) == '2'


# # Testing created frame in program

# def test_create_options_frame():
#     var = ToDoList().create_options_frame()
#     assert str(var) == '.!frame3'


# def test_create_tasks_frame():
#     var = ToDoList().create_tasks_frame()
#     assert str(var) == ".!frame3"


# def test_update_frame():
#     var = ToDoList().create_update_frame()
#     assert str(var) == ".!frame2.!frame"


# def test_create_list_of_tasks():
#     var = ToDoList().create_list_of_tasks()
#     assert str(var) == ".!frame2.!listbox2"


# # Testing created scrollbar
# def test_create_scrollbar():
#     var = ToDoList().create_scrollbar()
#     assert str(var) == ".!frame2.!scrollbar2"


# # Testing created buttons

# def test_create_add_task_button():
#     var = ToDoList().create_add_task_button()
#     assert str(var) == ".!frame.!button6"


# def test_create_add_to_completed_button():
#     var = ToDoList().create_add_to_completed_button()
#     assert str(var) == ".!frame2.!button4"


# def test_create_email_button():
#     var = ToDoList().create_email_button()
#     assert str(var) == ".!frame.!button6"

# def test_create_button_for_list_of_tasks_to_do():
#     var = ToDoList().create_button_for_list_of_tasks_to_do()
#     assert str(var) == ".!frame.!button6"


# def test_create_button_for_all_task_list():
#     var = ToDoList().create_button_for_all_task_list()
#     assert str(var) == ".!frame.!button6"


# def test_create_button_for_completed_tasks_list():
#     var = ToDoList().create_button_for_completed_tasks_list()
#     assert str(var) == ".!frame.!button6"


# def test_create_lists_button():
#     var = ToDoList().create_lists_button()
#     assert str(var) == ".!frame.!button6"


# # Testing created fields and inputs

# def test_create_email_field():
#     var = ToDoList().create_email_field()
#     assert str(var) == ".!frame2.!frame"


# def test_create_input_field():
#     var = ToDoList().create_input_field()
#     assert str(var) == ".!frame.!entry2"



# # Testing created entry for update task
# def test_create_entry_for_update_task():
#     var = ToDoList().create_entry_for_update_task('sample')
#     assert str(var) == ".!frame2.!frame.!entry"


# # Testing showing list of tasks
# def test_show_list_of_tasks():
#     var = ToDoList().show_list_of_tasks()
#     assert str(var) == ".!frame2.!listbox"


# # Testing is it string
# def test_tasks_in_list():
#     var = ToDoList().tasks_in_list()
#     assert var == ''