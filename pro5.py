# import time
# from plyer import notification

# while True:
#     print("Please sip some water ! ")
#     notification.notify(title="Please drink some water",
#                         message="You need to drink some water")
#     time.sleep(3)

'''it will not work on mac but it will run on windows which definately helpy and remind you to be hydrated'''

'''for mac'''

import time 
from pync import Notifier
while True:
    title="notification"
    message="PLEASE DRINK WATER!"
    Notifier.notify(f"{message},{title}")
    time.sleep(3600)