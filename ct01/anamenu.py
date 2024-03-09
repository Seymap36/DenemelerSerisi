import hesapmak.hm
import nothesabi.nothesaplayici

def ANAMENU():
    print("╔═════════════════════╗")
    print("║      ANA MENU       ║")
    print("║                     ║")
    print("║  1-HESAP MAK        ║")
    print("║  2-KM HESAP         ║")
    print("║  3-                 ║")
    print("║  4-Not hesabı       ║")
    print("║  ç-çıkış            ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    seçim = input()
    if seçim == "1" :
        hesapmak.hm.hmmenu()
        ANAMENU()
    if seçim == "ç" or seçim=="ç": exit()
    if seçim == "4":
        nothesabi.nothesaplayici.harfnotu()
        ANAMENU()
    else: 
        print("Seçim sadece 1,2,4,ç olabilir.")
        ANAMENU()

ANAMENU()
