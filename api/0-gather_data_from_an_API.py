#!/usr/bin/python3
""" get api data """
import requests
from sys import argv


def appeler_api():
    """ api function call """
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(argv[1]))
    task = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(argv[1]))

    if user.status_code == 200 and task.status_code == 200:
        user_data = user.json()
        tasks_data = task.json()

        EMPLOYEE_NAME = user_data["name"]
        TOTAL_NUMBER_OF_TASKS = len(tasks_data)
        NUMBER_OF_DONE_TASKS = 0
        TASK_TITLE = []
        print("Employee {} is done with tasks ({}/{}):".format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
        for task in tasks_data:
            if task["completed"] == True:
                NUMBER_OF_DONE_TASKS += 1
                print("\t {}".format(task["title"]))


if __name__ == '__main__':
    appeler_api()
