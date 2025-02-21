#!/usr/bin/python3
"""Get TODO list progress for a given employee"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])  # Ensure input is an integer
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print("Error: Employee not found")
        sys.exit(1)

    user = user_response.json()
    employee_name = user.get("name")

    # Fetch TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)

    if todos_response.status_code != 200:
        print("Error: Unable to fetch TODO list")
        sys.exit(1)

    todos = todos_response.json()
    done_tasks = [task for task in todos if task["completed"]]
    total_tasks = len(todos)
    number_of_done_tasks = len(done_tasks)

    # Print output
    print(f"Employee {employee_name} is done with tasks ({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")


