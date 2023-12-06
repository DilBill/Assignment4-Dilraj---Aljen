import json

class Manager:
    
    def showAll():
        
        with open('CarInvetory.json' , 'r') as jsonfile:
            data = json.load(jsonfile)

        for car in data :
            print(car['Year'],car['Make'] , car['Model'])
    
    
    def find(id):
        car_found = False

        with open('CarInvetory.json', 'r') as jsonfile:
            data = json.load(jsonfile)

        for car in data:
            if car["Model"] == id:
                print(car)
                car_found = True
                break  

        if not car_found:
            print("No Car Found")
            
    def update():
        pass
    
    def delete():
        pass
    
    def add():
        pass 
    
       
        


Manager.find("R34 Skyline")