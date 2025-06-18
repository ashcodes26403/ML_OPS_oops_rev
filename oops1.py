# initiate a class

class Employee:

    #dunder method - constructor
    def __init__(self, id, salary, designation):
        print("started executing attributes/data")
        self.id = id
        self.salary = salary
        self.designation = designation
        print("attributes/data executed")

    def travel(self, destination):
        print("started travelling")
        print(f"Employee {self.id} is travelling to {destination}")
        print("travelling completed")

sam = Employee(1, 10000, "Manager")
sam.travel("Mumbai")

print(type(sam)) #<class '__main__.Employee'>