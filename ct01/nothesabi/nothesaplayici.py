def harfnotu():
    print("Not Hesaplayıcı")
    notum = int(input ("notum nedir?"))
    if notum>100 or notum<0: print("Yanlış girdiniz, sayı '0-100' olmalıdır.")
    else:
        if notum > 90 : print ("Notun AA")
        elif notum > 80 : print ("Notun BA")
        elif notum > 70 : print ("Notun BB")
        elif notum > 60 : print ("Notun CC")
        elif notum >= 50 : print ("Notun DD")
        elif notum < 50 : print ("KALDINIZ!")
        if notum >50 and notum<70 : print("Harikasın Doja")
        
