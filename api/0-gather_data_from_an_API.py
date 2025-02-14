#!/usr/bin/python3
"""get TODO list"""

import json
import requests
import sys
if __name__ == "__main__":
    link = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    res = requests.get(link)
    user = json.loads(res.text)
    num = sys.argv[1]
    link = "https://jsonplaceholder.typicode.com/users/{}/todos".format(num)
    res = requests.get(link)
    todos = json.loads(res.text)
    done = []
    for i in todos:
        if i['completed']:
            done.append(i)
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for k, v in tasks.items():
        if v is True:
            print("\t {}".format(k))