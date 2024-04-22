#!/usr/bin/python3
"""export in json format all users and all their tasks"""

import json
import requests
import sys

if __name__ == "__main__":

    users = requests.get("https://jsonplaceholder.typicode.com/users").json()

    list_tasks = []
    dict_users = {}
    dict_task = {}

    for user in users:
        user_id = user.get("id")
        todos = requests.get(
                "https://jsonplaceholder.typicode.com/todos",
                params={"userId": user_id}).json()
        list_tasks = []
        for task in todos:
            dict_task = {}
            dict_task["username"] = user.get("username")
            dict_task["task"] = task.get("title")
            dict_task["completed"] = task.get("completed")
            list_tasks.append(dict_task)
        dict_users[user_id] = list_tasks

    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(dict_users, f)
