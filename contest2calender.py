import calender
import kontest
import todoist
from time import sleep
import logging
import sys

logging.basicConfig(
        level=logging.DEBUG, 
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
        datefmt='%d/%m/%Y %H:%M:%S' ,     
        handlers=[
        logging.FileHandler("contest2calender.log",'w'),
        logging.StreamHandler(sys.stdout),
    ])
logger = logging.getLogger()

def main():
  sites = ["codeforces","at_coder","code_chef"]
  contests = []
  for site in sites:
    logger.info(f"Getting available contest for {site}")
    contests.extend(kontest.get_contests(site))
  
  for contest in contests:
    duplicate = False
    logger.info(f"Checking if {contest.name} already exist")
    urls = calender.list_event_urls(contest.start,contest.end)
    for url in urls:
      if contest.url == url:
        duplicate = True
        break
    if not duplicate:
      print(contest.name)
      logger.info(f"{contest.name} not found in calender, adding to calender")
      calender.add_event(contest.name,contest.start,contest.end,contest.url)
  logger.info("All contest are added to calender")
  sleep(30)
  logger.info("Moving todoist inbox tasks to projects/cp")
  todoist.move()

if __name__ == '__main__':
    main()