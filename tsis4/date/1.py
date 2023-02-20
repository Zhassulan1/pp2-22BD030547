from datetime import datetime, timedelta
 
t1 = datetime.now()
t2 = timedelta(5)
t3 = t1 - t2
print(t3.strftime("%d-%m-%y"))
