from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar"]

flow = InstalledAppFlow.from_client_secrets_file(
    "credentials.json",
    SCOPES
)

creds = flow.run_local_server(port=0)

service = build(
    "calendar",
    "v3",
    credentials=creds
)

# print("Connected to Google Calendar successfully!")

events = service.events().list(
    calendarId="primary"
).execute()

# print(events)

for event in events["items"]:
    print("Title:", event.get("summary"))

    start = event.get("start", {})
    end = event.get("end", {})

    start_time = start.get("dateTime") or start.get("date")
    end_time = end.get("dateTime") or end.get("date")

    print("Start:", start_time)
    print("End:", end_time)
    print("-" * 30)