import turtle 
def ucgen():
    for abc in range(3):
        turtle.forward(100)
        turtle.right(120)

def kare():
    for a in range(4):
        turtle.forward(100)
        turtle.right(90)
def cizimlermenu():
    print("╔═══════════════════════════════════╗")
    print("║        Cizimler                   ║")
    print("║ 1-ucgen                           ║")
    print("║ 2-kare                            ║")
    print("║ 3-                                ║")
    print("║ 4-                                ║")
    print("║          Seçiminiz Nedir?         ║")
    print("╚═══════════════════════════════════╝")

secim = input()
if secim == "1" : ucgen()
if secim == "2" : kare()