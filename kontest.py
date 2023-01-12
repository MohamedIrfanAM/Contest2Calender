import requests
import datetime

class contest:
  def __init__(self,name,start,end,url):
    self.name = name
    self.start =start
    self.end = end
    self.url = url

def get_date(date_string):
  if(date_string[10] == 'T'):
    date = datetime.datetime.strptime(date_string,"%Y-%m-%dT%H:%M:%S.000Z")
  else:
    date = datetime.datetime.strptime(date_string,"%Y-%m-%d %H:%M:%S UTC")
  date += datetime.timedelta(hours=5,minutes=30)
  date_string = date.strftime("%Y-%m-%dT%H:%M:%S+05:30")
  return date_string

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
      start = get_date(contest_data["start_time"])
      end = get_date(contest_data["end_time"])
      contest_obj = contest(name,start,end,url)
      for keyword in keywords:
        if keyword in name:
          contests.append(contest_obj)
          break

  return contests