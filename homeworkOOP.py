       
# class Cow:
#     def __init__(self,sound): 
#         self.sound = sound  
#     def make_sound(self): 
#         return "muuuuuuu"
    
# make_sound= Cow("Muuuuuu")
# print(make_sound.sound)


# class Cars:
#     def __init__(self, brand, model, year, odometer, type_of,volume,is_going): 
#         self.brand=brand
#         self.model = model
#         self.year = year
#         self.odometer =odometer
#         self.type_of = type_of
#         self.volume = volume
#         self.is_going = is_going

#     def car_is_going(self, km):
#         self.odometer += km
#         self.is_going = True
#         return f"{self.odometer},{self.is_going}"

#     def car_not_going(self,is_going=False):
#         return f"{self.is_going}"
# Munar= Cars("Mitsubishi", 'Montero sport', 2021, 1000, 'SUV', 3,True)
# print(Munar.car_is_going(2000))
# print(Munar.car_not_going(0))


# class Airplane :
#     def __init__(self,make, model, year, max_speed, odometer, is_flying):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.max_speed=max_speed
#         self.odometer=odometer
#         self.is_flying=False

#     def take_off(self,odometer):
#         self.odometer+=0
#         self.is_flying=True
      
#     def fly(self,mile):
#         self.max_speed+=mile

#     def land(self,is_flying):
#         self.is_flying=is_flying
#         self.is_flying=False

#     def info_about_fly(self):
#         return F"{self.max_speed}"

#     def info_about_plane(self):
#         return F"{self.make}, {self.model}, {self.year}, {self.max_speed}, {self.odometer}, {self.is_flying}"
# munar=Airplane("Boing 787-9","JET","2021",5474,0,False)
# munar.take_off(0)
# munar.fly(1000)
# print(munar.info_about_fly())
# print(munar.info_about_plane())
