#!/usr/bin/python3
from sys import argv
import requests
import csv


def appeler_api():

    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(argv[1]))
    task = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(argv[1]))

    if user.status_code == 200 and task.status_code == 200:
        user_data = user.json()
        tasks_data = task.json()


        with open(f'{argv[1]}.csv', mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)

            for task in tasks_data:
                row = [argv[1], user_data["username"], str(task["completed"]), task["title"]]
                writer.writerow(row)
                # Vous pouvez également stocker les données dans TASK_TITLE si vous en avez besoin ultérieurement.



if __name__ == '__main__':
    appeler_api()
