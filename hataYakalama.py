while True:
    try:
        sayi=int(input("Sayı giriniz: "))
        sayi2=int(input("2. Sayıyı giriniz: "))
        bolme=sayi/sayi2
        print("Sonuc: ",bolme)
    except ZeroDivisionError:
        print("Sayı Sıfıra Bölünemez. 2. Sayıyı Kontrol Ediniz")
    except ValueError:
        print("Sayısal Değer Girmediniz. Verileri Kontrol Ediniz.")




#finally:
#    print("program sona erdi")
#ZeroDivisionError - sıfıra bölünme hatası
#ValueError - değişken tanımı hatası