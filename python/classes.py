# class Point(): 
#     def __init__(self, input1, input2):
#         self.x = input1
#         self.y = input2
    
# p = Point(2, 8)
# print(p.x)
# print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seat():
            return False
        self.passengers.append(name)
        return True

    def open_seat(self):
        return self.capacity - len(self.passengers)
    
flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    # success = flight.add_passenger(person)
    # if success:
    if flight.add_passenger(person):
        print(f"Added {person} to flight succesfully.")
    else:
        print("No Available Seats for that {person}")