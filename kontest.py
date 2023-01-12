import requests
from datetime import datetime

class contest:
  def __init__(self,name,start,end,url):
    self.name = name
    self.start =start
    self.end = end
    self.url = url


def get_contests(site):
  url = f"https://kontests.net/api/v1/{site}"
  response = requests.get(url)
  contests = []
  keywords = ["Starters","Codeforces","Beginner","Regular"]
  if response.json() is not None and response.status_code == 200:
    contest_arr = response.json()
    for contest_data in  contest_arr:
      name = contest_data["name"]
      url = contest_data["url"]
      start = contest_data["start_time"]
      end = contest_data["end_time"]
      contest_obj = contest(name,start,end,url)
      for keyword in keywords:
        if keyword in name:
          contests.append(contest_obj)
          break

  return contests