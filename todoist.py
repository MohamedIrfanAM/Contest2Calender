from todoist_api_python.api import TodoistAPI
import requests
from uuid import uuid4
import json

with open("todoist_token.json", "r") as f:
    todoist_json = json.load(f)

TOKEN = todoist_json["TOKEN"]
api = TodoistAPI(TOKEN)
inboxID = todoist_json["inboxID"]
projectID = todoist_json["projectID"]
sectionID = todoist_json["sectionID"]

def move_task(task_id: str,destination: str) -> bool:
    if destination == "section_id":
      ID = sectionID
    elif destination == 'project_id':
      ID = projectID
    body = {
        "commands": [
            {
                "type": "item_move",
                "args": {"id": task_id, destination: ID},
                "uuid": uuid4().hex,
            },
        ],
    }
    response = requests.post(
        "https://api.todoist.com/sync/v9/sync",
        headers={"Authorization": f"Bearer {TOKEN}"},
        json=body,
    )
    return response.ok


def move():
  keywords = ["Starters","Codeforces","Beginner","Regular"]
  try:
      tasks = api.get_tasks(project_id = inboxID)
      for task in tasks:
        task_id = str(task.id)
        task_name = str(task.content)
        if len(task.labels) == 1:
          task_label = str(task.labels[0])
          if task_label == "GCal":
            for keyword in keywords:
              if keyword in task_name:
                print(task_name)
                move_task(task_id,"project_id")
                move_task(task_id,"section_id")

  except Exception as error:
      print(error)