class SilahliKuvvetler(object):  
    "This class represents Silahlı Kuvvetler and it's the parent class.-Oğuz-"  
    def __init__(self,name,yearOfStart):  
        self.name = name  
        self.yearOfStart = yearOfStart  
         
  
  
    def IsRetired(self):  
        from datetime import datetime                           # Anlık seneyi kullanabilmek için datetime modülünü import ettik.  
        instanceTime = datetime.now()                           # (init’e almadık ki sürekli import etmeyip,  
                                                                # gerektiği zamanlarda import etsin, performansta düşüklük yaşamayalım.)    
        if (instanceTime.year - self.yearOfStart) > 30:  
            return True                                          # If it's achieved to condition we retire them   
              
        else:  
            return False  
  
  
          
class Jet(SilahliKuvvetler):  
    "This class represents Jets -Mete" 
    bomb = 0

    def __init__(self,name,yearOfStart):                   
        SilahliKuvvetler.__init__(self, name, yearOfStart)        # This line is for use the super class's(SilahlıKuvvetler) init module   
        print("-"*20)
        print("İstikbal Göklerdedir !")
        print("-"*20) 
  
    def IsRetired(self):                                                                                              
        "Returns boolean value depending on work time"                                                               
        
        # We override Isretired here
        # because jets've more bench life

        from datetime import datetime
        instanceTime = datetime.now()

        if (instanceTime.year - self.yearOfStart) > 55:  
            return True                                                                         # If it's achieved to condition we retire them   
        else:  
            return False

    def LoadOn(self,bomb=0):  
        
        if self.IsRetired():                                                                    # If it's retired he wouldn't load on 
            print("He's retired.")
        else:
            self.bomb = bomb
            if self.bomb == 0:
                print(self.name, "hasn't got any bomb.")  
            else:
                print(self.name, "has loaded with", self.bomb,"tons bomb.")  
  
  
    def TakeOff(self, adress, bomb2drop=0):  
        
        if self.IsRetired():                                                                    # If it's retired he wouldn't take off
            print("He's retired.")
        else:
            self.bomb2drop = bomb2drop                                                          # with tonnes  
            self.adress = adress      
            self.bomb = self.bomb - self.bomb2drop  
            
            if self.bomb2drop == 0:
                print(self.adress,"has just visited by",self.name,".")
            else:                                                       # city or region  
                print(self.name,"has bombed:",self.adress,", with:", self.bomb2drop,"tons bombs.")  # informing the user

            if (self.bomb == 0) and (bomb2drop != 0):
                print("All bombs are dropped..")

KaraKartal = Jet("F22",2001)
print(KaraKartal.name,"is retired: ", KaraKartal.IsRetired())
KaraKartal.LoadOn(5)
KaraKartal.TakeOff("Hakkari",5)
print(KaraKartal.name, "has", KaraKartal.bomb, "tons bomb left.")

AkKartal = Jet("F5",1945)
print(AkKartal.name,"is retired: ", AkKartal.IsRetired())
AkKartal.LoadOn(4)
AkKartal.TakeOff("Afyon",0)
print(AkKartal.name, "has", AkKartal.bomb, "tons bomb left.")
