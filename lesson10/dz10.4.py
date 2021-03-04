import time
from datetime import datetime

while True:
    try:
        time.sleep(2)
        now = datetime.now()
        print(now.strftime("%X"))
    except KeyboardInterrupt:
        print("stopped")
        break