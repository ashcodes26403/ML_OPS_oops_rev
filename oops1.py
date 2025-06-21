# initiate a class

class Employee:

    #dunder method - constructor
    def __init__(self):
        print("started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "Manager"
        print("attributes/data executed")

    def travel(self, destination):
        print("started travelling")
        print(f"Employee {self.id} is travelling to {destination}")
        print("travelling completed")

sam = Employee()
sam.name = "Sam Kumar"
print(sam.name)
sam.travel("Mumbai")

print(type(sam)) #<class '__main__.Employee'>