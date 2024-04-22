#!/usr/bin/python3
"""export data in the CSV format.

From https://jsonplaceholder.typicode.com/ REST API
about the given employee id and their task titel and status
"""
import csv
import requests
import sys


def employee_tasks_info(EMPLOYEE_ID):
    """request an employee data and task information from

    https://jsonplaceholder.typicode.com/
    REST API
    and save in csv format
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
    data = []  # this is the data that should be written to json file

    for task in response2_dict:
        user_id = task.get("userId", -1)
        if user_id == int(EMPLOYEE_ID):
            data.append(
                    {
                        "user_id": str(EMPLOYEE_ID),
                        "user_name": str(EMPLOYEE_NAME),
                        "task_compeleted_status": str(task.get("completed")),
                        "task_title": str(task.get("title"))
                    })

    # Specify the field names
    fieldnames = [
            "user_id", "user_name", "task_compeleted_status", "task_title"
            ]

    file_name = f'{EMPLOYEE_ID}.csv'
    # open a csv file for writing the fieldnames and get a writing object
    with open(file_name, "w", newline="") as csvfile:
        writer = csv.DictWriter(
                csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

        # uncommit this if you want the headers to be included in the csv file
        # writer.writeheader()

        # write the data with write object and the writenow function
        for row in data:
            writer.writerow(row)


if __name__ == "__main__":
    EMPLOYEE_ID = sys.argv[1]
    employee_tasks_info(EMPLOYEE_ID)
