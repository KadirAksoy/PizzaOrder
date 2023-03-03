import csv
import datetime
from Pizza import *

def main():
    
    ###  MENÜ İÇİN DOSYADAN OKUMA ////  DOSYANA EKSTRA BİRKAÇ SATIR EKLENDİ...
    with open ('PizzaOrder/Menu.txt','r') as dosya:
        for line in dosya.read().splitlines():
            print(line)
    
    
    ### PİZZA SEÇİMİ İÇİN DÖNGÜ...
    while True:  
        pizza_choice = int(input("Lütfen bir pizza tabani seçip enter tuşuna basiniz:"))
            
        if pizza_choice == 1:
            pizza = KlasikPizza()
            break
        
        elif pizza_choice == 2:
            pizza = MargheritaPizza()
            break
        
        elif pizza_choice == 3:
            pizza = TürkPizza()
            break
        
        elif pizza_choice == 4:
            pizza = SadePizza()
            break
        
        elif pizza_choice == 5:
            pizza = BaharatliPizza()
            break
        
        elif pizza_choice == 6:
            pizza = AciliPizza()
            break
        
        elif pizza_choice == 7:
            pizza = İtalyanPizza() 
            break
        else :
            print("Hatali seçim .")
            
            
    ###  SOS SEÇİMİ İÇİN DÖNGÜ...
            
    while True:
        
        sos_seçim = int(input("Lütfen bir sos seçin:"))
        
        if sos_seçim == 11:
            sos = Zeytin(pizza)
            break
        
        elif sos_seçim == 12:
            sos = Mantar(pizza)
            break
        
        elif sos_seçim == 13:
            sos = KeçiPeyniri(pizza)
            break
        
        elif sos_seçim == 14:
            sos = Et(pizza)
            break
        
        elif sos_seçim == 15:
            sos = Soğan(pizza)
            break
        
        elif sos_seçim == 16:
            sos = Misir(pizza)
            break
        
        elif sos_seçim == 17:
            sos = Biber(pizza) 
            break
        
        elif sos_seçim == 18:
            sos = BoşSos(pizza)
        else :
            print("Hatali seçim .")
            
            
    ###  PİZZANIN AÇIKLAMASI VE FİYATI DEĞİŞKENLERE EKLENDİ...
            
    hazirlanan_pizza = sos.get_description()
    hazirlanan_pizza_fiyat = sos.get_cost()
    
    ### AÇIKLAMA VE FİYAT EKRANA YAZDIRILDI...
    
    print("İstediğiniz pizza :" , hazirlanan_pizza)
    print("Pizzanin fiyati : ", hazirlanan_pizza_fiyat)
    
    
    ### KULLANICIDAN BİLGİLER ALINDI...
    
    isim = input("Lütfen isminizi giriniz:")
    tc_kimlik = input("Lütfen tc kimlik numaranizi giriniz:")
    kredi_kart_numarasi = input("Lütfen kredi kart numaranizi giriniz:")
    kredi_kart_şifresi = input("Lütfen kredi kart şifrenizi giriniz:")
    
    ### BİLGİLERİNİ GİRDİKTEN SONRA ZAMANIN BİLGİLERİ ALINDI...
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    
    
    ### CSV DOSYASINA BİLGİLER YAZILDI..
    with open('PizzaOrder/Orders_Database.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow([isim,tc_kimlik,hazirlanan_pizza,hazirlanan_pizza_fiyat,timestamp,kredi_kart_numarasi,kredi_kart_şifresi])
    
    
    ### SİPARİŞ TAMAMLANMIŞTIR...
    print("Teşekkürler siparişiniz alinmiştir..")
        
        
    ### PROJEYİ HEM VS_CODE HEM DE IDEDE DENEDİM...
        
    
main()
    
