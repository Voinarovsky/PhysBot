import datetime
nowdate = datetime.datetime.today().weekday()
print((datetime.datetime.today().isocalendar().week + 1) % 2)