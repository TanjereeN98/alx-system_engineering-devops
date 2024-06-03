#!/usr/bin/python3
"""Gather data from an API"""

import requests
import sys

if __name__ == '__main__':

    response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}')
    tasks = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos')
    if response.status_code == 200:
        data = response.json()
        tasks = tasks.json()
        tasks_number = len(tasks)
        completed_tasks = []
        for task in tasks:
            if task['completed'] is True:
                task_title = task['title']
                completed_tasks.append(task_title)
        print(
            f"Employee {data['name']} is done with tasks"
            f"({len(completed_tasks)}/{tasks_number}):")
        print('\n'.join('\t' + task for task in completed_tasks))
