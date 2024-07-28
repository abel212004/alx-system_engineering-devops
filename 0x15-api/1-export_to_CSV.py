#!/usr/bin/python3
"""
gathers employee data from api and exports it to csv file
USAGE: 1-export_to_CSV.py $EMPLOYEE_ID
"""

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    USER_ID = argv[1]
    USERNAME = ""
    TASKS = []
    BASE_URL = "https://jsonplaceholder.typicode.com"

    with get(BASE_URL + "/users/" + USER_ID) as response:
        response = response.json()
        USERNAME = response['username']

    with get(BASE_URL + "/todos?userId=" + USER_ID) as response:
        response = response.json()
        for task in response:
            TASKS.append([USER_ID, USERNAME, task['completed'], task['title']])

    with open(USER_ID + '.csv', 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in TASKS:
            writer.writerow(task)
