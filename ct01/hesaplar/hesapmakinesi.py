import hesaplar.toplama
import hesaplar.cikarma
import hesaplar.carpma
import hesaplar.bolme
import hesaplar.yuzde
def hmmenu():
    print("╔═════════════════════╗")
    print("║HESAP MAKİNESİ       ║")
    print("║                     ║")
    print("║  1-Toplama          ║")
    print("║  2-Çıkarma          ║")
    print("║  3-Çarpma           ║")
    print("║  4-Bölme            ║")
    print("║  5-Yüzde Hesap      ║")
    print("║  6-anamenudon       ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    secim = input ()

    if secim == "1" :
        hesaplar.toplama.toplamamenu ()
        hmmenu ()
    if secim == "2" : 
        hesaplar.cikarma.cikarmamenu ()
    if secim == "3" :
        hesaplar.carpma.carpmamenu ()
    if secim == "4" : 
        hesaplar.bolme.bolmemenu ()
    if secim == "5" : 
        hesaplar.yuzde.yuzdemenu ()
    
        

