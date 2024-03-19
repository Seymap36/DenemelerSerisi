def burcmenu():
    gun = int(input("Doğum gününüzü girin: "))
    ay = int(input("Doğum ayınızı girin: "))
    yil = int(input("Doğum yılınızı girin: "))

    # Burçları temsil eden tarih aralıklarını tanımla
    burclar = [
        ("Kova", 20, 1, 19, 2),
        ("Balık", 20, 2, 20, 3),
        ("Koç", 21, 3, 20, 4),
        ("Boğa", 21, 4, 20, 5),
        ("İkizler", 21, 5, 21, 6),
        ("Yengeç", 22, 6, 22, 7),
        ("Aslan", 23, 7, 23, 8),
        ("Başak", 24, 8, 23, 9),
        ("Terazi", 24, 9, 23, 10),
        ("Akrep", 24, 10, 22, 11),
        ("Yay", 23, 11, 21, 12),
        ("Oğlak", 22, 12, 20, 1)
    ]

    # Doğum tarihine göre burcu bul
    for burc, baslangic_gunu, baslangic_ayi, bitis_gunu, bitis_ayi in burclar:
        if (ay == baslangic_ayi and gun == baslangic_gunu):
            print("Burcunuz:", burc)