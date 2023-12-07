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
            #data.append(new_car)
        i = 0
        for car in data["Cars"]:
            i = i + 1
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
make = "Mazda"
model = "Miata"
vin = "JMIAT26XDEO372951"
#Manager.add(year,make,model,vin)
Manager.update(year,make,model,vin,1,"CX-3")
