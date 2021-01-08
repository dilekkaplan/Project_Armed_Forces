from datetime import datetime           # Şu anda bulunduğumuz seneyi kullanabilmek için datetime modülünü import ettik.  
instanceTime = datetime.now()

class SilahliKuvvetler(object):  
    "This class represents Silahlı Kuvvetler and it's the parent class.-Oğuz-"
    
    def __init__(self,name,yearOfStart):  
        self.name = name  
        self.yearOfStart = yearOfStart
        

    def Description(self):
        print("Türk Silahlı Kuvvetleri, Türkiye'yi karadan, havadan ve denizden gelebilecek her türlü saldırıya karşı korumakla görevli olan askerî kuvvettir.\n")
        print("Yaptırım gücünü Türkiye Cumhuriyeti Anayasası'ndan alır.\n")
        print("Türk Kara Kuvvetleri, Türk Hava Kuvvetleri ve Türk Deniz Kuvvetlerinden oluşmaktadır.")
        

    def IsRetired(self):  
                 
        if (instanceTime.year - self.yearOfStart) > 45:  
            return True                                         # If it's achieved to condition we retire them
        else:  
            return False  

  

class Jet(SilahliKuvvetler):  
    "This class represents Jets -Mete" 
    bomb = 0

    def __init__(self,name,yearOfStart):                   
        SilahliKuvvetler.__init__(self, name, yearOfStart)        # This line is for use the super class's(SilahlıKuvvetler) init module   
        print("-"*20)
        print("İstikbal Göklerdedir !")                           # Citation from Atatürk, signifies the importance of aviation
        print("-"*20) 
  
    def IsRetired(self):                                                                                              
        "Returns boolean value depending on work time"                                                               
        
        # We override Isretired here
        # because jets've more bench life

        if (instanceTime.year - self.yearOfStart) > 55:  
            return True                                                                         # If it's achieved to condition we retire them   
        else:  
            return False

    def LoadOn(self,bomb=0):  
        
        if self.IsRetired():                                                                    # If it's retired he wouldn't load on 
            print("He's retired. It is not available to load on. Don't bother him!")
        else:
            self.bomb = bomb
            if self.bomb == 0:
                print(self.name, "hasn't got any bomb.")  
            else:
                print(self.name, "has loaded with", self.bomb,"tons bomb.")  
  
  
    def TakeOff(self, adress, bomb2drop=0):  
        
        if self.IsRetired():                                                                    # If it's retired he wouldn't take off
            print("He's retired. It can not take off!")
        else:
            self.bomb2drop = bomb2drop                                                          # with tonnes  
            self.adress = adress      
            self.bomb = self.bomb - self.bomb2drop  
            
            if self.bomb2drop == 0:
                print(self.adress,"has just visited by",self.name,".")
            else:                                                         
                print(self.name,"has bombed:",self.adress,", with:", self.bomb2drop,"tons bombs.")  # informing the user

            if (self.bomb == 0) and (bomb2drop != 0):
                print("All bombs are dropped..")



class Denizaltı(SilahliKuvvetler):
    "Bu sınıf denizaltıları temsil eder, TSK envanterinde aktif faaliyette olan denizaltı sınıfları incelenmiştir -Ata" #silahlı kuvvetler classına override yapılmıştır
    
    def __init__(self,name,yearOfStart):                 
        SilahliKuvvetler.__init__(self, name, yearOfStart)
        print("-"*27)
        print("ETKİN , CAYDIRICI , SAYGIN")                                    #Türk Deniz Kuvvetleri'nin sloganıdır.Denizaltı sınıfı çağrıldığında yansıtılacaktır.                                      
        print("-"*27)

    def sınıflar(self):
        print("GÜR , PREVEZE , AY ")                                          #Türk Silahlı Kuvvetlerinde 3 çeşit denizaltı sınıfı vardır
                                                                                                
                                                                                            
    def slogan(self,denizaltının_sınıfı):
        self.denizaltının_sınıfı=denizaltının_sınıfı          #Her denizaltının kendine has bir sloganı olur. Her sınıf denizaltından birer örnek slogan yazdırdım

        if self.denizaltının_sınıfı=="GÜR":
            print("DENİZLER ONUNLA HÜR")
        if self.denizaltının_sınıfı=="PREVEZE":
            print("DERİNLİKLERİN EFSANESİ")
        if self.denizaltının_sınıfı=="AY":
            print("DERİNLİKlERİN CESUR OKU")
    
    def Deplasman_tonajı(self,denizaltının_sınıfı):
        self.denizaltının_sınıfı=denizaltının_sınıfı

        if self.denizaltının_sınıfı=="GÜR":
            print("Satıhta 1454 ton, dalmış halde 1586 ton taşır" )                         #deplasman tonajı bir denizaltının hareket kabiliyetini kaybetmeyeceği maksimum ağırlıktır.
                                                                                            #kaynakça : https://www.dzkk.tsk.tr/Destek/icerik/gür-sinifi         
        if self.denizaltının_sınıfı=="PREVEZE":
            print("Satıhta 1454 ton, dalmış halde 1586 ton taşır" )                         #kaynakça : https://www.dzkk.tsk.tr/Destek/icerik/preveze-sinifi
                
        if self.denizaltının_sınıfı=="AY":
            print("Satıhta 980 ton, dalmış halde 1185 ton taşır" )                          #kaynakça : https://www.dzkk.tsk.tr/Destek/icerik/ay-sinifi 

        elif self.denizaltının_sınıfı!="AY" and self.denizaltının_sınıfı!="PREVEZE" and self.denizaltının_sınıfı!="GÜR":         #yanlış girişlerde kullanıcıyı uyarır
            print("lütfen TSK envanterinde olan bir denizaltı sınıfı giriniz")
            
    def Seyir_menzili(self,denizaltının_sınıfı):
        self.denizaltının_sınıfı=denizaltının_sınıfı #Denizaltı sınıflarına göre menzillerini gösterir, metreye çevirir.
        nm=1852                                                                         #bir deniz mili (nautical mile) 1852 metredir hesaplamalarımızda kullanacağız

        if self.denizaltının_sınıfı=="GÜR":
            seyir_menzili_nm=7500
            seyir_menzili_m=7500*nm
            print("GÜR sınıfı denizaltıların menzili ,", seyir_menzili_nm ,"deniz milidir.""\n" "Bir deniz mili ",nm,"  metre olduğuna göre seyir menzili ,",seyir_menzili_m,"metre eder.")

        if self.denizaltının_sınıfı=="PREVEZE":
            seyir_menzili_nm=8200
            seyir_menzili_m=8200*nm
            print("PREVEZE sınıfı denizaltıların menzili ,",seyir_menzili_nm, "deniz milidir.\n Bir deniz mili ",nm," metre olduğuna göre seyir menzili ,",seyir_menzili_m,"metre eder.")

        if self.denizaltının_sınıfı=="AY":
            seyir_menzili_nm=7500
            seyir_menzili_m=7500*nm
            print("AY sınıfı denizaltıların menzili ,",seyir_menzili_nm, "deniz milidir.\n Bir deniz mili ",nm," metredir. Metreye çevirecek olursak ,",seyir_menzili_m,"metre eder.")

        elif self.denizaltının_sınıfı!="AY" and self.denizaltının_sınıfı!="PREVEZE" and self.denizaltının_sınıfı!="GÜR":            #yanlış girişlerde kullanıcıyı uyarır
            print("lütfen TSK envanterinde olan bir denizaltı sınıfı giriniz")
    
    def IsRetired(self):                                         # Silahlı kuvvetlerdeki   IsRetired fonksiyonunun (override) üzerine yazacağız
                                                                 # Gemiler silahlı kuvvetlerde en uzun süre kullanılabilen araçlardır , bunun sebebi ise her sene periyodik bakımları olmasıdır.

        if (instanceTime.year - self.yearOfStart) > 60:  
            return True                                         # En eski denizaltılar ay sınıfı denizaltılardır ve 1975 te alınmıştır,hala aktif servistedir.  
        else:  
            return False




class Personel(SilahliKuvvetler): 
    " This class represents the personnel doing military service in Turkish Army as profession -Nilüfer"
       
    def __init__(self, name, yearOfStart):                         
        SilahliKuvvetler.__init__(self, name, yearOfStart)                    
                   
   
    def degree(self):
        "This function calculates the degree of soldiers according to the time spent in the profession."
                                                    
        '''We will use the current year to calculate the time soldiers have worked.                
        After finding today's date, we will use the "year" method to use the year.
        With x, we calculate the time the soldier worked.'''
        
        x = instanceTime.year - self.yearOfStart

        # We determine the degree of the members of the army who do their military service professionally according to the time required to obtain
        # their degree.
        # We assume the situation where the soldier does not retire until his mandatory retirement.

        if x < 1 :
            return "Asteğmen"        
        elif  x < 4:            
            return "Teğmen"        
        elif x >=4 and x < 10 :
            return "Üsteğmen"        
        elif x >= 10 and x < 16 :
            return "Yüzbaşı"        
        elif x >= 16 and x < 21 :
            return "Binbaşı"        
        elif x >= 21 and x < 24 :
            return "Yarbay"        
        elif x >= 24 and x < 29 :
            return "Albay"        
        elif x >= 29 and x < 33 :
            return "Tuğgeneral"        
        elif x >= 33 and x < 37 :
            return "Tümgeneral"        
        elif x >= 37 and x < 41 :
            return "Korgeneral"        
        elif x <= 41 and x > 45 :
            return "Orgeneral"
        elif x>= 45 :
            return "mandatory retirement"
        

    def assignment(self,duration=0):
        "Duration = the soldier's working time at the last place of duty"
        "This function takes as an argument to get work at the soldier's last duty station and returns the time remaining to the next assignment period."

        #We consider the working period as 10 years."

        self.duration = duration

        if duration == 10:
            print(self.name,"will be appointed this year.")

        elif duration>=0 and duration < 10:            
            print("{} years left to the next assignment period of".format(10-duration),self.name)
        else:
            print("Please enter a valid working period (from 0 to 10)")
        

    def salary(self):
        "This function uses the return of the degree function and prints the salary of the soldiers according to the degree."
        a = self.degree()

        if a == "Asteğmen":
            print("The salary of {} is 5000 TL.".format(self.name))
        elif a == "Teğmen":
            print("The salary of {} is 6500 TL.".format(self.name))
        elif a == "Üsteğmen":
            print("The salary of {} is 7000 TL.".format(self.name))
        elif a == "Yüzbaşı":
            print("The salary of {} is 7200 TL.".format(self.name))
        elif a == "Binbaşı":
            print("The salary of {} is 7500 TL.".format(self.name))
        elif a == "Yarbay":
            print("The salary of {} is 8200 TL.".format(self.name))
        elif a == "Albay":
            print("The salary of {} is 8600 TL.".format(self.name)) 
        elif a == "Tuğgeneral":
            print("The salary of {} is 9200 TL.".format(self.name))
        elif a == "Tümgeneral":
            print("The salary of {} is 10000 TL.".format(self.name)) 
        elif a == "Korgeneral":
            print("The salary of {} is 11000 TL.".format(self.name)) 
        elif a == "Orgeneral":
            print("The salary of {} is 12000 TL.".format(self.name))
        elif a == "mandatory retirement" :
            print("The salary of {} is 7500 TL.".format(self.name))


            
class Tanklar(SilahliKuvvetler):
    "Bu class tankları temsil eder. -Dilek-"
 
    def __init__(self,name,yearOfStart,origin):
        super().__init__(name,yearOfStart)
        self.origin=origin
 
 
    def info(self):
        "isim, kullanım yılı ve menşei ile ilgili bilgileri yazdırıyoruz."
        print("Tank İsmi:",self.name,"\nKullanıma başlama yılı:",self.yearOfStart,"\nOrijin:",self.origin) 

 
    def agility(self,strength,weight):
        "tankın ağırlık (ton cinsinden) ve atiklik durumuyla ilgili bilgileri yazdırıyoruz."          
 
        self.strength=strength
        self.weight=weight
 
        agility=strength/weight                 #Bir tankın çevikliği tank gücünün ağırlığına bölünmesi ile elde edilir.
               
 
        if agility>=18:                         #Tankın çevilikiği >18 ise tankın çevik olduğu kabul edilmiştir. 
            #Tank ağırlığı 55 tondan büyükse ağır, 50-55 arasındaysa orta ağırlıkta ve 50den küçükse hafif tank olarak kabul edilmiştir.            
            if weight>=55:
                print(self.name, "atik ve ağır bir tanktır.") 
            if 50<weight<55:
                print(self.name, "atik ve orta ağırlıkta bir tanktır.") 
            if weight<50:
                print(self.name, "atik ve hafif bir tanktır.")       
        else:
            print(self.name, "atik bir tank değildir.")
 
 
    def time2repair(self):
        "tankın bakımının ne zaman yapılması gerektiği ile ilgili bilgiyi yazdırır." 
        
        year = instanceTime.year                                  # Biz yalnızca yıl ile ilgilendiğimiz için yıl year fonksiyonu ile içinde bulunduğumuz yıl bilgisini çektik.
 
        if (year-self.yearOfStart)%5==0:
            #Tankların bakımı 5 yılda bir yapılmalıdır.
            #Tankın kullanıma başlandığı yıl esas alınarak bakım yapılması gerken sene hesaplanmıştır 
            print(self.yearOfStart, "yılında alınan", self.name, "nin bakımı bu yıl içerisinde yapılmıştır,5 yıl sonra tekrar bakımı yapılacaktır.") 
        elif (year-self.yearOfStart)%5!=0:
            print(self.yearOfStart,"yılında alınan",self.name, "nin bakımı", (5-((year-self.yearOfStart)%5)), "yıl sonra yapılacaktır.")
 

    def is_usable_in_water(self,passwater,passwater_prep):
        "Tankların sulu ortamlarda çalışabilme durumunu true/false ile veren fonksiyon"
        self.passwater=passwater
        self.passwater_prep=passwater_prep
        #Tankların  hazırlıksız ve hazırlıklı durumlarda geçebildikleri su yüksekliğinin farkı esas alınmıştır. 
        
        if (passwater_prep-passwater)>200:          #Hazırlıklı durumda geçilebilen su yüksekliği ile hazırlıksız durumda geçilebilen            
            return True                             #su yüksekliği arasındaki fark 200cm olduğunda, bu tank sulu ortamlarda çalışabiliyor demektir.
        else:
            return False
        
    

class Helicopter(SilahliKuvvetler):
    "Bu class helikopterleri temsil eder. -Büşra-"
   
    def __init__(self,name,yearOfStart,origin):
       SilahliKuvvetler.__init__(self, name, yearOfStart)
       self.origin=origin


    def bilgileri_goster(self):
        "bilgileri_goster fonksiyonuyla helikopterin adı,kullanıma başlama yılı ve originine ait bilgileri görebiliyoruz."
        return print("Helikopterin Adı: {} Kullanıma Başlama Yılı: {}  Origin: {} ".format(self.name,self.yearOfStart,self.origin))  


    def length(self,length):
        self.length=length
        "uzunluk fonksiyonuyla helikopterin uzunluğuna(metre cinsinden) ait bilgileri görebiliyoruz."
        if self.length<15.0:
            print("Bu helikopterin uzunluğu: {} ve küçük helikopter kategorisine girer".format(self.length))
        if 15.0<=self.length<=20.0:
            print("Bu helikopterin uzunluğu: {} ve orta helikopter kategorisine girer".format(self.length))
        else:
            print("Bu helikopterin uzunluğu: {} ve büyük helikopter kategorisine girer".format(self.length))


    def max_kalkış_kütlesi(self,masse1):
        self.masse1=masse1
        "max_kalkış_kütlesi fonksiyonuyla helikopterin maksimum kalkış kütlesiyle(kg cinsinden ve helikopterin kütlesi hariç) hangi sınıfa ait olduğunu görebiliyoruz."
        if self.masse1< 2300:
            print("Bu helikopter 1.kategoridedir")
        if 2300<=self.masse1< 5000:
            print("Bu helikopter 2.kategoridedir")
        if 5000<=self.masse1< 9000:
            print("Bu helikopter 3.kategoridedir")
        if 9000<=self.masse1< 13500:
            print("Bu helikopter 4.kategoridedir")
        if 13500<=self.masse1< 19500:
            print("Bu helikopter 5.kategoridedir")
        if 19500<=self.masse1< 27000:
            print("Bu helikopter 6.kategoridedir")

    #masse1 helikopter kütlesi hariç, masse2 helikopter kütlesi dahil
    def distance(self,masse2):
        self.masse2=masse2
        "distance fonksiyonu helikopter toplam kütlesine göre FATO(Son yaklaşma ve kalkış alanı) kenarı ile uçak pisti kenarı arasındaki mesafeyi görebiliyoruz."

        if self.masse2<2720:
            print("60m")
        if 2720<=self.masse2<5760:
            print("120m")
        if 5760<=self.masse2<100.000:
            print("180m")
        else:
            print("250m")

class İHA(SilahliKuvvetler): #İHA, "insansız hava aracı"nın kısaltması olarak kullanılmıştır
    "Tanımlanan bu sınıf 'insansız hava araçları' yani 'iha' sınıfıdır ve silahlı kuvvetler sınıfından türemiştir."
    
    def __init__(self, name, yearOfStart, mass, elevation):
        SilahliKuvvetler.__init__(self, name, yearOfStart)
        self.mass=mass
        self.elevation=elevation
        print("Lütfen tanımladığınız İHA'nın kütlesini kilogram ve görev yüksekliğini feet olarak girdiğinizden emin olun.")

    def sınıf(self): #Bu fonksiyon aracın hangi sınıfa ait olduğunu belirleyip yazdırır #Aracın kütlesi kilogram(kg) olarak girilmelidir
        if self.mass<150: #Eğer kütle 150 kg'dan daha azsa sınıf kendi içinde kategorilere ayrılır.
            if self.mass<2:
                return("İHA Sınıf1'e ve mikro kategorisine aittir.")
            elif self.mass>=2 and self.mass<=20:
                return("İHA Sınıf1'e ve mini kategorisine aittir.")
            elif self.mass>20:
                return("İHA Sınıf1'e ve küçük kategorisine aittir.")         
        elif 150<=self.mass and self.mass<=600:
            return("İHA Sınıf2'ye aittir.")    
        elif 600<self.mass:
            if self.elevation<45000:
                return("İHA Sınıf3'e ve 'orta irtifa uzun havada kalış (MALE) kategorisine aittir.")
            elif self.elevation<65000:
                return("İHA Sınıf3'e ve 'yüksek irtifa uzun havada kalış (HALE) kategorisine aittir.")
        else:
            print("Lütfen aracın kütlesini kilogram olarak doğru şekilde giriniz.")

    def görev_yarıçapı(self): #Bu fonksiyon aracın görev yarıçapını belirleyip yazdırı #Görev yüksekliği Feet(ft) olarak girilmelidir
        if self.elevation<200:
            return("Görev yarıçapı: 5 km; LOS") #LOS: İnsanlı ve insansız hava araçları için "görüş hattı" diye belirlenen terim
        elif self.elevation<3000:
            return("Görev yarıçapı: 25 km; LOS")
        elif self.elevation<5000:
            return("Görev yarıçapı: 50 km; LOS")
        elif self.elevation<10000:
            return("Görev yarıçapı: 200 km; LOS")
        elif self.elevation<45000:
            return("Görev yarıçapı: limitsiz; BLOS") #BLOS: İnsanlı ve insansız hava araçları için "görüş hattı ötesi" diye belirlenen terim
        elif self.elevation<65000:
            return("Görev yarıçapı: limitsiz; BLOS")
        else:
            print("Lütfen aracın görev yüksekliğini feet olarak doğru şekilde giriniz.")

    def rekor(self): #Bu fonksiyon aracın, Türk havacılık tarihindeki irtifa rekorunu kırıp kırmadığını yazdırır
        if self.elevation<27.030:
            print("Bu İHA, Türk havacılık tarihinde var olan irtifa rekorunu kıramamıştır. Rekor 27.030 ft ile Bayraktar TB2'ye aittir.")
        elif self.elevation>=27.030:
            print("Bu İHA, Türk havacılık tarihinde var olan irtifa rekorunu kırmıştır. Eski rekor 27.030 ft ile Bayraktar TB2'ye aitti.")

    def genel_bilgi(self): #Bu fonksiyon tanımlanan İHA ile ilgili bütün girilen ve fonksiyonlarla bulunan özellikleri topluca yazdırır
        print("İHA Adı:",self.name,"Kullanıma başlanma yılı:",self.yearOfStart,"Kütlesi:",self.mass,"kg","Görev yüksekliği:",self.elevation,"ft",self.görev_yarıçapı(), self.sınıf())



class Roketler():
    """ Bu class TSK envanterindeki roketleri gösterir. -Tevfik"""
    
    """kargo_roketleri = ["SLS","SLN","SLS3"]
    roket_firlatici = ["T270", "T-122", "T-300", "T-500","T-999"]
    havan_toplari = ["M52", "MKE", "M109", "M108", "M-44","M-999"]"""
    
    def __init__(self,model):
        """Class başlangıcı kısmı."""
        self.model = model


    def __str__(self):
        """Operator overloading kısmı.Default __str__ implementation'u yerine daha okunaklı bir gösterim yaptım."""
        return f"Roketin modeli >> {self.model}'dir."  


    def menşei(self):
        """ Verilen modelin menşeisini gösterir.
        T ile başlayan her model, Türk yapımıdır. Gerisiyse ABD menşeilidir."""
        print(self.model+"'in menşeisi Türkiye'dir.") if self.model.startswith("T") else print(
            self.model+"'in menşeisi ABD'dir.")


    def roket_türü(self):
        """ Verilen modelin türünü gösterir.
        Ülkemizdeki tüm roket fırlatıcılar millidir ve T ile başlar."""
        if self.model.startswith("S"):
            print("Girilen model bir kargo roketidir.") 
        if self.model.startswith("T"):
            print("Girilen model bir roket fırlatıcıdır.") # Ülkemizdeki tüm roket fırlatıcılar millidir ve T ile başlar.
        else:
            print("Girilen model bir havan topudur.")


    def hangi_roket_atılmalı(self, metrekare):
        """Verilen metrekarelik savaş alanına atılması gereken roket tercihini gösterir."""
        if metrekare < 5000:
            print("T-122 ve M52 ikilisi kullanılmalı.\n")   # Bu ikili yalnızca dar alanları tahrip edebilir.
        elif metrekare < 10000:
            print("T-300 ve MKE ikilisi kullanılmalı.\n")   
        elif metrekare < 15000:
            print("T-500 ve M44 ikilisi kullanılmalı.\n")
        elif metrekare < 20000:
            print("T-270 ve M108 ikilisi kullanılmalı.\n")
        else:
            print("T-999 ve M-999 ikilisi kullanılmalı.\n") # Bu ikili atıldığı bölgenin neredeyse tamamını tahrip edebilir



class Terrorism():
    "Bu sınıf terör aktivitelerine göre bölgelerin tehlike seviyesini ve kullanılması gereken ekipmanı temsil eder. Zeynep"
    def __init__(self,location_name):
        self.location_name = location_name
    
    def degree_of_the_danger(self,danger=0): #tehlikeyi 10 üzerinden alır.
        "Bölgenin tehlike seviyesini değişken olarak giriniz."#kırmızı yüksek tehlike seviyesini, mavi orta tehlike seviyesini, 
        if danger >= 5 and danger < 7:         # yeşil düşük tehlike seviyesini, beyaz beklenen bir tehlike olmadığını temsil eder.
            return "Mavi Bölge"
           
        if danger >= 7 and danger <= 10:
            return "Kırmızı Bölge"
           
        if danger < 5 and danger >= 3:
            return "Yeşil Bölge"
           
        if danger >= 0 and danger < 3:
            return "Beyaz Bölge"
            
        else:
            print("Lütfen belirtilen sayı aralığında değerlendirme yapın!")

    def recommended_variations(self,danger):
        "Bölgenin tehlike seviyesini değişken olarak giriniz"
        a = self.degree_of_the_danger(danger)
        if a == "Beyaz Bölge":
            return "Sadece personel öneriliyor ve bir çeşit araç"

        elif a == "Kırmızı Bölge":
            return"Bölgeye uygun tüm ekipman çeşitleri ve personel öneriliyor"

        elif a == "Yeşil Bölge":
            return "Personel ve o bölgeye uygun üç çeşit ekipman öneriliyor"

        elif a == "Mavi Bölge":
            return "Personel ve o bölgeye uygun beş çeşit ekipman öneriliyor"               
                                                                     

    def equipment_selection(self,iklim=0,deniz_kenari=0,engebeli=0):
        "iklim 'agir' veya 'hafif', deniz_kenari ve engebeli True/False şeklinde seçilmelidir."
                                                                     #bölgenin belirleyici özelliğine göre ekipman
        if deniz_kenari == False and iklim == "agir":                #seçimi yapılır. İklim agir/hafif şeklinde
            if engebeli == True:                                     #Deniz Kenarı True/False şeklinde
                return ["Jet",  "personel", "İHA","roket"]                   #engebeli True/False şeklinde girilmelidir.
            if engebeli == False:
                return ["Jet",  "personel", "tank", "İHA","roket"]                        

        elif deniz_kenari == False and iklim == "hafif":
            if engebeli == True:                                           
                return ["Jet",  "personel", "helikopter","İHA","roket"]                                 
            if engebeli == False:
                return ["Jet",  "personel", "helikopter", "tank","İHA","roket" ]                       

        elif deniz_kenari == True and iklim == "hafif":
            if engebeli == True:                                           
                return ["Jet",  "personel", "helikopter", "denizaltı","İHA","roket" ] 
            if engebeli == False:
                return ["Jet", "personel","tank", "helikopter", "denizaltı","İHA","roket"]
        elif deniz_kenari == True and iklim == "agir":
            if engebeli == True:                                           
                return ["Jet", "personel","denizaltı","İHA","roket"] 
            if engebeli == False:
                return ["Jet", "personel", "tank" ,"denizaltı","İHA","roket" ]



class silah(Terrorism):
    " Bu sınıf bölgenin tehlike düzeyine,silahın taşınabileceği ağırlığa ve gerekli menziline göre silah tipini belirler. -Bengisu"

    def __init__(self,location_name,):
        Terrorism.__init__(self,location_name)
        

    def silah_sec(self,agirlik,menzil): # bu fonksiyon silahları kg cinsinden ağırlıklarına
                                        #ve metre cinsinden menzillerine göre ayırır
        "ağr<=1 mnz<300;1<ağr<=4 300<mnz<=400;4<ağr<=6 400<mnz<=1000;6<ağr<=12 1k<mnz<=6800"

        self.agirlik=agirlik
        self.menzil=menzil
                
        if self.agirlik <= 1 and self.menzil <= 300:
            return 'tabanca' 

        if 1< self.agirlik <=4 and 300< self.menzil <=400:
            return 'tüfek'

        if 4< self.agirlik <=6 and 400< self.menzil <=1000:
            return 'keskin nişancı tüfeği'

        if 6< self.agirlik <= 12 and 1000< self.menzil <= 6800:
            return 'makineli tüfek'

        else:
            print("Böyle bir silah üretilmemiştir")
            
    def uygunluk(self,danger): #Terrorism classının degree_of_the_danger fonksiyonununu
                               #çağırarak bölgelerin tehlike düzeylerine göre silah önerisinde bulunuyor.
                               #silah önerisi yaparken silah seç fonksiyonunu çağırıyor.
        "Bölgenin tehlike seviyesini 10 üzerinden değerlendirin."
        a = self.degree_of_the_danger(danger)
        
        if a == "Kırmızı Bölge":
            print('Kırmızı Bölge: yok edici silahlar gerekir')
            return self.silah_sec(12,6800)
    
        if a == "Beyaz Bölge":
            print('Beyaz Bölge: hafif silahlar yeterlidir')
            return self.silah_sec(1,300)

        if a == "Mavi Bölge":
            print('Mavi Bölge: güçlü silahlar gerekir')
            return self.silah_sec(6,1000)

        if a == "Yeşil Bölge":
            print('Yeşil Bölge: etkili silahlar gerekir')
            return self.silah_sec(4,400)

''' TRY SECTION '''

# Jet
MorPenguen = Jet("F4",1945)
print(MorPenguen.name,"is retired: ", MorPenguen.IsRetired())
MorPenguen.LoadOn(4)
MorPenguen.TakeOff("Afyon",0)
print(MorPenguen.name, "has", MorPenguen.bomb, "tons bomb left.")

# Denizalti
TCG_PREVEZE = Denizaltı("TCG_PREVEZE",1989)
print(TCG_PREVEZE.name,"emekli edilmiştir: ",TCG_PREVEZE.IsRetired())
TCG_PREVEZE.slogan("PREVEZE")
TCG_PREVEZE.Deplasman_tonajı("PREVEZE")
TCG_PREVEZE.Seyir_menzili("PREVEZE")

# Helicopter
