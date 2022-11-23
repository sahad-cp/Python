#parent class 
class person:
    def __init__(self,name,contact):
        self.name =name
        self.contact =contact
    def address(self):
        print(self.name,self.contact)   
#child class
class Doctor(person):
    pass
class patient(person):
    pass

doc1 = Doctor("jhone",1234567)
pat1 = patient("rahul",34567890)

doc1.address()
pat1.address()
        
    