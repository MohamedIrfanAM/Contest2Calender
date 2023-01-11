import requests
from datetime import datetime

url = "https://codeforces.com/api/contest.list"
class contest:
  def __init__(self,name,date,duration):
    self.name = name
    self.date = date
    self.duration = duration


def get_contests():
  response = requests.get(url)
  if response.json() is not None and response.status_code == 200:
    contests = []
    for contest_data in response.json()["result"]:
      date = datetime.utcfromtimestamp(int(contest_data["startTimeSeconds"]))
      duration = int(contest_data["durationSeconds"]/3600)
      contest_obj = contest(contest_data["name"],date,duration)
      contests.append(contest_obj)
    return contests