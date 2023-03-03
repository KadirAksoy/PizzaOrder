###### PİZZA SINIFI VE PİZZALAR ######3

class Pizza():
    def __init__(self, cost, description):
        self.description = description
        self.cost = cost
        
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost
    
class SadePizza(Pizza):
    price = 50 
    description = "Özel sos, sucuk, kaşar"
    def __init__(self):
        super().__init__(self.price,self.description)
    
class KlasikPizza(Pizza):
    price = 60
    description = "Özel sos, sucuk, kaşar peyniri, zeytin"
    def __init__(self):
        super().__init__(self.price,self.description)
    
class TürkPizza(Pizza):
    price = 75
    description = "Özel sos, sucuk, kaşar peyniri, zeytin, salam, çedar peyniri"
    def __init__(self):
        super().__init__(self.price,self.description)
    
class MargheritaPizza(Pizza):
    price = 70
    description = "Özel sos, margarita sosu, sucuk , kaşar peyniri"
    def __init__(self):
        super().__init__(self.price,self.description)
        
class BaharatliPizza(Pizza):
    price = 65
    description = "Özel sos, margarita sosu, sucuk , kaşar peyniri, özel baharat"
    def __init__(self):
        super().__init__(self.price,self.description)
    
class AciliPizza(Pizza):
    price = 65
    description = "Özel sos, margarita sosu, sucuk , kaşar peyniri, özel aci baharat"
    def __init__(self):
        super().__init__(self.price,self.description)
    
class İtalyanPizza(Pizza):
    price = 100
    description = "Özel sos, margarita sosu, sucuk , kaşar peyniri, mozerella peyniri, çedar peyniri, italyan sos"
    def __init__(self):
        super().__init__(self.price,self.description)
        
        
        
        
        
        
 ####      DECORATOR SINIFI VE SOSLAR     #######       
        
class Decorator(Pizza):
    def __init__(self, component):
        self.component = component
    
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)
    
    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)
    
class Zeytin(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.cost = 3
        self.description = "ve zeytin sosu ile hazirlanmiş pizza."

class Mantar(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.cost = 3
        self.description = "ve mantar sosu ile hazirlanmiş pizza."

class KeçiPeyniri(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.cost = 5
        self.description = "ve keçi peyniri sosu ile hazirlanmiş pizza."

class Et(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.cost = 10
        self.description = "ve et sosu ile hazirlanmiş pizza."

class Soğan(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.cost = 4
        self.description = "ve soğan sosu ile hazirlanmiş pizza."

class Misir(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.cost = 5
        self.description = "ve misir sosu ile hazirlanmiş pizza."  
        
class Biber(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.cost = 6
        self.description = "ve biber sosu ile hazirlanmiş pizza."  
        
class BoşSos(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.cost = 0
        self.description = "ile hazirlanmiş , sos kullanilmamiş pizza."  
         
         
#b = MargheritaPizza()
#a = BoşSos(b)
#c = a.get_cost()
#d = a.get_description()

#print(c)
    
    

   
   


