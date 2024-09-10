import json
import os

class Demo:
    def __init__(self):
        self.file = 'data.json'
        self.data = None  
        self.load() 

    def int(self):
        print("Enter 1 to add a car\nEnter 2 to start a car\nEnter 3 to stop a car\nEnter 4 to list the cars\nEnter 5 to exit\n")
        self.a = int(input("Enter your choice: "))
        self.add_car()

    def write_json(self):
        with open(self.file, 'w') as file:
            json.dump(self.data, file, indent=4)
            print("Data updated successfully!")

    def load(self):
        if os.path.exists(self.file):
            with open(self.file, 'r') as f:
                self.data = json.load(f)  
        else:
            self.data = {"emp_details": []}  

    def add_car(self):
        if self.a == 1:
            b = input("Are you here to enter new cars (y/n): ")
            if b.lower() == 'y':
                self.brand = input("Enter brand name: ")
                self.model = input("Enter model name: ")
                self.status = "off"
                self.data["emp_details"].append({
                    'brand': self.brand,
                    'model': self.model,
                    'status': self.status
                })
                self.write_json()
            else:
                self.int()
        elif self.a == 2:
            self.start_car()
        elif self.a == 3:
            self.stop_car()
        elif self.a == 4:
            self.display()
        elif self.a == 5:
            self.exit()

    def start_car(self):
        g1, g2 = input("Enter car brand and model to start: ").split(" ")
        for car in self.data.get('emp_details', []):
            if car['brand'] == g1 and car['model'] == g2:
                if car['status'] == 'off':
                    car['status'] = 'on'
                    print(f"Your car {g1} {g2} has started.")
                    self.write_json() 
                else:
                    print("Your car is already started.")
                break
        else:
            print("Car not found.")
        self.int()

    def stop_car(self):
        g1, g2 = input("Enter car brand and model to stop: ").split(" ")
        for car in self.data.get('emp_details', []):
            if car['brand'] == g1 and car['model'] == g2:
                if car['status'] == 'on':
                    car['status'] = 'off'
                    print(f"Your car {g1} {g2} has stopped.")
                    self.write_json() 
                else:
                    print("Your car is already stopped.")
                break
        else:
            print("Car not found.")
        self.int()

    def display(self):
        self.load()  
        for datas in self.data.get('emp_details', []):
            print(datas['brand'].rjust(1), datas['model'].rjust(4), "---->", datas['status'].rjust(6))
        self.int()

    def exit(self):
        print("Exiting...")
        


d = Demo()
d.int()
