#!/usr/bin/python3
"""
Records task data of all employees and exports it to json

USAGE: 3-dictionary_of_list_of_dictionaries.py
"""

from requests import get
import json


if __name__ == "__main__":
    tasks = []
    tasks_json = {}
    BASE_URL = "https://jsonplaceholder.typicode.com"

    with get(BASE_URL + "/users/") as response:
        users = response.json()
        for user in users:
            tasks = []
            with get(BASE_URL + f"/todos?userId={user['id']}") as todos:
                todos = todos.json()
                for task in todos:
                    tasks.append({
                        "username": user['username'],
                        "task": task['title'],
                        "completed": task['completed']
                    })
            tasks_json.update({user['id']: tasks})

    with open("todo_all_employees.json", 'w', newline='') as f:
        json.dump(tasks_json, f)
