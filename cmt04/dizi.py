dizi1 = []
meyve1 = "Elma"
meyve2 = "Armut"
meyve3 = "Muz"
dizi2 = []
print("dizi1: ",dizi1)
print("dizi2:", dizi2)

dizi1 = [meyve3,meyve2]
dizi2 = [meyve1,meyve2]
print("dizi1:",dizi1)
print("dizi2:",dizi2)

dizi2[1] = "Kiraz"
dizi2 = dizi1+ dizi2
dizi2.append("Nar")
dizi2.insert(1,"Dut")
print("dizi1:",dizi1)
print("dizi2:",dizi2)
dizi2.pop()
print("dizi2:", dizi2)
dizi2.sort()
print("dizi2:", dizi2)
print("Eleman sayısı:",dizi2)