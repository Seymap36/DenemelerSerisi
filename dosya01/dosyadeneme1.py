#not1=5
#with open("sayilar.txt", "a") as dosyaac:
#    for a in range(10):
#        dosyaac.write(f"\n{a}")

#try:
#    okunan = open("sayilar.txt", "r")
#    print(okunan.read())
#    okunan.close()
#except:
#    print("Bir hata oluştu")


okunan = open("sayilar.txt", "r")
a = okunan.read(5)
b = okunan.read(6)
print(b,a)
okunan.close()
