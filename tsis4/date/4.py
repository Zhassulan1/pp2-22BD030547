from datetime import datetime, timedelta

now=datetime.now().replace(microsecond=0)
day = timedelta(1)
t = now - day
difference = now - t
print(difference.total_seconds())
