#!/usr/bin/python3
"""
This module fetches all employees' TODO list data from a REST API and
exports the data in JSON format.
"""

import json
import requests


def get_all_employees_todo_data():
    """Fetch all employee tasks and export them in JSON format."""
    try:
        users = requests.get("https://jsonplaceholder.typicode.com/users").json()
        todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    except requests.RequestException as e:
        print(f"Error: Unable to fetch data - {e}")
        return

    tasks_by_user = {
        user["id"]: [
            {"username": user["username"], "task": task["title"], "completed": task["completed"]}
            for task in todos if task["userId"] == user["id"]
        ]
        for user in users
    }

    filename = "todo_all_employees.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(tasks_by_user, file, indent=4)

    print(f"Data successfully saved to {filename}")


if __name__ == "__main__":
    get_all_employees_todo_data()