#!/usr/bin/python3
"""
gathers employee data from an api and exports it to json file
USAGE: 2-export_to_JSON.py $EMPLOYEE_ID
"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":
    USER_ID = argv[1]
    USERNAME = ""
    BASE_URL = "https://jsonplaceholder.typicode.com"
    tasks = []

    with get(BASE_URL + "/users?id=" + USER_ID) as response:
        response = response.json()[0]
        USERNAME = response['username']

    with get(BASE_URL + "/todos?userId=" + USER_ID) as response:
        response = response.json()
        for task in response:
            tasks.append(
                {
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": USERNAME
                }
            )

    with open(USER_ID + ".json", 'w', newline='') as f:
        json.dump({USER_ID: tasks}, f)
