#!/usr/bin/python3
"""Export to JSON"""

import json
import requests
import sys

if __name__ == '__main__':

    user_id = sys.argv[1]
    response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}')
    tasks = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')
    if response.status_code == 200:
        data = response.json()
        tasks = tasks.json()
        user_name = data['username']
        with open(f'{user_id}.json', 'w', newline='') as file:
            json.dump({f"{user_id}": [
                {
                    "task": f"{task['title']}",
                    "completed": task.get("completed"),
                    "username": f"{data['username']}"
                } for task in tasks
            ]},
                file)
