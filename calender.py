import google_api

service = google_api.get_service()

def add_event(name,start,end,url):
  event = {
    'summary': name,
    'description': url,
    'colorId':"11",
    'start': {
      'dateTime': start,
      'timeZone': 'Asia/Kolkata',
    },
    'end': {
      'dateTime': end,
      'timeZone': 'Asia/Kolkata',
    },
    'attendees': [
      {'email': 'i4irfan777@gmail.com.com'},
    ],
    'reminders': {
      'useDefault': False,
      'overrides': [
        {'method': 'email', 'minutes': 24 * 60},
        {'method': 'popup', 'minutes': 30},
        {'method': 'popup', 'minutes': 5},
      ],
    },
  }
  event = service.events().insert(calendarId='primary', body=event).execute()

def list_event_urls(start,end):
  response = service.events().list(calendarId='primary',timeMin=start,timeMax=end,showDeleted=False).execute() 
  if "items" in response:
    urls = [item["description"] for item in response["items"]]
    return urls