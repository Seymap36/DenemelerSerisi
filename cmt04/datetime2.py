import datetime,random
bugun = datetime.datetime.now().strftime("%d/%m/%Y %H:%H:%S")
yil = int(datetime.datetime.now().strftime("%Y"))
ay = int(datetime.datetime.now().strftime("%m"))
gun = int(datetime.datetime.now().strftime("%d"))
print("Tarih saat=",bugun)
#dgunu = input("Dogum tarihin nedir? (01.01.1999 gibi yaz)")
dgunu="02.02.2023"
print(dgunu)
dyil = int(dgunu[6:10])
day1 = int(dgunu[3:5])
dgun = int(dgunu[0:2])
print(dyil,day1,dgun)


yyil = 0
if ay>day1:
    yyil = yil-dyil
    print("yaşadığın yıl:", yyil)
else:
    yyil = yil-dyil-1
    print("yaşadığın yıl:", yyil)

print("yaşadığın gün:",yyil*365)
