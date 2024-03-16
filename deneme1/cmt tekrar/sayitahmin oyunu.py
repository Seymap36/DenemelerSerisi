import random
bas = 1
son = 100
hak = 5
tutulan = random.randint(bas,son)
print(tutulan)
print(f"Ben {bas} ile {son} arası bir sayı tuttum.")
print(f"{hak} hakkın var.")

for xx in range(hak):
    tahmin = int(input("tahminin nedir?"))
    if tahmin == tutulam:
        print("Bildin.")
        break
    elif tahmin > tutulan:
        print("Tahmin büyük.")
        tahmin = int(input("Tahminin nedir?"))
    elif tahmin < tutulan:
        print("tahminin küçük")
        tahmin = int(input("Tahmin nedir?"))