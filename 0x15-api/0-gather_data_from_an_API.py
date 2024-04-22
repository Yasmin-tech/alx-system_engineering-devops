#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


EMPLOYEE_ID = sys.argv[1]


def employee_tasks_info(EMPLOYEE_ID):
    """request an employee data and task information from

    https://jsonplaceholder.typicode.com/
    REST API
    """

    # response1 to get the employee name
    # response2 to get all the todos
    response1 = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".format(EMPLOYEE_ID)
            )
    response2 = requests.get(
            "https://jsonplaceholder.typicode.com/todos".format(EMPLOYEE_ID)
            )

    employee = response1.json()
    EMPLOYEE_NAME = employee.get("name")

    response2_dict = response2.json()
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    list_done_tasks = []

    for task in response2_dict:
        user_id = task.get("userId", -1)
        if user_id == int(EMPLOYEE_ID):
            if task.get("completed") is True:
                NUMBER_OF_DONE_TASKS += 1
                TOTAL_NUMBER_OF_TASKS += 1
                list_done_tasks.append(task.get("title"))
            else:
                TOTAL_NUMBER_OF_TASKS += 1

    print(
        f'Employee {EMPLOYEE_NAME} is done with tasks'
        f'({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):'
    )
    for task in list_done_tasks:
        print("\t", task)


if __name__ == "__main__":
    employee_tasks_info(EMPLOYEE_ID)
