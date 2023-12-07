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
      
        for car in data["Cars"]:
            if car["Model"] == id:
                print(car)
                car_found = True
                return car  

        if not car_found:
            print("No Car Found")
            
    def update(year,make,model,vin,index,id):
        
        with open('CarInvetory.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            new_car = {"Year": year, "Make": make, "Model": model, "Vin": vin}
            #data.append(new_car)
        i = 0
        for car in data["Cars"]:
            i = i + 1
            if car["Model"] == id:
                car = new_car
                print(type(car))
                with open('CarInvetory.json','w') as file:
                    
                    json.dump(data,file,indent=4,separators=(', ',': '))
                car_found = True
                file.close()
                return car  

        if not car_found:
            print("No Car Found")
            jsonfile.close()
            
    
    def delete():
        pass
    
    def add(year,make,model,vin):
        with open('CarInvetory.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            new_car = {"Year": year, "Make": make, "Model": model, "Vin": vin}
            data["Cars"].append(new_car)
            jsonfile.close()
        with open('CarInvetory.json','w') as file:

            json.dump(data,file,indent=4,separators=(', ',': '))
            file.close()
        
    
       
        


#Manager.find("R34 Skyline")
year = "1990"
make = "Toyota"
model = "Supra"
vin = "JTYAS26KDNM261840"
Manager.add(year,make,model,vin)
#Manager.update(year,make,model,vin,1,"R34 Skyline")
