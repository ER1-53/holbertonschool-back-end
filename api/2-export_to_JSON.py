#!/usr/bin/python3
""" export information to json file"""
import json
import requests
from sys import argv


def appeler_api():
    """ create a json file with data"""
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1]))
    task = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(argv[1]))

    if user.status_code == 200 and task.status_code == 200:
        user_data = user.json()
        tasks_data = task.json()

    my_dict = {argv[1]: []}
    for task in tasks_data:
        dict_all = {"task": task["title"],
                    "completed": task["completed"],
                    "username": user_data["username"]
                    }

        my_dict[argv[1]].append(dict_all)

    with open("{}.json".format(argv[1]), 'w') as json_file:
        json.dump(my_dict, json_file, indent=2)


if __name__ == '__main__':
    appeler_api()
