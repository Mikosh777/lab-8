import requests

# 1.1: GET Request
post_id = 1 
response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{post_id}")

if response.status_code >= 400:
    print(f"Error: {response.status_code} - {response.text}")
else:
    print("Response content:")
    print(response.json())

# 1.2: Create a ToDo class
class ToDo:
    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed

# 1.3: Create a new object of class ToDo
new_todo = ToDo(userId=1, id=post_id, title="Sample Title", completed=False)
