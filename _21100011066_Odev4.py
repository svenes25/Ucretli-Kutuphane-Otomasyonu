#21100011066
#ENES EREN SEVEN
#ÜCRETLİ KÜTÜPHANE OTOMASYONU
import datetime #Kütüphaneye abonelik süresini bulmak için
import time #Kütüphane içerisine giriş saatini ve çıkış saatini ayarlamak için
import winsound #Alarmın çalması için
print("kütüphane otomasyonuna hoş geldiniz\n")
Kullanicilar=[]
mesgul=[]#KÜTÜPHANE İÇERİSİNDE OLANLAR DEPOLANIYOR
Aboneler=[]#Kütüphaneye abone olanlar saklanıyor.
NULL={}#python da NULL değereni bulamadım kendim NULL yaptım
ListeNULL=[]#Bu da arada lazım oluyor.
AbonelikUcreti=300
saat=int(input("Lütfen kapanış saatini önce saat sonra dakika şeklinde giriniz:\n"))
dakika=int(input())
saatlik3=int(input("3 saatlik giriş ücretini giriniz: "))
gunluk=int(input("Günlük giriş ücretini giriniz: "))
denklik=1
id=0
if(saat>24 or dakika>60):
    print("Geçerli bir kapanış saati girmediniz")
    denklik=0
while (denklik!=0):
    kullanici={}
    bosta=[]#KÜTÜPHANEDE SÜRESİ DOLANAN KİŞİLERİ ATABİLMEK İÇİN KULLANDIM. MEŞGULDE SÜRESİ DOLAN BURAYA ATILIYOR
    def KullaniciListele():
        global Kullanicilar
        Kullanicilar=[]
        print("\n")
        with open("21100011066.txt","r",encoding="utf-8") as a:
            degisken=a.readlines()
            if(degisken!=ListeNULL):
                try:
                    for i in degisken:
                        kullanici={}
                        b=i.split("-")
                        b.remove("\n")
                        kullanici["ID"]=int(i[0])
                        kullanici["İsim"]=b[1]
                        kullanici["Soyisim"]=b[2]
                        kullanici["Okul"]=b[3]
                        kullanici["Bakiye"]=int(b[4])
                        kullanici["Numara"]=int(b[5])
                        Kullanicilar.append(kullanici)

                except:
                    print("Kullanici Dosyasında Hata Bulundu Lütfen Düzeltin\n")

                try:
                    for i in range(len(Kullanicilar)):
                        if(Kullanicilar[i]["ID"]==Kullanicilar[-1]["ID"]):
                            Kullanicilar[-1]["ID"]=Kullanicilar[-2]["ID"]+1
                except:
                    pass
                print("Kullanicilar Aşağıda Listelenmiştir\n")
                for i in Kullanicilar:
                    print(i)
                    global id
                    id=i["ID"]
    
            else:
                print("Kütüphaneye Kayıtlı Kullanici Bulunamadi\n")
    def KullaniciKayit(id,isim,soyisim,okul,bakiye,numara):
        yenikullanici={}
        yenikullanici["id"]=id
        yenikullanici["isim"]=isim
        yenikullanici["soyisim"]=soyisim
        yenikullanici["okul"]=okul
        yenikullanici["bakiye"]=bakiye
        yenikullanici["numara"]=numara
        with open("21100011066.txt","a+",encoding="utf-8") as kullanici:
            kullanici.write("{}-{}-{}-{}-{}-{}-\n".format(id,isim,soyisim,okul,bakiye,numara))
        print(yenikullanici)
        print("kullanıcı başarı ile sisteme kaydedildi\n\n")
    def KullaniciSil(id):
        def DosyaYazdir(Kullanicilar):
            with open("21100011066.txt","w",encoding="utf-8") as a:
                for i,e in enumerate(Kullanicilar):
                    a.write("{}-{}-{}-{}-{}-{}-\n".format(e["ID"],e["İsim"],e["Soyisim"],e["Okul"],e["Bakiye"],e["Numara"]))
            KullaniciListele()
        if(Kullanicilar!=NULL):
            sil=KullaniciBul(id)
            try:
                Kullanicilar.remove(sil)
                DosyaYazdir(Kullanicilar)
            except:
                print("Lütfen Önce Kullanıcıları Listeleyiniz\n")
        else:
            print("Kayıtlı kullanıcı bulunamadı\n\n")
    def KullaniciBul(id):
        if(Kullanicilar!=ListeNULL):
            for i in Kullanicilar:
                if(i["ID"]==id):
                    return i
        else:
            print("Aranan Kullanici Bulunamadi\n")
    def KullaniciGuncelle(id):
        def DosyaYazdir(Kullanicilar):
            with open("21100011066.txt","w",encoding="utf-8") as a:
                for i,e in enumerate(Kullanicilar):
                    a.write("{}-{}-{}-{}-{}-{}-\n".format(e["ID"],e["İsim"],e["Soyisim"],e["Okul"],e["Bakiye"],e["Numara"]))
            KullaniciListele()
        kullanici=KullaniciBul(id)
        degisim=int(input("Kullanıcın değiştirmek istediğiniz bilgisini giriniz\n1: isim\n2: soyisim\n3: okul\n4: bakiye\n5: numara\n"))
        if(degisim==1):
            for i in Kullanicilar:
                if(i==kullanici):
                    bilgi=input("Kullanicinin Güncel İsmini Giriniz: ")
                    i["İsim"]=bilgi
                    DosyaYazdir(Kullanicilar)
        elif(degisim==2):
            for i in Kullanicilar:
                if(i==kullanici):
                    bilgi=input("Kullanicinin Güncel Soyadini Giriniz: ")
                    i["Soyisim"]=bilgi
                    DosyaYazdir(Kullanicilar)
        elif(degisim==3):
            for i in Kullanicilar:
                if(i==kullanici):
                    bilgi=input("Kullanicinin Güncel Okulunu Giriniz: ")
                    i["Okul"]=bilgi
                    DosyaYazdir(Kullanicilar)
        elif(degisim==4):
            for i in Kullanicilar:
                if(i==kullanici):
                    bilgi=int(input("Kullanicinin Güncel Bakiyesini Giriniz: "))
                    i["Bakiye"]=bilgi
                    DosyaYazdir(Kullanicilar)
        elif(degisim==5):
            for i in Kullanicilar:
                if(i==kullanici):
                    bilgi=int(input("Kullanicinin Güncel Numarasını Giriniz: "))
                    i["Numara"]=bilgi
                    DosyaYazdir(Kullanicilar)
        else:
            print("Geçerli Seçim Girmediniz\n")
    def KullaniciGiris(id):
        def DosyaYazdir(Kullanicilar):
            with open("21100011066.txt","w",encoding="utf-8") as a:
                for i,e in enumerate(Kullanicilar):
                    a.write("{}-{}-{}-{}-{}-{}-\n".format(e["ID"],e["İsim"],e["Soyisim"],e["Okul"],e["Bakiye"],e["Numara"]))
            KullaniciListele()
        kullanici=KullaniciBul(id)
        mesgulkullanici={}
        if(Kullanicilar!=ListeNULL):
            tarama=0
            kontrol=0
            for i in mesgul:
                if(i["ID"]==kullanici["ID"]):
                    kontrol=1
                    print("Kütüphane içerisindeki kullanıcı tekrardan kütüphaneye giremez\n")
                    break
            if(kontrol==0):
                for i in Aboneler:
                    if(i["ID"]==kullanici["ID"]):
                        giris=2
                        for i in Kullanicilar:
                            if(i["ID"]==kullanici["ID"]):
                                i["ID"]=i["ID"]+gunluk
                        tarama=1
                        break 
                if(tarama==0):
                    giris=int(input("Giriş türünü seçiniz\n1: 3 saatlik\n2: Tüm gün\n"))
                Girissaati=time.strftime("%H")
                TamGiris=time.strftime("%X")
                Girisdakika=time.strftime("%M")
                Cikissaati=int(Girissaati)+3
                Skontrol=int(Girissaati)
                Dkontrol=int(Girisdakika)
                if((saat>Skontrol) or ((saat==Skontrol) and (dakika>=Dkontrol))):
                    if(giris==1):
                        if(kullanici["Bakiye"]>=saatlik3):
                            kullanici["Bakiye"]-=saatlik3
                            if(Cikissaati>=saat):
                                print("Çıkış saatiniz",saat,":",dakika,"\n")
                                mesgulkullanici=kullanici.copy()
                                mesgulkullanici["Csaat"]=saat
                                mesgulkullanici["Cdakika"]=dakika
                            else:
                                print("Çıkış saatiniz: ",Cikissaati,".",Dkontrol)
                                mesgulkullanici=kullanici.copy()
                                mesgulkullanici["Csaat"]=saat
                                mesgulkullanici["Cdakika"]=dakika
                            print("Kalan bakiyeniz: ",kullanici["Bakiye"])
                            mesgul.append(mesgulkullanici)
                            with open("mesgul.txt","a",encoding="utf-8") as a:
                                a.write("{}-{}-{}-{}-{}-{}-{}-{}-\n".format(mesgulkullanici["ID"],mesgulkullanici["İsim"],mesgulkullanici["Soyisim"],mesgulkullanici["Okul"],mesgulkullanici["Bakiye"],mesgulkullanici["Numara"],mesgulkullanici["Csaat"],mesgulkullanici["Cdakika"]))
                            DosyaYazdir(Kullanicilar)
                        else:
                            print("Yeterli Bakiyeniz Bulunmamaktadır\n")
                elif(giris==2):
                    if(kullanici["Bakiye"]>=gunluk):
                        kullanici["Bakiye"]-=gunluk
                        print("Çıkış saatiniz",saat,":",dakika)
                        print("Kalan bakiyeniz: ",kullanici["Bakiye"])
                        mesgulkullanici=kullanici.copy()
                        mesgulkullanici["Csaat"]=saat
                        mesgulkullanici["Cdakika"]=dakika
                        mesgul.append(mesgulkullanici)
                        with open("mesgul.txt","a",encoding="utf-8") as a:
                            a.write("{}-{}-{}-{}-{}-{}-{}-{}-\n".format(mesgulkullanici["ID"],mesgulkullanici["İsim"],mesgulkullanici["Soyisim"],mesgulkullanici["Okul"],mesgulkullanici["Bakiye"],mesgulkullanici["Numara"],mesgulkullanici["Csaat"],mesgulkullanici["Cdakika"]))
                        DosyaYazdir(Kullanicilar)
                    else:
                        print("Yeterli Bakiyeniz Bulunmamaktadır\n")
                else:
                    print("Geçerli Bir Seçenek Girmediniz\n")

        else:
            print("Kayıtlı Kullanıcı Bulunamadı\n")
    def KutuphaneListele():
        global mesgul
        mesgul=[]
        print("\n")
        with open("mesgul.txt","r",encoding="utf-8") as a:
            degisken=a.readlines()
            if(degisken!=ListeNULL):
                try:
                    for i in degisken:
                        kullanici={}
                        b=i.split("-")
                        b.remove("\n")
                        kullanici["ID"]=int(i[0])
                        kullanici["İsim"]=b[1]
                        kullanici["Soyisim"]=b[2]
                        kullanici["Okul"]=b[3]
                        kullanici["Bakiye"]=int(b[4])
                        kullanici["Numara"]=int(b[5])
                        kullanici["Csaat"]=int(b[6])
                        kullanici["Cdakika"]=int(b[7])
                        mesgul.append(kullanici)

                except:
                    print("Mesgul Dosyasında Hata Bulundu Lütfen Düzeltin\n")

                print("Kütüphane İçerisi Aşağıda Listelenmiştir\n")
                for i in mesgul:
                    print(i)
            else:
                print("Kütüphaneye İçerisinde Kullanici Bulunamadi\n")
    def KutuphaneKontrol():
        AnlıkSaat=int(time.strftime("%H"))
        AnlıkDakika=int(time.strftime("%M"))
        for i in mesgul:
            if((i["Csaat"]<AnlıkSaat) or ((i["Csaat"]==AnlıkSaat) and (i["Csaat"]<=AnlıkDakika))):
                bosta.append(i)
        for i in bosta:
            for j in mesgul:
                if(i==j):
                    freq=440
                    dur=1500
                    for i in range(0, 3):#SESİ TEST ETMEK İÇİN BİLGİSAYARIN SAATİNİ KULLANICININ CIKIS SAATİ OLARAK AYARLAYABİLİRSİNİZ	
	                    winsound.Beep(freq, dur)	
	                    freq-= 50
                    print(b,"Kulanıcının süresi doldu\n")
                    mesgul.remove(J)
                    with open("mesgul.txt","a",encoding="utf-8") as a:
                        a.write("{}-{}-{}-{}-{}-{}-{}-{}-\n".format(j["ID"],j["İsim"],j["Soyisim"],j["Okul"],j["Bakiye"],j["Numara"],j["Csaat"],j["Cdakika"]))
                    DosyaYazdir(Kullanicilar)
    def Alisveris(id):
        def DosyaYazdir(Kullanicilar):
            with open("21100011066.txt","w",encoding="utf-8") as a:
                for i,e in enumerate(Kullanicilar):
                    a.write("{}-{}-{}-{}-{}-{}-\n".format(e["ID"],e["İsim"],e["Soyisim"],e["Okul"],e["Bakiye"],e["Numara"]))
        if(Kullanicilar!=ListeNULL):
            kullanici=KullaniciBul(id)
            if(kullanici!=None):
                tutar=int(input("Ödenecek tutarı giriniz: "))
                if(kullanici["Bakiye"]>=tutar):
                    kontrol=0
                    cashback=0
                    for i in Aboneler:
                        if(i["ID"]==kullanici["ID"]):
                            kontrol=1
                            break
                        else:
                            kontrol=0
                    if(kontrol==1):
                        cashback=tutar//10
                    kullanici["Bakiye"]-=tutar
                    kullanici["Bakiye"]+=cashback
                    print("\nBaşarılı şekilde alışveriş gerçekleştirildi")
                    print("Kalan Bakiyeniz:",kullanici["Bakiye"])
                    Dosyayazdir(Kullanicilar)
                else:
                    print("yeterli bakiye bulunmamaktadır\n")
        else:
            print("Kayıtlı kullanıcı bulunamadı\n")
    def BakiyeYukleme(id):
        def Dosyayazdir(Kullanicilar):
            with open("21100011066.txt","w",encoding="utf-8") as a:
                for i,e in enumerate(Kullanicilar):
                    a.write("{}-{}-{}-{}-{}-{}-\n".format(e["ID"],e["İsim"],e["Soyisim"],e["Okul"],e["Bakiye"],e["Numara"]))
        if(Kullanicilar!=ListeNULL):
            kullanici=KullaniciBul(id)
            if(kullanici!=None):
                para=int(input("Yüklemek istediğiniz miktarını giriniz: "))
                kullanici["Bakiye"]+=para
                DosyaYazdir(Kullanicilar)
        else:
            print("Kayıtlı kullanıcı bulunamadı\n")
    def Abonelik(id):
        def DosyaYazdir(Kullanicilar):
            with open("21100011066.txt","w",encoding="utf-8") as a:
                for i,e in enumerate(Kullanicilar):
                    a.write("{}-{}-{}-{}-{}-{}-\n".format(e["ID"],e["İsim"],e["Soyisim"],e["Okul"],e["Bakiye"],e["Numara"]))
        abone={}
        print("Aylık abonelik ücreti 300TL'dir\nAbonelik Kapsamında kütüphaneye ücretsiz girebileceksiniz\nYapacağınız alışverişlerin %10'U size CashBack olark geri dönecektir.\n")
        try:
            if(Kullanicilar!=NULL):
                kullanici=KullaniciBul(id)
                if(kullanici["Bakiye"]>=AbonelikUcreti):
                    kullanici["Bakiye"]-=AbonelikUcreti
                    AboneAnı=datetime.datetime.today()
                    AbonelikGunu=int(AboneAnı.day)
                    AbonelikAyı=int(AboneAnı.month)
                    AbonelikAyı+=1
                    if(AbonelikAyı>12):
                        AbonelikAyı=1
                    abone=kullanici.copy()
                    abone["AGun"]=AbonelikGunu
                    abone["AAy"]=AbonelikAyı
                    with open("aboneler.txt","a",encoding="utf-8") as a:
                        a.write("{}-{}-{}-{}-{}-{}-{}-{}-\n".format(abone["ID"],abone["İsim"],abone["Soyisim"],abone["Okul"],abone["Bakiye"],abone["Numara"],abone["AGun"],abone["AAy"]))
                    print("Başarıyla Abone Olundu\n")
                    print("Kalan Bakiyeniz:",kullanici["Bakiye"])
                    DosyaYazdir(Kullanicilar)
                else:
                    print("Yeterli Bakiyeniz Bulunmamaktadır\n")
            else:
                print("Kayıtlı Kullanıcı Bulunamadı\n")
        except:
            print("Aboneleri ya da Kullanıcıları Listelemeyi Unutmuş Olabilirsin\n")
    def AboneListele():
        global Aboneler
        Aboneler=[]
        print("\n")
        with open("aboneler.txt","r",encoding="utf-8") as a:
            degisken=a.readlines()
        if(degisken!=ListeNULL):
            for i in degisken:
                try:
                    for i in degisken:
                        kullanici={}
                        b=i.split("-")
                        b.remove("\n")
                        kullanici["ID"]=int(i[0])
                        kullanici["İsim"]=b[1]
                        kullanici["Soyisim"]=b[2]
                        kullanici["Okul"]=b[3]
                        kullanici["Bakiye"]=int(b[4])
                        kullanici["Numara"]=int(b[5])
                        kullanici["AGun"]=int(b[6])
                        kullanici["AAy"]=int(b[7])
                        Aboneler.append(kullanici)

                except:
                    print("Abone Dosyasında Hata Bulundu Lütfen Düzeltin\n")

                print("Aboneler Aşağıda Listelenmiştir\n")
                for i in Aboneler:
                    print(i)
        else:
            print("Abone Olan Kullanici Bulunamadi\n")
    def AboneKontrol():
        Gunkontrol=datetime.datetime.today()
        Gun=int(Gunkontrol.day)
        Ay=int(Gunkontrol.month)
        for i in Aboneler:
            if((i["AAy"]<Ay) or ((i["AAy"]==Ay) and (i["AGun"]<=Gun))):
                print(i,"Abonelik Süresi Dolmuştur\n")
                Aboneler.remove(i)
        with open("aboneler","w",encoding="utf-8") as a:
            for i in Aboneler:
                 a.write("{}-{}-{}-{}-{}-{}-{}-{}-\n".format(i["ID"],i["İsim"],i["Soyisim"],i["Okul"],i["Bakiye"],i["Numara"],i["AGun"],i["AAy"]))
    AnlıkSaat=int(time.strftime("%H"))
    AnlıkDakika=int(time.strftime("%M"))
    print("SAAT",AnlıkSaat,":",AnlıkDakika,"\n") 
    KutuphaneKontrol()
    AboneKontrol()
    print("1: Kullanıcı Listele\n2: Kullanıcı Kayıt\n3: Kullanıcı Sil\n4: Kullanıcı Güncelle\n5: Kullanıcı Bul\n6: Giriş İşlemleri\n7: Alısveriş İşlemleri\n8: Para Yükleme\n9: Abonelik İşlemleri\n0: Çıkış")
    secim=int(input("seçiminizi giriniz "))
    if(secim==1):
        sec=int(input("\n1: Kullanıcıları Listele\n2: Kütüphane İçerisini Listele\n3: Aboneleri Listele: "))
        if(sec==1):
            KullaniciListele()
        elif(sec==2):
            KutuphaneListele()
        elif(sec==3):
            AboneListele()
        else:
            print("Geçerli Bir Seçim Girmediniz\n")
    elif(secim==2):
        id+=1
        isim=input("Kullanıcı isimi: ")
        soyisim=input("Kullanıcı soyisimi: ")
        okul=input("Kullanıcını okuduğu okul: ")
        bakiye=int(input("Kullanıcın yüklemek istediği ücret: "))
        numara=int(input("Baştaki sıfır (0) olmadan telefon numarası giriniz: "))
        KullaniciKayit(id,isim,soyisim,okul,bakiye,numara)
    elif(secim==3):
        arananID=int(input("Silmek istediğiniz kullanicinin ID'sini giriniz: "))
        KullaniciSil(arananID)
    elif(secim==4):
        arananID=int(input("Güncellemek istediğiniz kullanicinin ID'sini giriniz: "))
        KullaniciGuncelle(arananID)
    elif(secim==5):
        arananID=int(input("Bulmak istediğiniz kullanicinin ID'sini giriniz: "))
        print(KullaniciBul(arananID))
    elif(secim==6):
        arananID=int(input("Kütüphaneye giriş yapacak kullanicinin ID'sini giriniz: "))
        KullaniciGiris(arananID)
    elif(secim==7):
        arananID=int(input("Alışveriş yapacak kullanicinin ID'sini giriniz: "))
        Alisveris(arananID)
    elif(secim==8):
        arananID=int(input("Para yüklemek istediğiniz kullanicinin ID'sini giriniz: "))
        BakiyeYukleme(arananID)
    elif(secim==9):
        arananID=int(input("Abone olmasını istediğiniz kullanicinin ID'sini giriniz: "))
        Abonelik(arananID)
    elif(secim==0):
        print("Başarıyla Çıkış Yapıldı\n")
        break
    else:
        print("Geçerli Seçim Girilmedi\n")
