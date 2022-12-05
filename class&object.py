class cars:
    def __init__(self,name,price,color) :
        self.name = name
        self.price = price
        self.color = color
    def start(self):
        print(self.name , " engine started")
cars1 = cars("swift",500000,"red")
cars2 = cars("Innova",3200000,"grey")

print(cars1.name,cars1.price,cars1.color)
print(cars2.name,cars2.price,cars2.color)

cars1.price=200000
      
cars1.start()
cars2.start()