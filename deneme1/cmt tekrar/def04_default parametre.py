def topla(aa,bb=0):
    return aa+bb
def carp(x,yy):
    return x*yy


#sayi1 = int(input("Birinci sayı nedir?"))
#sayi2 = int(input("İkinci sayı nedir?"))
sayi1 = 8
sayi2 = 7
print (topla(sayi1))
print (topla(sayi1,sayi2))
print (f"Toplam:{topla(sayi1,sayi2)}")
print (topla(sayi1,topla(8,sayi1)))
print (carp(sayi1,sayi2))
print (f"Carpma:{carp(sayi1,sayi2)}")
