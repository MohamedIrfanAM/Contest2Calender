import calender
import kontest
import datetime

def get_date(date_string):
  if(date_string[10] == 'T'):
    date = datetime.datetime.strptime(date_string,"%Y-%m-%dT%H:%M:%S.000Z")
  else:
    date = datetime.datetime.strptime(date_string,"%Y-%m-%d %H:%M:%S UTC")
  date += datetime.timedelta(hours=5,minutes=30)
  date_string = date.strftime("%Y-%m-%dT%H:%M:%S+05:30")
  return date_string

def main():
  sites = ["codeforces","at_coder","code_chef"]
  contests = []
  for site in sites:
    contests.extend(kontest.get_contests(site))
  
  for contest in contests:
    calender.add_event(contest.name,get_date(contest.start),get_date(contest.end),contest.url)

if __name__ == '__main__':
    main()