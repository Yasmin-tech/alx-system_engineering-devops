#!/usr/bin/python3
"""export in json format the user and all their tasks"""

import json
import requests
import sys

if __name__ == "__main__":
    USER_ID = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(USER_ID)).json()
    user_name = user.get("username")

    todos = requests.get(url + "todos", params={"userId": USER_ID}).json()

    list_tasks = []
    for task in todos:
        task_dict = {}
        task_dict["task"] = task.get("title")
        task_dict["completed"] = task.get("completed")
        task_dict["username"] = user_name
        list_tasks.append(task_dict)

    dict_ = {str(USER_ID): list_tasks}

    filename = f"{USER_ID}.json"
    with open(filename, "w") as f:
        json.dump(dict_, f)
