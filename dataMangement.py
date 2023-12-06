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
    
    def add(year,make,model,vin):
        data =[]
        with open('CarInvetory.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            new_car = {"Year": year, "Make": make, "Model": model, "Vin": vin}
            print(type(data))
            data.append(new_car)
        with open('CarInvetory.json','w') as file:

            json.dump(data,file,separators=(', ',': '))
        
    
       
        


Manager.find("R34 Skyline")
year = "2023"
make = "Honda"
model = "Civic"
vin = "1HMNG52CVNM110297"
Manager.add(year,make,model,vin)