import time
menu = 1
while menu != 0 :
    secim = int(input("[1] saniye,[2] dakika,[3] programı kapat"))
    if secim == 1 :
        kac = int(input("kaç saniye"))
        while kac != 0 :
            print(kac , "saniye kaldı")
            time.sleep(1)
            kac = kac - 1
        print("zaman doldu")
    elif secim == 2 :
        kacdk = int(input("kaç dakika"))
        kac = kacdk*60
        while kac != 0 :
            print (kac,"saniye kaldı")
            time.sleep(1)
            kac = kac-1
        print("zaman doldu")
    elif secim == 3 :
          print("made by s0nguras")
          print("Program sonlandırıldı")
          time.sleep(1)
          raise SystemExit()
