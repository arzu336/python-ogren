def not_hesapla(satir):
    satir = satir.strip()  # Satırdaki boşlukları temizle
    liste = satir.split(':')
    isim = liste[0]
    notlar = liste[1].split(',')
    notlar = [int(n) for n in notlar]
    ortalama = sum(notlar) / len(notlar)
    

    if ortalama==100:
        print('AA')
    elif ortalama<100 and ortalama>80:
        print('BA')
    else:
        print('CC')      

def not_gir():
    ad = input("Ad: ")
    soyad = input("Soyad: ")
    not1 = int(input("1. Not: "))
    not2 = int(input("2. Not: "))
    not3 = int(input("3. Not: "))
    
    with open("sinav_notlari.txt", "a", encoding='utf-8') as file:
        file.write(f"{ad} {soyad}:{not1},{not2},{not3}\n")

def ortalama_oku():
    with open("sinav_notlari.txt", "r", encoding='utf-8') as file:
        for satir in file:
            not_hesapla(satir)

def kaydet():
    pass

while True:
    islem = input("1- Notları oku\n2- Not gir\n3- Kayıt et\n4- Çıkış\n")

    if islem == '1':
        ortalama_oku()
    elif islem == '2':
        not_gir()
    elif islem == '3':
        kaydet()
    else:
        break