from datetime import datetime, timedelta

t1 = datetime.now()
day = timedelta(1)
print((t1 - day).strftime("%d-%m-%y"))
print(t1.strftime("%d-%m-%y"))
print((t1 + day).strftime("%d-%m-%y"))
