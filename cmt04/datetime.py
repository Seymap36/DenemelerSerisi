#from datetime import datetime
#print("Bugün:",datetime.date.today())
#print("şimdi=", datetime.now())


import datetime, random
print("Tarih saat=", datetime.datetime.now().strftime("%d/%m/%y %H:%H:%S"))
print("Tarih saat=", datetime.datetime.now().strftime("%Y"))
a = datetime.datetime.now().strftime("%y")
b = datetime.datetime.now().strftime("%m")
c = datetime.datetime.now().strftime("%d")
yil = int(a)+random.randint(1,5)
ay = int(b)+random.randint(1,9)
gun = int(c)+random.randint(1,7)
print(yil,ay,gun)


