import json

class Manager:
    # Method to allow all the user to show all items in the json file
    def showAll():
        # open file in read mode
        with open('CarInvetory.json' , 'r') as jsonfile:
            data = json.load(jsonfile)
        # print out all the cars in the json file
        allCars = []
        for car in data["Cars"]:
            cars = {car['Year'],car['Make'] , car['Model'], car['Vin']}
            allCars.append(cars)
        return allCars

        jsonfile.close()
        
    # Method to allow the user to find a single car in the json file
    def find(id,type):
        
        car_found = False
        # open json file in read mode
        with open('CarInvetory.json', 'r') as jsonfile:
            data = json.load(jsonfile)
        # find the car that the user is looking for based on the model or year
        for car in data["Cars"]:
            if car[type] == id:
                print(car)
                car_found = True
                return car  

        if not car_found:
            print("No Car Found")
            return False
    
    # Method that will allow the user to find and update the details of a car
    def update(year,make,model,vin,id):
        
        car_found = False
        with open('CarInvetory.json', 'r') as jsonfile:
            data = json.load(jsonfile)
        

        for car in data["Cars"]:
            if car["Model"] == id:
                print(type(car))
                print(car)
                yR = car["Year"]
                mK = car["Make"]
                mD = car["Model"]
                vN = car["Vin"]
                car["Year"] = car["Year"].replace(yR,year)
                car["Make"] = car["Make"].replace(mK,make)
                car["Model"] = car["Model"].replace(mD,model)
                car["Vin"] = car["Vin"].replace(vN,vin)
                
                with open('CarInvetory.json','w') as file:
                    
                    json.dump(data,file,indent=4,separators=(', ',': '))
                car_found = True
                file.close()
                print(car)
                return car  

        if not car_found:
            print("No Car Found")
            jsonfile.close()
            
    
    def delete(id):
        car_found = False
        with open('CarInvetory.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            
        i = 0
        for car in data["Cars"]:
            
            if car["Model"] == id:
                print(data["Cars"][i])
                print(type(car))
                print(car)
                del data["Cars"][i]
            
                
                with open('CarInvetory.json','w') as file:
                    
                    json.dump(data,file,indent=4,separators=(', ',': '))
                car_found = True
                file.close()
                return car  
            i = i + 1
        if not car_found:
            print("No Car Found")
            jsonfile.close()
    
    def add(year,make,model,vin):
        with open('CarInvetory.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            new_car = {"Year": year, "Make": make, "Model": model, "Vin": vin}
            data["Cars"].append(new_car)
            jsonfile.close()
        with open('CarInvetory.json','w') as file:

            json.dump(data,file,indent=4,separators=(', ',': '))
            file.close()
            
        return new_car
        
    
       
        


#Manager.find("R34 Skyline")
year = "2005"
make = "Acura"
model = "RSX"
vin = "JRSXL27XDEO041221"
#Manager.add(year,make,model,vin)
#Manager.update(year,make,model,vin,"Supra")
Manager.delete("Supra")
