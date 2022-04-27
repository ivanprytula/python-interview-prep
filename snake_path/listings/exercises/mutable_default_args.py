import time
from datetime import datetime


# NB: if use now() we'll get the same time even after sleep for 1 sec
# def display_time(start_time=datetime.now()):
def display_time(start_time=None):
    if start_time is None:
        start_time = datetime.now()
    print(start_time.strftime('%B %d, %Y %H:%M:%S'))


display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()

# def add_employee(employee, employees_list=None):
#     if employees_list is None:
#         employees_list = []
#     employees_list.append(employee)
#     print(employees_list)
#
#
# main_employees = ['John', 'Dave']
#
# add_employee('Corey', main_employees)
# add_employee('Jack', main_employees)
# add_employee('Cris')
# add_employee('Rebecca')
