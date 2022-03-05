from datetime import datetime as dt
now=dt.now()
print("current datetime=",now)
s=now.strftime("%a %m %y")
print(s)