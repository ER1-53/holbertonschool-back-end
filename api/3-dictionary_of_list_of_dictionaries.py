#!/usr/bin/python3
"""export information to json file"""
import json
import requests


def appeler_api():
    """create a json file with data"""
    users = requests.get("https://jsonplaceholder.typicode.com/users")

    if users.status_code == 200:
        user_data = users.json()

        my_dict = {}
        url = "https://jsonplaceholder.typicode.com/users"
        for user in user_data:
            tasks = requests.get(
                "{}/{}/todos".format(url, user['id']))

            if tasks.status_code == 200:
                tasks_data = tasks.json()

                my_dict[user["id"]] = []
                for task in tasks_data:
                    dict_all = {
                        "username": user["username"],
                        "task": task["title"],
                        "completed": task["completed"]
                    }
                    my_dict[user["id"]].append(dict_all)

        with open("todo_all_employees.json", 'w') as json_file:
            json.dump(my_dict, json_file, indent=2)


if __name__ == '__main__':
    appeler_api()
