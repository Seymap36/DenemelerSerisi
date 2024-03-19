import hesaplar.hesapmakinesi
import nothesabi.nothesaplayici
import cizimler.cizim
import burcogrenme.burc

def ANAMENU():
    print("╔═════════════════════╗")
    print("║      ANA MENU       ║")
    print("║                     ║")
    print("║  1-HESAP MAK        ║")
    print("║  2-KM HESAP         ║")
    print("║  3-Cizim            ║")
    print("║  4-Not hesabı       ║")
    print("║  5-Burc Ogrenme     ║")
    print("║  ç-çıkış            ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    seçim = input()
    if seçim == "1" :
        hesaplar.hesapmakinesi.hmmenu()
    if seçim == "3" :
        cizimler.cizim.cizimlermenu()
        ANAMENU()
    if seçim == "ç" or seçim=="ç": exit()
    if seçim == "4":
        nothesabi.nothesaplayici.harfnotu()
        ANAMENU()
    if seçim == "5" :
        burcogrenme.burc.burcmenu()
        ANAMENU()
    else: 
        print("Seçim sadece 1,2,4,5,ç olabilir.")
        ANAMENU()

ANAMENU()
