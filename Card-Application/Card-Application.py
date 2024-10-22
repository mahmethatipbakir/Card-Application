# kart uygulamasi projesi
import random
#kart sinifi acilacak
# kart tipleri = karo sinek kupa maca
#kart degerleri = A ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9,10 ,J ,Q ,K
#Deste sinifindaki kartlar listesine 52 karti for ve list comphension ile ekleyiniz
#destede kalan kart sayisi icin kartsayisi() isminde bir metot
#destedefki kartlari karistirmak icin kartlarikaristir() isminde metot
#kartdagit isminde metot ile belirtilen adet kadar karti dagitmali destedeki kalan kart sayisina dikkat
# kartat() isminde metot ile elden bir kart atmak icin kullanilsin

class Kart:
    def __init__(self,tip,deger):
        self.tip = tip
        self.deger = deger
    def __repr__(self): # tanimlama anlaminda kullaniliyor
        return f"{self.tip} {self.deger}"

#kart sinifindan turetilen her bir nesne bir kart turunu temsil edecek
# kart sinifinin tip ve deger isminde 2 instance ozelliugi olacak .(tip sinek deger 5 )

#sinek5 = kart("sinek","5")
sinek5 = Kart("sinek","5")
print(sinek5)


kart_tip = ["karo","sinek","kupa","maca"]
kart_deger = ['A','1','2','3','4','5','7','8','9','10','Q','J','K']
for i in kart_tip:
    for j in kart_deger:
        Kart(i,j)


class Deste:
    kart_tip = ["karo","sinek","kupa","maca"]
    kart_deger = ['A','1','2','3','4','5','7','8','9','10','Q','J','K']
    def __init__(self):

        self.kartlar = [Kart(tip,deger)for tip in Deste.kart_tip for deger in Deste.kart_deger]
        #for i in kart_tip:
        #    for j in kart_deger:
        #        self.kartlar.append(Kart(i,j))
        print (self.kartlar)
    def kartsayisi(self):
        return len(self.kartlar)
    
    def kartlarikaristir(self):
        if (self.kartsayisi() < 52):
            raise ValueError("kartlari deste bozulmadan karistirabilirsiniz ")
        random.shuffle(self.kartlar)
        

    def kartdagit(self,adet):
        sayi_kart = self.kartsayisi()
        adet = min([sayi_kart,adet])
        if sayi_kart == 0 :
            raise ValueError( "butun kartlar dagitildi")
        adet = min([sayi_kart,adet])
        kartlar= self.kartlar[-adet:]
        self.kartlar = self.kartlar[:-adet]
        return kartlar
    
    def kartat(self):
        return self.kartdagit(1)[0]
    
        
deste1= Deste()
print (deste1.kartsayisi())
deste1.kartlarikaristir()

deste1.kartdagit(3)
print (deste1.kartsayisi())
