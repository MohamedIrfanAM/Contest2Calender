import calender
import kontest

def main():
  sites = ["codeforces","at_coder","code_chef"]
  contests = []
  for site in sites:
    contests.extend(kontest.get_contests(site))
  
  for contest in contests:
    duplicate = False
    urls = calender.list_event_urls(contest.start,contest.end)
    for url in urls:
      if contest.url == url:
        duplicate = True
        break
    if not duplicate:
      print(contest.name)
      calender.add_event(contest.name,contest.start,contest.end,contest.url)

if __name__ == '__main__':
    main()