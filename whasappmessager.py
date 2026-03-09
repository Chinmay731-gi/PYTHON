from twilio.rest import Client
from datetime import datetime
import time
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

def sendwpsmessage(message_body, recipient_number):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print("Message sent:", message.sid)
    except Exception as e:
        print(f"An error occurred: {e}")

name = input("Enter recipient name: ").strip()
recipient_number = input("Enter recipient number with country code: ").strip()
message_body = input(f"Enter the message you want to send to {name}: ").strip()

date_str = input("Enter the date to send the message (YYYY-MM-DD): ").strip()
time_str = input("Enter the time to send the message (HH-MM IN 24 hours format): ").strip()

sch_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
current_datetime = datetime.now()
delay_sec = (sch_datetime - current_datetime).total_seconds()

if delay_sec <= 0:
    print("Time has passed, please enter a future date and time")
else:
    print(f"Message scheduled to be sent to {name} at {sch_datetime}.")
    time.sleep(delay_sec)
    sendwpsmessage(message_body, recipient_number)