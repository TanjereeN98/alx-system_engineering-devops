#!/usr/bin/python3
"""Export to CSV"""

import csv
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    user = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}').json()
    tasks = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')
    user_name = user['username']
    if tasks.status_code == 200:
        with open(f'{sys.argv[1]}.csv', 'w') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for task in tasks.json():
                writer.writerow(
                    [user_id, user_name, task['completed'], task['title']])
