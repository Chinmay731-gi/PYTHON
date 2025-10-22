from plyer import notification
import time

if __name__ == "__main__":
    while True:
     notification.notify(
        title="PORNHUB",
        message="Aaja bhai hilana ni hai kya aaj",
        app_name="Notification Example",
        timeout=5,
     )
     time.sleep(10)

