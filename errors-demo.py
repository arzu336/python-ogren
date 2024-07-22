#liste elemanı içindeki sayısal değerleri bulun
# liste=["1","2","5a","10b","abc","10","50"]
# #liste elemanları içindeki sayısal değerler
# for x in liste:
#      try:
#           result=int(x)
#           print(result)
#      except ValueError:
#           continue     


#kullanıcı q degerini girmedikçe girilen değerin sayı olup olmadıgını kontrol edin değilse hata ver

# values=[]

# while True:
#      value=input("sayi:")
#      if (value=='q'):
#           print("bitti")
#           break
#      values.append(value)

# for c in values:
#      try:
#           deneme=int(c)
#           print(deneme)
#      except ValueError:
#           continue       

#girilen parola içinde türkçe karakter hatası

# def turkce_karakter_hatasi(psw):
#      import re
#      if len(psw)<8:
#           raise Exception('parola en az 7 karakterden oluşmalıdır')
#      elif re.search('[şüıçö]',psw):
#           raise Exception("türkçe karakterler bulunmamalıdır")
#      elif re.search("/s",psw):
#           raise Exception("parola boşluk içermemelidir")
     
# password=input('şifreyi giriniz:')
# try:
#      turkce_karakter_hatasi(password)
# except Exception as ex:
#      print(ex)
# else:
#      pass
# finally:
#      print("validation tamamlandı")   

# #girilen parola içinde türkçe karakter hatası

def check_name(name):
     turkce_karakterler='ı,ö,ç,Ş,İ,ş,Ö,Ç'
     for i in name:
          for i in turkce_karakterler:
               raise Exception('türkçe karakter kullanmayınız')
          
while True:
     ad=input("name:")
     try:
          check_name(ad)
     except Exception as e:
          print(e)
     else:
          break                    

